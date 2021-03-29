#This module contains the definition of game characters of the "Healer" class

import Heroes
from time import sleep

class Healer(Heroes.AllHeroes):
    
        
    def __attack__(self, hero): #Base heal
        self.IsDef = False
        self.__CheckTheStatusOfPriority__()
        RestoreHealth = hero.health
        hero.health = hero.health + self.damage if (hero.health + self.damage) <= hero.MaxHealth else hero.MaxHealth #Single healing
        RestoreHealth = hero.health - RestoreHealth #Calculate how much health has been restored
        print(" %s heals %i health points to hero %s" %(self.name, RestoreHealth, hero.name))
        hero.__CheckTheStatusOfPriority__()
        sleep(0.35)       
    
    def __skill__(self, hero): #Powerful heal
        self.IsDef = False
        self.__CheckTheStatusOfPriority__()
        self.energy -=25 #Расходует ресурс
        print(" %s use powerful healing"%(self.name))
        sleep(0.35)
        RestoreHealth = hero.health
        hero.health = hero.health + int(self.damage * 1.5) if (hero.health + self.damage * 1.5) <= hero.MaxHealth else hero.MaxHealth #Powerful healing
        RestoreHealth = hero.health - RestoreHealth #Calculate how much health has been restored
        print(" %s heals %i health points to hero %s" %(self.name, RestoreHealth, hero.name))
        hero.__CheckTheStatusOfPriority__()
        sleep(0.35)