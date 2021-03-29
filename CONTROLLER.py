#This module is responsible for the User's interaction with the game
####################################################################---------AUXILIARY FUNCTIONS---------########################################################################


#
def ShowStatistic(Table_Of_Characters): #This feature allows the Player to get information about the progress of the battle (in real time)
    print("Battle reports")
    for i in Table_Of_Characters:
        if i.IsAlive == False:
            continue
        if i.IsHuman == True:
            print("\t\t\tYour fighter. %s. The serial number of the fighter. %i. Class %s. Damage %i. Health %i / %i. Energy reserve %i \n"%(i.name, i.Number, i.Class, i.damage, i.health, i.MaxHealth, i.energy))
        else:
            print("\t\t\tEnemy fighter. %s. The serial number of the fighter. %i. Class %s. Damage %i. Health %i / %i. Energy reserve %i \n"%(i.name, i.Number, i.Class, i.damage, i.health, i.MaxHealth, i.energy))
#


#
def ShowScale(List_Of_Iniziative): #The player can ask to display the initiative scale on the screen
    for i in List_Of_Iniziative:
        if i[0].IsHuman == True:
                print('\tThe player"s fighter' , i[0].name, ' walks', '(', i[0].Number,  ') initiative: ', i[1])
        else:
                print('\tThe enemy fighter' , i[0].name, ' walks', '(', i[0].Number,  ') initiative: ', i[1])
        
#

#
def TableForWarrior(GroupAI): #This function generates a table for the player's heroes of the "Warrior" class. Unlike the AI table, this table is a list
    List_Of_Warriors = []
    for i in GroupAI:
        if i.Class == "Warrior"  and i.IsAlive == True:
            List_Of_Warriors.append(i)
    return List_Of_Warriors
#

#    
def CheckWaiting(Player, Wait_List): #Each character can only use "Waiting" once per round
    for i in Wait_List:
        if i == Player:
            print(" We can't wait any longer, we must act!")
            return False
    return True #True - end turn, false - wait for new command
#




#######################################################################---------MAIN FUNCTIONS---------##########################################################################


#This" Controller " is the base for all the others. It performs the functions common to all characters
def BaseController(Command, Player, Table_Of_Characters, List_Of_Iniziative, Wait_List):
    
    This_Command_Is_Not_Here = -1 #The command is not present here, you need to check the calling controller, if necessary, repeat the input
    Exit_And_Restart = 0 #The player has decided to give up, you need to go out and offer to play a new game
    Continue_The_Turn = 1 #The character's turn does not end, waiting for a new command
    Pass_The_Turn_To_The_Next = 2 #The player was like, pass the move to the next one
    
    
    if Command == "stat": #This command calls a function that displays a summary
        ShowStatistic(Table_Of_Characters)
        return Continue_The_Turn #The move didn't end
        
    if Command == "scale": #This command calls a function that displays the initiative scale (and some other information)
        ShowScale(List_Of_Iniziative)
        return Continue_The_Turn #The move didn't end
        
    if Command == "def": #This command calls the __defense__ method on the class object
        Player.__defence__()
        return Pass_The_Turn_To_The_Next #End of turn
        
    if Command == "wait": #This command implements the "Waiting" mechanic
        if not CheckWaiting(Player, Wait_List): #A character cannot delay a turn twice in a round
            return Continue_The_Turn #The move didn't end
        Player.__wait__(Wait_List) #If not, add to the list of "Waiting", the turn ends, the player did not give up
        return Pass_The_Turn_To_The_Next #End of turn
        
    if Command == "retry":#This command restarts the game session
        return Exit_And_Restart #Exit the game and offer to start a new match
    
    return This_Command_Is_Not_Here #If you have reached this place - the entered command is not here
#
            
