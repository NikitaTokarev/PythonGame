#This module contains the definition of the game characters of the class "Warrior" and " Bowman"
import Heroes
from  random import randint, random
from time import sleep


class Warrior(Heroes.AllHeroes):
    
        
    #        
    def __attack__(self, Enemy): #Basic strike method
        self.IsDef = False #It is necessary to remove the protection in case the character took the defense on the previous turn
        self.__CheckTheStatusOfPriority__()
        self.Hit = self.__MissOrHit__(Enemy) #Calculate the probability of a hit
        MissGenerator = random() - 0.1 #Generating a pseudo-random number
        if MissGenerator <= self.Hit: #If the generated number is less than / equal to the one calculated by the formula - hit
            RealDamage = self.__CalculateDamage__(Enemy) #Calculate the damage
            if Enemy.IsDef : RealDamage/=2 #If the enemy is on the defensive - divide the damage by 2
            
            if MissGenerator <= (self.Hit)/2 - (Enemy.dodge)/100 - 0.05: #Critical impact calculation formula
                RealDamage*=1.5 #On a critical hit, the damage increases by 50%
                print(" CRIT! %s deals %i damage" %(self.name, RealDamage))
            else: print(" %s deals %i damage to the hero %s" %(self.name, RealDamage, Enemy.name)) #Else - not critical
            
            sleep(0.35)
            if Enemy.health - RealDamage >0: #If the opponent has survived - display a message about the remaining health
                Enemy.health -= int(RealDamage)
                print(" The character %s has %i health points remaining" %(Enemy.name, Enemy.health))
            else: #If the enemy is dead - print a message and change the value of the IsAlive variable
                Enemy.health = 0
                print("\t%s deals a fatal blow - %s dies" %(self.name, Enemy.name))
                Enemy.IsAlive = False
        else: 
            print(" %s misses!" %(self.name)) #If the generated number is greater than the calculated one, it is a miss
            sleep(0.35)
        Enemy.__CheckTheStatusOfPriority__()
#


#       
    def __skill__(self, Enemy): #A class method that allows a character to use an energy-consuming skill
        self.IsDef = False #The character is not in a defensive stance
        self.__CheckTheStatusOfPriority__()
        self.energy -=25 #We reduce the energy reserve (the check is carried out outside, so as not to call this function without energy)
        print(" %s deals a powerful blow"%(self.name))
        sleep(0.35)
        
        self.Hit = self.__MissOrHit__(Enemy)
        MissGenerator = random() - 0.1
        if MissGenerator <= self.Hit: #The calculation is made in the same way
            RealDamage = self.__CalculateDamage__(Enemy) + randint(75, 150) #More spread + additional damage does not take into account the opponent's "Armor" value
            if Enemy.IsDef : RealDamage/=2 #Но учитывает защитную стойку
            if MissGenerator <= (self.Hit)/2 - (Enemy.dodge) /100 - 0.05: #Calculation of the crit with a small correction
                RealDamage*=1.5
                print(" CRIT! %s deals %i damage" %(self.name, RealDamage))
            else: print(" %s deals %i damage to the hero %s" %(self.name, RealDamage, Enemy.name))
            sleep(0.35)
            if Enemy.health - RealDamage >0: #If the opponent has survived - display a message about the remaining health
                Enemy.health -= int(RealDamage)
                print(" The character %s has %i health points remaining" %(Enemy.name, Enemy.health))
            else: #If the enemy is dead - print a message and change the value of the IsAlive variable
                Enemy.health = 0
                print("\t%s deals a fatal blow - %s dies" %(self.name, Enemy.name))
                Enemy.IsAlive = False
        else: 
            print(" %s misses!" %(self.name)) #If the generated number is greater than the calculated one, it is a miss
        sleep(0.35)
        Enemy.__CheckTheStatusOfPriority__()

#
    
    
    