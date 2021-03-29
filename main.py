#Entry Point

#Include the necessary modules
from CreatingGroups import CreatePlayerGroup, CreateAIGroup, CreateTableOfCharacters, Reincarnation
from BattleField import BATTLE



#Endless game cycle
while True:
    
    GroupOfPlayer = CreatePlayerGroup() #Calling the function to create the player's group (the function is located in the CreatingGroups module)
    
    GroupOfAI = CreateAIGroup(GroupOfPlayer) #Calling the function to create the AI's group (the function is located in the CreatingGroups module)
    

    Table_Of_Characters = CreateTableOfCharacters(GroupOfPlayer, GroupOfAI) #Calling a function that will create a table containing characters from BOTH groups
                                                                            #(the function is located in the CreatingGroups module)
   
    BATTLE(GroupOfPlayer, GroupOfAI, Table_Of_Characters) #Run the main function of this game and pass it the necessary arguments
                                                                              #(the function is located in the BattleField module)
    
    run = input('\nShall we play another game? If yes, press X ' ) #The game is over, we suggest you play again
    run = run.lower()
    if run == "x" or run == "х": 
        Reincarnation(Table_Of_Characters)
        print(chr(27) + "[2J")
    else:
        break
    
#END




