#This module contains the definition of game characters of the "Wizard" class
import Heroes
from  random import randint, random
from time import sleep

class Wizard(Heroes.AllHeroes):
    
#        
    def __attack__(self, Group): #Base attack
        self.IsDef = False
        self.__CheckTheStatusOfPriority__()
        for i in Group: #Wizards attack the entire enemy group
            if i.IsAlive == True:
                self.Hit = self.__MissOrHit__(i) 
                MissGenerator = random() - 0.1
                if MissGenerator <= self.Hit: 
                    RealDamage = self.__CalculateDamage__(i)
                    if i.IsDef : RealDamage/=2
                    if MissGenerator <= (self.Hit)/2 - (i.dodge)/100 - 0.15: #Wizards have a slightly low probability of making a critical hit
                        RealDamage*=1.5
                        print(" CRIT! %s deals %i damage" %(self.name, RealDamage))
                    else: print(" %s deals %i damage to the hero %s" %(self.name, RealDamage, i.name)) 
                    sleep(0.2)
                    if i.health - RealDamage >0: #The enemy survived
                        i.health -= int(RealDamage)
                        print(" The character %s has %i health points remaining" %(i.name, i.health)) 
                    else: #The enemy is dead
                        i.health = 0
                        print("\t%s deals a fatal blow - %s dies" %(self.name, i.name))
                        i.IsAlive = False
                    i.__CheckTheStatusOfPriority__()
                else: 
                    print(" %s misses!" %(self.name)) 
                    sleep(0.2)
                
#                
 
#   
    def __skill__(self, Group): #Powerful cast
        self.IsDef = False 
        self.__CheckTheStatusOfPriority__()
        self.energy -=25 #Change energy
        print(" %s uses a powerful spell"%(self.name))
        sleep(0.2)
        for i in Group: #For each
            if i.IsAlive == True:
                self.Hit = self.__MissOrHit__(i)
                MissGenerator = random() - 0.1
                if MissGenerator <= self.Hit: 
                    RealDamage = self.__CalculateDamage__(i) + randint(35, 70) #The damage spread is smaller than that of warriors and archers
                    if i.IsDef : RealDamage/=2
                    if MissGenerator <= (self.Hit)/2 - (i.dodge)/100 - 0.15: #The probability of a critical hit is also slightly underestimated
                        RealDamage*=1.5
                        print(" CRIT! %s deals %i damage" %(self.name, RealDamage))
                    else: print(" %s deals %i damage to the hero %s" %(self.name, RealDamage, i.name))
                    sleep(0.2)
                    if i.health - RealDamage >0: #The enemy survived
                        i.health -= int(RealDamage)
                        print(" The character %s has %i health points remaining" %(i.name, i.health))
                    else: #The enemy is dead
                        i.health = 0
                        print("\t%s deals a fatal blow - %s dies" %(self.name, i.name))
                        i.IsAlive = False
                    i.__CheckTheStatusOfPriority__()
                else: 
                    print(" %s misses!" %(self.name)) 
                sleep(0.2)
                
                    