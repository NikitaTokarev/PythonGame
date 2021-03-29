#This module starts the battle and is responsible for its progress


from time import sleep
from random import randint

from AI import*
from CONTROLLER import*

#These two global variables are responsible for ending the battle
VictoryPlayer = False
VictoryAI = False

####################################################################---------AUXILIARY FUNCTIONS---------########################################################################

#
def Check(GroupOne, GroupTwo): #This function is called to check for victory/defeat
    global VictoryPlayer
    global VictoryAI
    
    count = 0 #This variable counts the number of dead heroes in the squad
    
    for i in GroupOne: #The enemy group is checked first
        if i.IsAlive == False:
            count+=1
    if count == 5: #If the entire squad is dead, the player wins
        VictoryPlayer = True
        return
    
    count = 0 
    
    for i in GroupTwo: #Checking the player's group
        if i.IsAlive == False:
            count+=1
    if count == 5: #If the entire squad is killed, the AI wins
        VictoryAI = True
        return 
#    
        
        
#    
def ShowStatistic(Table_Of_Characters): #This function outputs statistics at the end of each round
    print(" Round results")
    for i in Table_Of_Characters: #We go through the table, which contains units from the player's groups and AI
        if i.IsAlive == False: #If the character is dead, do not include it in the statistics
            continue
        if i.IsHuman == True: #If the character is in the player's group, print the following
            print("\t\tYour fighter. Damage %i. The hero of %s has %i health points and %i energy points left"%(i.damage, i.name, i.health, i.energy))
        else:                #Otherwise
            print("\t\tEnemy fighter. Damage %i. The hero of %s has %i health points and %i energy points left"%(i.damage, i.name, i.health, i.energy))
#


#######################################################################---------MAIN FUNCTIONS---------##########################################################################


