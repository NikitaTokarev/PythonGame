#This module contains the base class definition for all other game classes

#Importing the necessary functions
from  random import randint, random


class AllHeroes(object):
    IsDef = False  #Indicates whether the character has taken a defensive position
    IsAlive = True #If the character is alive - he participates in the game
    IsHuman = False #False - AI unit, true - player unit
    MaxHealth = 0   #The maximum amount of health required for the implementation of the treatment mechanics, as well as for the" resurrection " of the character in subsequent games
    MaxEnergy = 0   #Maximum energy reserve required when replenishing energy when "resurrecting" after a battle
    Hit = 0.0 #The variable is involved in calculating the miss-hit generation and critical strike
    UsualPriority = 0 #Will contain the default priority of the unit, as it may change
#
    def __init__(self, name, health, damage, accuracy, energy, iniziative, armor, dodge, priority, Class, Number): #Class Constructor
    #Initialize the attributes
        self.name = name
        self.health = health
        self.MaxHealth = self.health 
        self.damage = damage
        self.accuracy = accuracy
        self.energy = energy
        self.MaxEnergy = self.energy 
        self.iniziative = iniziative
        self.armor = armor
        self.dodge = dodge
        self.priority = priority
        self.UsualPriority = self.priority 
        self.Class = Class
        self.Number = Number #The number is needed to facilitate player input
#

#
    def __MissOrHit__(self, Enemy): #This function generates a miss-hit + critical hit, taking into account the "Accuracy" of the hero and the "Dodge" of the enemy
        return self.accuracy/100*(1.0-(Enemy.dodge/100)) 
#        


#        
    def __CalculateDamage__(self, Enemy): #This function calculates the damage done, taking into account the hero's damage, the enemy's "Armor" and a small spread
        return (self.damage + randint(0, 30))*(1-(Enemy.armor/100))
#        

#
    def __CheckTheStatusOfPriority__(Hero):
        if Hero.health < int(Hero.MaxHealth/3): #If the opponent's health reserve is below a third, the priority is doubled
            Hero.priority*=2
        else:
            Hero.priority = Hero.UsualPriority #With sufficient treatment, priority returns to the default level
        
#            

#
    def __defence__(self): #Class method that allows the character to go on the defensive
        self.priority-=10
        print(" %s takes a defensive position" %(self.name))
        self.IsDef = True 
#
    
#
    def __wait__(self, Wait_List): #Class method that allows the character to delay the turn until the end of the round
        self.__CheckTheStatusOfPriority__()
        print(" %s waiting for the right moment" %(self.name))
        Wait_List.append(self) #It is necessary to write down the" Waiting " character in the list
        self.IsDef = False
#

#
        #The following two methods are simply defined in the base class, but they are implemented in inherited classes
    def __attack__(self, Enemy):
        self.IsDef = False
        Enemy.health -=self.damage
        if Enemy.health <=0:
            Enemy.IsAlive = False
#
    def __skill__(self, Enemy):
        self.IsDef = False
        Enemy.health -=self.damage + randint(30, 75)
        if Enemy.health <=0:
            Enemy.IsAlive = False
#        
        
        
        
        
        