#This "Controller" is responsible for the interaction of the player character of the "Bowman" class (and mages attacking single targets) or "Warrior" (only if the enemy "Warrior" is dead) with the game
def Controller(Player, GroupOfAI, Table_Of_Characters, List_Of_Iniziative, Wait_List):
    while True:
            GameOver = False #This variable will become true if the player decides to give up
            Success = False  # The variable is responsible for whether the command is successful
            Command = input('Your Turn! ') #Player's turn, waiting for the command input
            Command = Command.lower()
            
           #First we check the unique controller commands
            
            for i in GroupOfAI: 
                if Command == ("atk %i"%(i.Number)): #We check whether the player entered the correct number
                    if i.IsAlive == False:
                        print("The enemy is already dead")
                        break
                    Player.__attack__(i) #Calling the __attack__ method on the object
                    Success = True
            if Success: #This is necessary to complete the move
                break
                
            for i in GroupOfAI: 
                if Command == ("skl %i"%(i.Number)): #We check whether the goal is specified correctly
                    if Player.energy < 25: #Mana is required to use the skill
                        print("Not enough energy")
                        break
                    if i.IsAlive == False:
                        print("The enemy is already dead")
                        break
                    Player.__skill__(i) #Calling the __skill__ method on the object
                    Success = True
            if Success:
                break
            
            #Then, if no matches are found, call BaseController
            
            Opcode = BaseController(Command, Player, Table_Of_Characters, List_Of_Iniziative, Wait_List)
            if Opcode == 0: #If the first value is 0, the move continues, waiting for a new command
                GameOver = True
                break
            elif Opcode == 1: #If the first value is 1 - end of turn
                continue
            elif Opcode == 2: #End of turn
                break
            #Else - the command is incorrect
            print("The command is incorrect. Repeat the input")
    return GameOver #A false will always be returned if the player does not plan to give up       
#



#This "Controller" is responsible for the interaction of the player character of the "Warrior" class with the game
def ControllerWarrior(Player, GroupOfAI, Table_Of_Characters, List_Of_Iniziative, Wait_List):
    GameOver = False #If it gives up, it becomes the truth
    TablePlayer = TableForWarrior(GroupOfAI) #The warrior needs to get information about the presence of enemy " Warrior"
    if not TablePlayer: #If there are no "Warrior" left alive in the enemy's squad, the warrior can attack as Bowman
        Controller(Player, GroupOfAI, Table_Of_Characters, List_Of_Iniziative, Wait_List)
    else:
        while True:
            Success = False
            Command = input('Your Turn! ')
            Command = Command.lower()
            
           
            
            for i in TablePlayer: #A warrior, if there are combat-ready enemy "Warriors", can only attack them
                if Command == ("atk %i"%(i.Number)):
                    if i.IsAlive == False:
                        print("The enemy is already dead")
                        break
                    Player.__attack__(i) #Calling the __attack__ method on this object
                    Success = True
            
            if Success:
                break
            
            for i in TablePlayer: #A warrior, if there are combat-ready enemy "Warriors", can only attack them
                if Command == ("skl %i"%(i.Number)):
                    if Player.energy < 25: #Check energy
                        print("Not enough energy")
                        break
                    if i.IsAlive == False:
                        print("The enemy is already dead")
                        break
                    Player.__skill__(i) 
                    Success = True
            if Success:
                break
            #If there are no matches, delegate the BaseController authority
            
            Opcode = BaseController(Command, Player, Table_Of_Characters, List_Of_Iniziative, Wait_List)
            if Opcode == 0: #If the first value is 0, the move continues, waiting for a new command
                GameOver = True
                break
            elif Opcode == 1: #If the first value is 1 - end of turn
                continue
            elif Opcode == 2: #End of turn
                break
            #So returned -1 - no matches
            print("In the enemy group, there are warriors who protect their comrades") #If you have reached this point, it means that the player either specified the wrong goal
            for i in TablePlayer:                                                    #or entered the wrong command
                print("\t%s (%i)"%(i.name, i.Number))
    return GameOver #A false will always be returned if the player does not plan to give up
#




