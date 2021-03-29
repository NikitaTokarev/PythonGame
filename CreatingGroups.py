#Module for creating player and AI groups

from time import sleep
from random import randint
from PlayingHeroes import*
from InfoList import*

#######################################################################---------AUXILIARY FUNCTIONS---------#####################################################################
#
def Reincarnation(Table_Of_Characters): #We resurrect all the heroes
    for i in Table_Of_Characters:
        i.IsHuman = False
        i.IsAlive = True
        i.health = i.MaxHealth
        i.energy = i.MaxEnergy
        i.priority = i.UsualPriority
#

#
def CreateRandomGroup(GroupOfPlayers, TotalCharacters, Human = False):  #A function that creates a random group (can work for both the player and the AI)
                                                                        #The first parameter is the player group, which is required to create unique heroes (for the AI group)
    InGroup = 0   #Shows how many units are in the squad                #The second parameter is a list of all the game characters from the Playing Heroes module
    Count = 5     #How many units should there be in total              #The third parameter-initializes whose squad it is (by default, a group is created for the AI)
    Group = []    #The group to return
    Random = [-1] * 5  #A list that will contain the numbers of already created characters (to exclude repetitions)
    
    Range = TotalWarrior  # A range that is set to a variable from the Playing Heroes module that shows the number of the last character of the Warrior class
                          #This is done to ensure that there is at least one Warrior class unit in a random group
    
    
    while InGroup < Count: #The cycle continues until the squad is formed
        if InGroup == 1:
            Range = TotalCharacters #After a warrior is generated in the group, we change the range
        Opponent = randint(1, Range) #The number will correspond to the number of the Warrior class Warrior
        while Opponent == GroupOfPlayers[0].Number or Opponent == GroupOfPlayers[1].Number or Opponent == GroupOfPlayers[2].Number\
        or Opponent == GroupOfPlayers[3].Number or Opponent == GroupOfPlayers[4].Number or Opponent == Random[0]\
        or Opponent == Random[1] or Opponent == Random[2] or Opponent == Random[3] or Opponent == Random[4]:
            Opponent = randint(1, Range) #If such a character already exists in the squad (player or AI), you need to create a new one
            
        GamingCharacters[Opponent-1].IsHuman = Human #Transferring control
        Group.append(GamingCharacters[Opponent-1])   #Adding the selected character to the group
        Random[InGroup] = Opponent                   #Adding the generated number to the list
        InGroup+=1                                   #Increasing the counter value
    
    
    return Group #Returning the created group
#
#######################################################################---------MAIN FUNCTIONS---------##########################################################################

#
def CreatePlayerGroup(): #Function that creates a player's group
       
        Manual() #We invite the player to read the manual (the function is located in the InfoList module)
        CharacterInformation(GamingCharacters) #Call the function that displays all available units (the function is located in the Info List module)
        
        print(" Choose your fighters, wanderer.\n You can try your luck and go into battle with a random squad. To do this, press '0'\n\n")
        
        
        GroupOfPlayer = [Nothing] * 5 #Creating a list that will contain the player's heroes. Initialize it with empty objects of the Warrior class
        InYourGroup = 0  #Counter to track the number of warriors in the player's squad
    
        sleep(0.5)
    
        while InYourGroup < 5: #So far, there are less than five fighters in the squad
            try:
                Choise = int(input('Your choice '))
            except:
                print(" Repeat the input")
                continue
            if Choise == 0:
                GroupOfPlayer = CreateRandomGroup(GroupOfPlayer, TotalCharacters, True)  #Calling the function to create a random group (the function is above)
                break
            if Choise == GroupOfPlayer[0].Number or Choise == GroupOfPlayer[1].Number or Choise == GroupOfPlayer[2].Number\
            or Choise == GroupOfPlayer[3].Number or Choise == GroupOfPlayer[4].Number: #Making a check for uniqueness
                print(" This character is already present in the squad")
                continue
            if Choise > 0 and Choise <= TotalCharacters: #If the selected character exists, we transfer it to the player's control, add it to the player's group and increase the counter
                GamingCharacters[Choise-1].IsHuman = True
                GroupOfPlayer[InYourGroup] = GamingCharacters[Choise-1]
                InYourGroup+=1
                print(" Selected: ",GamingCharacters[Choise-1].name)
            else:
                print(" The character under this number is not in the list")
                continue
   
        print("\n\tYour group\n") #Output the player's group
        for i in GroupOfPlayer:
            print(' ', i.name)
        return GroupOfPlayer #Returning the created group
#        
    

#
def CreateAIGroup(GroupOfPlayer): #Function for creating an AI group

    GroupOfAI = [] #A list that will contain the enemy group
    
    GroupOfAI = CreateRandomGroup(GroupOfPlayer, TotalCharacters) #Creating an enemy group by calling the necessary function
                                                                  #Parameters pass the ALREADY created player group and a list of all the characters from the PlayingHeroes module
        
      
    print("\n\tEnemy group\n") 
    for i in GroupOfAI: #Printing the enemy group
        print(' ', i.name)
        
    sleep(0.75)
    
    return GroupOfAI #Returning the created enemy group
#

#   
def CreateTableOfCharacters(GroupOfPlayer, GroupOfAI): #Function to create a table containing all the selected game characters
    Table_Of_Characters = [GroupOfPlayer[0], GroupOfPlayer[1], GroupOfPlayer[2], GroupOfPlayer[3], GroupOfPlayer[4],
                       GroupOfAI[0], GroupOfAI[1], GroupOfAI[2], GroupOfAI[3], GroupOfAI[4]] #Enter the heroes from both groups in the table
    return Table_Of_Characters #Returning the table of selected heroes
#    
    
