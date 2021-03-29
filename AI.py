#Artificial Intelligence is registered in this module

####################################################################---------AUXILIARY FUNCTIONS---------########################################################################


#
def TableForWarrior(Group): #The warriors in this game have their own mechanics. They can't attack anyone else while the Warrior class hero is still alive in the enemy group.
                            #This function allows to implement it, forming information about the presence of a hero of the Warrior class in the enemy group
                            
    Cortege_Of_Warriors = {} #Creating a dictionary
    for i in Group:
        if i.Class == "Warrior"  and i.IsAlive == True: 
            Cortege_Of_Warriors[i] = i.priority #Entering the dictionary of "living" Warriors: the key is an object of the class, the value is its priority
        
    List_Of_Warriors = list(Cortege_Of_Warriors.items()) #Creating a list of tuples
    List_Of_Warriors.sort(reverse = True,key = lambda i: i[1]) #Sort from highest priority to lowest priority
    return List_Of_Warriors #Returning the resulting table
#    
    
    
#    
def TableForHeal(GroupOfAI): #AI clerics need to know who to treat. This function generates a special table for them

    Cortege_Of_SoloHealerAI = {} #Creating a dictionary
    for i in GroupOfAI: #Moving through the AI group
        if i.IsAlive == True: #We only add live brothers
            Cortege_Of_SoloHealerAI[i] = i.health / i.MaxHealth #The value is the ratio of the current health to the maximum
        
    List_Of_SoloHealer = list(Cortege_Of_SoloHealerAI.items()) #Creating a list of tuples
    List_Of_SoloHealer.sort(key = lambda i: i[1]) #Sort in order from SMALLER to LARGER
    #Next, you need to get the value from the first tuple of the first element (this will be the object of the class with the lowest ratio of the current health to the maximum)
    count = 0 
    for i in List_Of_SoloHealer:
        A = i[0]
        count = 1
        if count == 1:
            break
    return A #Returning this class object
#   
    
#######################################################################---------MAIN FUNCTIONS---------##########################################################################  
    
    
#    
def TurnAI(AI, GroupOfPlayer): #This function is responsible for the behavior of the AI class " Bowman"
    Cortege_Of_Priorities = {} #Creating a dictionary
    for i in GroupOfPlayer:
        if i.IsAlive == True:
            Cortege_Of_Priorities[i] = i.priority #The key is an object of the AllHeroes class, the value is the priority of this object
        
    List_Of_Priorities = list(Cortege_Of_Priorities.items()) #Creating a tuple sheet
    List_Of_Priorities.sort(reverse = True,key = lambda i: i[1]) #Finding the highest priority
    for i in List_Of_Priorities: #AI looks at the priority table
        if (i[0].IsDef == False and (i[0].health - AI.damage + 45) < 0) or (i[0].IsDef == True and (i[0].health - AI.damage + 50)/2 < 0) or AI.energy < 25: #If the AI finishes the character with a normal attack or the AI doesn't have enough energy, just attack
            AI.__attack__(i[0])
            break
        else: #Else - attacks it with a strong attack
            AI.__skill__(i[0])
            break
    
#

#    
def TurnAIWarrior(AI,GroupOfPlayer): #This function is responsible for the behavior of the AI class "Warrior"
    
    TableAI = TableForWarrior(GroupOfPlayer) #First you need to get a table
    if not TableAI: #If there is NO ONE in the table, the AI behaves like "Bowman"
        TurnAI(AI, GroupOfPlayer)
    else: #Otherwise gets the highest priority unit of the "Warrior" class
        count = 0
        for i in TableAI:
            A = i[0]
            count = 1
            if count == 1:
                break
        if (A.IsDef == False and (A.health - AI.damage + 55) < 0) or (A.IsDef == True and (A.health - AI.damage + 70)/2 < 0) or AI.energy < 25:
            AI.__attack__(A) #Attack if guaranteed to kill, or if there is not enough energy
        else:
            AI.__skill__(A) #Else - strong attack 
#
 
#           
def TurnAIWizard(AI, GroupOfPlayer): #This function is responsible for the behavior of the AI class "Wizard"
    if AI.energy >= 25: #If the wizard has mana - unleash a powerful spell on the heads of enemies
        AI.__skill__(GroupOfPlayer)
    else: #Else - base attack
        AI.__attack__(GroupOfPlayer)
#        

#        
def TurnAIHealer(AI, GroupOfAI): #This function is responsible for the behavior of the AI of the "HealingAll" class
    
    A = TableForHeal(GroupOfAI) #The AI gets a table with the ratio of the current health to the maximum
   
    if A.health == A.MaxHealth: #If the health reserve of the most wounded character is equal to the maximum reserve, then there is no one to treat - take up the defense
        AI.__defence__()
    elif A.health + AI.damage * 1.35 < A.MaxHealth: #If this character is "severely" injured, then use powerful healing
        AI.__skill__(GroupOfAI)
    else:
        AI.__attack__(GroupOfAI) #Otherwise, just treat the whole group
#

#
def TurnAISoloHealer(AI, GroupOfAI): #This function is responsible for the behavior of the AI of the "Healer" class
    
    A = TableForHeal(GroupOfAI) #The AI gets a table with the ratio of the current health to the maximum
   
   
    if A.health == A.MaxHealth: #If the health reserve of the most wounded character is equal to the maximum reserve, then there is no one to treat - take up the defense
        AI.__defence__()
    elif A.health + AI.damage * 1.5 < A.MaxHealth: #If this character is seriously injured, then use a powerful treatment
        AI.__skill__(A)
    else:
        AI.__attack__(A) #Otherwise, use normal healing
#        