#This "Controller" is responsible for the interaction of the player character of the "Wizard" class with the game 
def ControllerWizard(Player, GroupOfAI, Table_Of_Characters, List_Of_Iniziative, Wait_List):
    while True:
            GameOver = False
            Command = input('Your Turn! ')
            Command = Command.lower()
            
            #Checking unique commands
            
            if Command == "atk": # The Wizard attacks the entire enemy squad, there is no need for him to perform checks
                Player.__attack__(GroupOfAI) #Base attack
                break
            if Command == "skl":
                if Player.energy < 25: #Check energy
                    print("Not enough energy")
                    continue
                Player.__skill__(GroupOfAI) #Powerful cast
                break
            #No matches found - call BaseController
            
            Opcode = BaseController(Command, Player, Table_Of_Characters, List_Of_Iniziative, Wait_List)
            if Opcode == 0: #If the first value is 0, the move continues, waiting for a new command
                GameOver = True
                break
            elif Opcode == 1: #If the first value is 1 - end of turn
                continue
            elif Opcode == 2: #End of turn
                break
            #So returned -1 - no matches
            print("The command is incorrect. Repeat the input")
    return GameOver #A false will always be returned if the player does not plan to give up
#


#This "Controller" is responsible for the interaction of the player character of the "HealingAll" class with the game
def ControllerHealer(Player, GroupOfPlayer, Table_Of_Characters, List_Of_Iniziative, Wait_List):
    while True:
            GameOver = False
            Command = input('Your Turn! ')
            Command = Command.lower()
            #We check for a match with unique commands
            
            if Command == "heal": #This healer heals the entire group, you don't need to specify anything else to call the method
                Player.__attack__(GroupOfPlayer) 
                break
            
            if Command == "skl": #This healer heals the entire group, you don't need to specify anything else to call the method
                if Player.energy < 25: #Check energy
                    print("Not enough energy")
                    continue
                Player.__skill__(GroupOfPlayer)
                break
            #Else - BaseController
            
            Opcode = BaseController(Command, Player, Table_Of_Characters, List_Of_Iniziative, Wait_List)
            if Opcode == 0: #If the first value is 0, the move continues, waiting for a new command
                GameOver = True
                break
            elif Opcode == 1: #If the first value is 1 - end of turn
                continue
            elif Opcode == 2: #End of turn
                break
            #Means returned -1-the command is incorrect
            print("The command is incorrect. Repeat the input")
    return GameOver
#


#This "Controller" is responsible for the interaction of the player character of the "Healer" class with the game
def ControllerSoloHealer(Player, GroupOfPlayer, Table_Of_Characters, List_Of_Iniziative, Wait_List):
    while True:
            GameOver = False
            Success = False
            Command = input('Your Turn! ')
            Command = Command.lower()
            #We first check the unique commands
            
            for i in GroupOfPlayer:
                if Command == ("heal %i"%(i.Number)): #Checking the command for correctness
                    if i.IsAlive == False:
                        print("The associate is dead")
                        break
                    Player.__attack__(i) #Base healing
                    Success = True
            if Success:
                break
                
            for i in GroupOfPlayer:
                if Command == ("skl %i"%(i.Number)): #Checking the command for correctness
                    if Player.energy < 25:
                        print("Not enough energy")
                        break
                    if i.IsAlive == False:
                        print("The associate is dead")
                        break
                    Player.__skill__(i) #Powerful healing
                    Success = True
            if Success:
                break
            Opcode = BaseController(Command, Player, Table_Of_Characters, List_Of_Iniziative, Wait_List)
            if Opcode == 0: #If the first value is 0, the move continues, waiting for a new command
                GameOver = True
                break
            elif Opcode == 1: #If the first value is 1 - end of turn
                continue
            elif Opcode == 2: #End of turn
                break
            #Means returned -1 - the command is incorrect
            print("The command is incorrect. Repeat the input")
            
    return GameOver
#

