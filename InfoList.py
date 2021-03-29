#This module contains all the information about the mechanics of this game, as well as information about all the available game characters

from PlayingHeroes import TotalWarrior, LastBowman, LastWizard_Single, LastWizard_Splash, LastHealer, LastHealingAll

def Manual(): #Manual
    print(" Greetings, adventurer. Would you like to get acquainted with the mechanics of this game? (If you wish, enter 'yes')")
    Choise = input()
    Choise = Choise.lower()
    if Choise == "да" or Choise == "yes":
        print("\tThis project is based on the legendary game Disciples 2. From this game, he inherited a lot, including the combat system.\n\
        The battle involves two squads of five units each. One is controlled by the player, the other by the AI.\n\
        In battle, the warriors stand in two rows. In the front row are melee fighters, they can not attack enemy warriors from the second row,\n\
        if someone is in the first row of the enemy squad. Bowmans do not have such restrictions and are free to attack any enemy warrior.\n\
        There are also mages, many of whom attack the area, hitting the entire opponent's squad at a time.\n\
        Mages attacking single targets have the mechanics of shooters.\n\
        Healers play a special role in combat. There are two types of clerics: healing single targets and healing the entire squad.\n\
        They are easily distinguished by the amount of health restored.\n\
        As with the original Disciples, each unit has a 'Accuracy' score (with the exception of Healers). \n\
        This indicator, together with the 'Dodge' indicator, is responsible for generating a miss, and also affects the probability of a critical hit.\n\
        The damage dealt is also affected by the 'Armor' indicator. The higher it is, the less damage it takes.\n\
        Another way to reduce the damage received is to go on the defensive. Characters who take a defensive position will receive 50% less damage.\n\
        The damage itself is of two types (in addition to critical) - damage from a normal attack and damage from a skill that consumes a resource.\n\
        The damage from the skill has a small 'penetrating effect', which allows you to ignore the enemy's' Armor ' to a certain extent.\n\
        'Energy' is a resource required for the use of combat skills. Each such skill requires 25 units of energy.\n\
        In battle, the warriors move according to the 'Initiative' indicator. However, each turn generates a 'Scale of Initiative', as a result of which each unit\n\
        receives an increase to the 'Initiative' indicator in the range from 0 to 10. Thus, a slightly less initiative character can overtake a more initiative one.\n\n\
        \tCONTROL OF THE GAME\n\
        The game has quite simple controls. Each character can attack / heal, use a skill, go on the defensive, or delay a move.\n\
        Each character has its own unique 'sequence number'. This number is necessary for easier command entry, since the PLAYER'S WARRIORS ATTACKING \n\
        SINGLE TARGETS need to specify who to attack. You can find out the number by typing the command 'STAT'.\n\
        'STAT' - show battle summaries\n\
        'SCALE'- display the initiative scale\n\
        'ATK'  - attack. For warriors attacking a single target, you must specify the 'serial number' of the enemy SEPARATED by a SPACE\n\
        'SKL'  - use the skill (requires 25 units of energy). For heroes attacking a single target, a SPACE-separated value must be specified\n\
        'the opponent's serial number\n\
        'DEF'  - go on the defensive. Reduces damage received by 50%\n\
        'WAIT' - delay the move. The character passes at the end of the round, but the units will go in the opposite order of waiting\n\
        'HEAL' - a command for the healer. For a healer who heals a single target, you must specify the number of your warrior SEPARATED by a SPACE\n\
        'RETRY'- restart the game\n\
        \nThis is the end of the guide. Good luck to you, hero!\n")
        Skip = input("To continue, press any key ")
        print(Skip, " ")
    else:
        print(Choise, " ")
        return

def CharacterInformation(GamingCharacters): #This feature displays all available game characters and their characteristics
    print("\t\t\tWARRIORS\n")
    for i in GamingCharacters:
        if i.Number == TotalWarrior + 1: print("\n\t\t\tBOWMANS\n")
        if i.Number == LastBowman: print("\n\t\t\tWIZARDS (SINGLE)\n")
        if i.Number == LastWizard_Single: print("\n\t\t\tWIZARDS (SPLASH)\n")
        if i.Number == LastWizard_Splash: print("\n\t\t\tHEALER (SINGLE)\n")
        if i.Number == LastHealingAll: print("\n\t\t\tHEALER (SPLASH)\n")
        print(" %i %s   Health %i  Damage %i  Iniziative %i  Accuracy %i  Dodge %i  Armor %i  Energy %i\n"%(i.Number, i.name, i.health, i.damage, i.iniziative, i.accuracy, i.dodge, i.armor, i.energy))
    print("\n\n")