#
def BATTLE(GroupOfPlayer, GroupOfAI, Table_Of_Characters): #This function is responsible for the battle
    Round = 1 #Round reference point
    while True: #Exit the loop only when one of the VictoryPlayer or VictoryAI variables becomes true
        
        global VictoryPlayer
        global VictoryAI
        VictoryPlayer = False
        VictoryAI = False
        
        print("\n\t\t\t\tROUND %i" %(Round)) #Round counter
        sleep(0.5)
        
        Table_Of_Iniziatives = {} #Creatures move according to their initiative + spread from 0 to 10. Here this table is compiled
        for i in Table_Of_Characters: #Moving through the table with the selected characters
            if i.IsAlive == False:    #The dead are not counted
                continue
            IniziativeControl = i.iniziative + randint(0,10) #Generating a " control initiative"
            Table_Of_Iniziatives[i] = IniziativeControl #Adding the result to the dictionary
        List_Of_Iniziative = list(Table_Of_Iniziatives.items()) #Creating a list of tuples: the first value is an object of the class, the second is its initiative
        List_Of_Iniziative.sort(reverse = True,key = lambda i: i[1]) #Sort by initiative (from larger to smaller)
        
        Wait_List = [] #The player has the option to delay the move. The waiting heroes will walk at the end of the round in reverse order
        
        print(" In this round, the heroes move in the following order")
        for i in List_Of_Iniziative: #Output the order of moves in this round
            if i[0].IsHuman == True:
                print('\tThe player"s fighter' , i[0].name, ' walks', '(', i[0].Number,  ') initiative: ', i[1])
            else:
                print('\tThe enemy fighter' , i[0].name, ' walks', '(', i[0].Number,  ') initiative: ', i[1])
        print("\n")
        
        for i in List_Of_Iniziative: #Moving through the list of initiatives
            if i[0].IsAlive == False: #If the hero does not live up to his turn - skip it
                continue
            sleep(0.5)
            
            print("\n\tХодит герой %s (%s)\n"%(i[0].name, i[0].Class))
            if i[0].IsHuman == True: #If the character is in the player's group
                if i[0].Class == "Warrior": #If a unit of the Warrior class-pass control to the ControllerWarrior function from the CONTROLLER module
                    VictoryAI = ControllerWarrior(i[0], GroupOfAI, Table_Of_Characters, List_Of_Iniziative, Wait_List)# The player can give up, then the truth will return
                    
                if i[0].Class == "Bowman": #If a unit of the Archer class - pass control to the Controller function from the CONTROLLER module
                    VictoryAI = Controller(i[0], GroupOfAI, Table_Of_Characters, List_Of_Iniziative, Wait_List)# The player can give up, then the truth will return
                    
                if i[0].Class == "Wizard": #If a unit of the Wizard class - pass control to the Controller Wizard function from the CONTROLLER module
                    VictoryAI = ControllerWizard(i[0], GroupOfAI, Table_Of_Characters, List_Of_Iniziative, Wait_List)# The player can give up, then the truth will return
                    
                if i[0].Class == "HealingAll": #If a unit of the Healer class (general) - pass control to the ControllerHealer function from the CONTROLLER module
                    VictoryAI = ControllerHealer(i[0], GroupOfPlayer, Table_Of_Characters, List_Of_Iniziative, Wait_List)# The player can give up, then the truth will return
                if i[0].Class == "Healer": #If a unit of the Healer class (single) - pass control to the ControllerSoloHealer function from the CONTROLLER module
                    VictoryAI = ControllerSoloHealer(i[0], GroupOfPlayer, Table_Of_Characters, List_Of_Iniziative, Wait_List)# The player can give up, then the truth will return
                print("\n")
                Check(GroupOfAI, GroupOfPlayer) #After the player character's turn, we make a check
                if VictoryPlayer:
                    print("\t\t\t\t\tVICTORY!!!")
                    break
                if VictoryAI:
                    print("\t\t\t\t\tDEFEAT")
                    break
            else: #If the character is in an AI group
                if i[0].Class == "Warrior": #If a unit of the Warrior class - pass control to the TurnAIWarrior function from the AI module
                    TurnAIWarrior(i[0], GroupOfPlayer)
                   
                if i[0].Class == "Bowman": #If a unit of the Archer class-pass control to the Turn AI function from the AI module
                    TurnAI(i[0], GroupOfPlayer)
                    
                if i[0].Class == "Wizard": #If a unit of the Wizard class - pass control to the TurnAIWizard function from the AI module
                    TurnAIWizard(i[0], GroupOfPlayer)
                    
                if i[0].Class == "HealingAll": #If a unit of the Healer class (general) - pass control to the TurnAIHealer function from the AI module
                    TurnAIHealer(i[0], GroupOfAI)
                if i[0].Class == "Healer": #If a unit of the Healer class (single) - pass control to the TurnAISoloHealer function from the AI module
                    TurnAISoloHealer(i[0], GroupOfAI)
                print("\n")
                Check(GroupOfAI, GroupOfPlayer) #After the turn of the AI character, we make a check
                if VictoryAI:
                        print("\t\t\t\t\tDEFEAT")
                        break
        
        if VictoryPlayer or VictoryAI: #If win / lose - exit the loop
            break
        if Wait_List: #If a character has postponed a move, it passes at the end of the round
            for i in reversed(Wait_List): #Но порядок ходов будет обратным "ожиданию"
                if i.IsAlive == True:
                    print("\n\tХодит герой %s (%s)\n"%(i.name, i.Class))
                    if i.IsHuman == True: 
                        if i.Class == "Warrior": 
                            VictoryAI = ControllerWarrior(i, GroupOfAI, Table_Of_Characters, List_Of_Iniziative, Wait_List)
                        if i.Class == "Bowman": 
                            VictoryAI = Controller(i, GroupOfAI, Table_Of_Characters, List_Of_Iniziative, Wait_List)
                        if i.Class == "Wizard": 
                            VictoryAI = ControllerWizard(i, GroupOfAI, Table_Of_Characters, List_Of_Iniziative, Wait_List)
                        if i.Class == "HealingAll": 
                            VictoryAI = ControllerHealer(i, GroupOfPlayer, Table_Of_Characters, List_Of_Iniziative, Wait_List)
                        if i.Class == "Healer": 
                            VictoryAI = ControllerSoloHealer(i, GroupOfPlayer, Table_Of_Characters, List_Of_Iniziative, Wait_List)
                            
                        print("\n")
                        Check(GroupOfAI, GroupOfPlayer) 
                        if VictoryPlayer:
                            print("\t\t\t\t\tVICTORY!!!")
                            break
                        if VictoryAI:
                            print("\t\t\t\t\tDEFEAT")
                            break
        if VictoryPlayer or VictoryAI:
            break            
        ShowStatistic(Table_Of_Characters) #Displaying statistics for the round
        Round +=1 #Increasing the round counter
#        
