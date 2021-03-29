#This module contains the definition of game characters of the "HealingAll" class

import Heroes
from time import sleep

class HealingAll(Heroes.AllHeroes):
    
        
    def __attack__(self, Group): #Base heah
        self.IsDef = False
        self.__CheckTheStatusOfPriority__()
        for i in Group: #Heals all the living characters in the group
            if i.IsAlive == True:
                RestoreHealth = i.health
                i.health = i.health + self.damage if (i.health + self.damage) <= i.MaxHealth else i.MaxHealth #The health reserve can not exceed the maximum
                RestoreHealth = i.health - RestoreHealth #Calculate how much health has been restored
                print(" %s heals %i health points to hero %s" %(self.name, RestoreHealth, i.name))
                i.__CheckTheStatusOfPriority__()
                sleep(0.2)
                
    
    def __skill__(self, Group): #Powerful heal
        self.IsDef = False 
        self.__CheckTheStatusOfPriority__()
        self.energy -=25 #Change energy
        print(" %s use powerful healing"%(self.name))
        sleep(0.2)
        for i in Group: #Heals all the living characters in the group
            if i.IsAlive == True:
                RestoreHealth = i.health
                i.health = i.health + (self.damage*1.5) if i.health + int(self.damage*1.5) <= i.MaxHealth else i.MaxHealth #The health reserve can not exceed the maximum
                RestoreHealth = i.health - RestoreHealth #Calculate how much health has been restored
                print(" %s heals %i health points to hero %s" %(self.name, RestoreHealth, i.name))
                i.__CheckTheStatusOfPriority__()
                sleep(0.2)