#This module contains all the game characters
#To create characters, you need to connect modules that contain the class definitions of these characters
import ClassWarrior
import ClassWizard
import ClassHealingAll
import ClassHealer

NumberCount = 1 # Responsible for automated counting of the number of characters

TotalWarrior = 0 #At least one "Warrior" class character must be present in the AI group
LastBowman = 0
LastWizard_Single = 0
LastWizard_Splash = 0
LastHealer = 0
LastHealingAll = 0
#The first character is not a game character, it is necessary to create random groups
Nothing    =     ClassWarrior.Warrior              ("NONE",            1000,    1000,     99.0,     500,      250,        90.0,   90.0,       1,      "Warrior",      0)

                                                    #Name                Health    Damage    Accuracy Energy Initiative    Armor  Dodge  Priority       Class      Number

#Warriors

Paladin    =      ClassWarrior.Warrior              ("Paladin",            925,    255,     75.0,     75,      50,        30.0,   10.0,       40,       "Warrior",     NumberCount)
NumberCount +=1 

Crusader   =      ClassWarrior.Warrior              ("Crusader",           950,    245,     75.0,     100,     45,        35.0,   10.0,       35,       "Warrior",     NumberCount)
NumberCount +=1 

Zealot     =      ClassWarrior.Warrior              ("Zealot",             875,    270,     80.0,     75,      55,        25.0,   15.0,       45,       "Warrior",     NumberCount)
NumberCount +=1 

Inquisitor =      ClassWarrior.Warrior              ("Inquisitor",         900,    260,     75.0,     125,     55,        20.0,   20.0,       46,       "Warrior",     NumberCount)
NumberCount +=1 

Knight     =      ClassWarrior.Warrior              ("Knight",             950,    240,     80.0,     50,      40,        35.0,   5.0,        35,       "Warrior",     NumberCount)
NumberCount +=1 

ForestWarrior  =  ClassWarrior.Warrior              ("Forest Warrior",     850,    255,     88.0,     100,     60,        10.0,   25.0,       50,       "Warrior",     NumberCount)
NumberCount +=1 

DefenderOfTheGrov=ClassWarrior.Warrior              ("Grove defender",     920,    245,     80.0,     75,      52,        25.0,   12.0,       40,       "Warrior",     NumberCount)
NumberCount +=1 

MasterOfTheBlade =ClassWarrior.Warrior              ("Master of the blade",875,    250,     90.0,     100,     60,        15.0,   20.0,       51,       "Warrior",     NumberCount)
NumberCount +=1 

DefenderOfTheMoun=ClassWarrior.Warrior              ("Mountain defender",  1000,   215,     70.0,     75,      30,        50.0,   1.0,        20,       "Warrior",     NumberCount)
NumberCount +=1 

DwarfWarrior  =   ClassWarrior.Warrior              ("Dwarf Warrior",      950,    235,     80.0,     75,      35,        35.0,   5.0,        32,       "Warrior",     NumberCount)
NumberCount +=1 

DwarfGuardsman  = ClassWarrior.Warrior              ("Dwarf Guardsman",    975,    230,     75.0,     100,     35,        35.0,   7.0,        32,       "Warrior",     NumberCount)
NumberCount +=1 

OrcishFighter  =  ClassWarrior.Warrior              ("Orcish Fighter",     775,    280,     80.0,     75,      47,        5.0,    15.0,       47,       "Warrior",     NumberCount)
NumberCount +=1 

Barbarian  =      ClassWarrior.Warrior              ("Barbarian",          750,    290,     75.0,     100,     50,        1.0,    10.0,       51,       "Warrior",     NumberCount)
NumberCount +=1 

Gladiator =       ClassWarrior.Warrior              ("Gladiator",          850,    270,     85.0,     100,     50,        10.0,   25.0,       45,       "Warrior",     NumberCount)
NumberCount +=1 

Bandit    =       ClassWarrior.Warrior              ("Bandit",             800,    265,     90.0,     100,     60,        1.0,    20.0,       50,       "Warrior",     NumberCount)
NumberCount +=1 

Assassin =        ClassWarrior.Warrior              ("Assassin",           715,    305,     99.0,     100,     75,        1.0,    40.0,       70,       "Warrior",     NumberCount)
NumberCount +=1 

TotalWarrior = NumberCount - 1 #Upper limit of the warrior range

#Bowmans
#Bowmans have the same class that warriors, but other "game class"
ImperialArcher =  ClassWarrior.Warrior              ("Imperial Archer",    425,    205,     85.0,      50,     75,        5.0,    20.0,       80,       "Bowman",      NumberCount)
NumberCount +=1 

Crossbowman    =  ClassWarrior.Warrior              ("Crossbowman",        475,    220,     85.0,      25,     65,        5.0,    10.0,       75,       "Bowman",      NumberCount)
NumberCount +=1 

Bowman         =  ClassWarrior.Warrior              ("Bowman",             450,    210,     80.0,     25,      70,        1.0,    15.0,       77,       "Bowman",      NumberCount)
NumberCount +=1 

Sniper         =  ClassWarrior.Warrior              ("Sniper",             400,    230,      93.0,    25,      80,        1.0,    10.0,       82,       "Bowman",     NumberCount)
NumberCount +=1 

Sentinel       =  ClassWarrior.Warrior              ("Sentinel",           400,    220,      95.0,    25,      83,        1.0,    11.0,       82,       "Bowman",     NumberCount)
NumberCount +=1 

ElvenShooter   =  ClassWarrior.Warrior              ("Elven Shooter",      380,    220,      97.0,    50,      85,        1.0,    15.0,       85,       "Bowman",     NumberCount)
NumberCount +=1 

ForestAvenger  =  ClassWarrior.Warrior              ("Forest Avenger",     405,    215,      98.5,    50,      86,        1.0,    15.0,       85,       "Bowman",     NumberCount)
NumberCount +=1 

MasterOfTheBow =  ClassWarrior.Warrior              ("Master of the bow",  400,    220,      99.0,    50,      90,        1.0,    20.0,       90,       "Bowman",     NumberCount)
NumberCount +=1

DwarfCrossbowman = ClassWarrior.Warrior             ("Dwarf crossbowman",  500,    205,      80.0,    25,      63,        10.0,    8.0,       73,       "Bowman",     NumberCount)
NumberCount +=1 

FireThrower      = ClassWarrior.Warrior             ("Fire thrower",       490,    210,      78.0,    50,      63,        10.0,    7.0,       74,       "Bowman",     NumberCount)
NumberCount +=1

LastBowman = NumberCount

#Wizards attacking a single target are actually Bowmans
DarkWizard       = ClassWarrior.Warrior             ("Dark wizard",        420,    225,      75.0,    100,     70,        1.0,     5.0,       81,       "Bowman",     NumberCount)
NumberCount +=1

Adept            = ClassWarrior.Warrior             ("Adept",              430,    220,      75.0,    100,     70,        1.0,     5.0,       81,       "Bowman",     NumberCount)
NumberCount +=1

Warlock          = ClassWarrior.Warrior             ("Warlock",            390,    230,      80.0,    75,      72,        1.0,     8.0,       86,       "Bowman",     NumberCount)
NumberCount +=1

Pyromancer       = ClassWarrior.Warrior             ("Pyromancer",         400,    225,      82.0,    75,      70,        1.0,     7.0,       85,       "Bowman",     NumberCount)
NumberCount +=1 

LastWizard_Single = NumberCount

#Wizards

WhiteMagician    = ClassWizard.Wizard               ("White magician",     420,    125,      80.0,    100,     68,        1.0,     5.0,       70,       "Wizard",     NumberCount)
NumberCount +=1

Elementalist     = ClassWizard.Wizard               ("Elementalist",       405,    130,      75.0,    100,     63,        1.0,     6.0,       71,       "Wizard",     NumberCount)
NumberCount +=1

Wizard           = ClassWizard.Wizard               ("Wizard",             395,    125,      75.0,    125,     65,        1.0,     5.0,       71,       "Wizard",     NumberCount)
NumberCount +=1

BattleMage       = ClassWizard.Wizard               ("Battle mage",        380,    135,      77.0,    75,      68,        10.0,    10.0,      74,       "Wizard",     NumberCount)
NumberCount +=1

Druid            = ClassWizard.Wizard               ("Druid",              370,    130,      78.0,    100,     70,        1.0,     17.0,      74,       "Wizard",     NumberCount)
NumberCount +=1

Archon           = ClassWizard.Wizard               ("Archon",             390,    115,      83.0,    125,     70,        1.0,     20.0,      75,       "Wizard",     NumberCount)
NumberCount +=1

KeeperOfTheFlame = ClassWizard.Wizard               ("Keeper of the flame",445,    125,      73.0,     75,     62,        15.0,    5.0,       70,       "Wizard",     NumberCount)
NumberCount +=1 

RuneMaster       = ClassWizard.Wizard               ("Rune master",        420,    130,      70.0,    100,     64,        15.0,    5.0,       73,       "Wizard",     NumberCount)
NumberCount +=1

LordOfTheStorms  = ClassWizard.Wizard               ("Lord of the storms", 425,    130,      73.0,    100,     63,        10.0,    5.0,       73,       "Wizard",     NumberCount)
NumberCount +=1

Necromancer      = ClassWizard.Wizard               ("Necromancer",        385,    135,      80.0,    125,     70,        5.0,     10.0,      70,       "Wizard",     NumberCount)
NumberCount +=1

Demonologist     = ClassWizard.Wizard               ("Demonologist",       370,    140,      76.0,    75,      68,        5.0,     10.0,      70,       "Wizard",     NumberCount)
NumberCount +=1 

Shaman           = ClassWizard.Wizard               ("Shaman",             380,    135,      85.0,    100,     65,        5.0,     15.0,      75,       "Wizard",     NumberCount)
NumberCount +=1

Reaper           = ClassWizard.Wizard               ("Reaper",             430,    150,      85.0,    50,      73,        5.0,     18.0,      77,       "Wizard",     NumberCount)
NumberCount +=1

Archilich        = ClassWizard.Wizard               ("Archilich",          400,    135,      80.0,    100,     70,        5.0,     10.0,      76,       "Wizard",     NumberCount)
NumberCount +=1 

LastWizard_Splash = NumberCount

#Healers (group)

PriestessOfLight = ClassHealingAll.HealingAll       ("Priestess of light", 490,    110,      100.0,   100,     15,         5.0,    10.0,      60,       "HealingAll",  NumberCount)
NumberCount +=1

Abbess           = ClassHealingAll.HealingAll       ("Abbess",             450,    120,      100.0,    75,      17,        15.0,    10.0,     60,       "HealingAll",  NumberCount)
NumberCount +=1 

MaidenOfSun     = ClassHealingAll.HealingAll        ("Maiden of sun",      470,    100,      100.0,    150,     20,         5.0,    30.0,     60,       "HealingAll",  NumberCount)
NumberCount +=1 

MaidenOfIce      = ClassHealingAll.HealingAll       ("Maiden Of ice",      460,    115,      100.0,    100,     18,         10.0,    25.0,    60,       "HealingAll",  NumberCount)
NumberCount +=1

Herbalist        = ClassHealingAll.HealingAll       ("Herbalist",          520,    115,      100.0,    75,      13,         10.0,     5.0,    60,       "HealingAll",  NumberCount)
NumberCount +=1 

Alchemist        = ClassHealingAll.HealingAll       ("Alchemist",          505,    145,      100.0,    25,      14,         25.0,     5.0,    60,       "HealingAll",  NumberCount)
NumberCount +=1 

LastHealingAll = NumberCount

#Healers (single)

Matriarch        = ClassHealer.Healer               ("Matriarch",          500,    200,      100.0,    75,      9,          10.0,     10.0,   65,       "Healer",      NumberCount)
NumberCount +=1

Preacher         = ClassHealer.Healer               ("Preacher",           450,    185,      100.0,    125,     8,          15.0,     5.0,    65,       "Healer",      NumberCount)
NumberCount +=1

Medium           = ClassHealer.Healer               ("Medium",             450,    190,      100.0,    100,     11,         5.0,      25.0,   65,       "Healer",      NumberCount)
NumberCount +=1

ForestMaiden    = ClassHealer.Healer                ("Forest maiden",      475,    210,      100.0,    50,      12,         20.0,     15.0,   65,       "Healer",      NumberCount)
NumberCount +=1

RuneHealer       = ClassHealer.Healer               ("Rune healer",        525,    195,      100.0,    75,      14,         30.0,     1.0,    65,       "Healer",      NumberCount)

LastHealer = NumberCount

#This table contains all created game characters
GamingCharacters = [
    Paladin, Crusader, Zealot, Inquisitor,Knight, ForestWarrior, DefenderOfTheGrov, MasterOfTheBlade, DefenderOfTheMoun,
                    DwarfWarrior, DwarfGuardsman, OrcishFighter, Barbarian, Gladiator, Bandit, Assassin,
                    ImperialArcher, Crossbowman, Bowman, Sniper,  Sentinel, ElvenShooter, ForestAvenger,
                    MasterOfTheBow, DwarfCrossbowman, FireThrower, DarkWizard, Adept, Warlock, Pyromancer,
                    WhiteMagician, Elementalist, Wizard, BattleMage, Druid, Archon, KeeperOfTheFlame,
                    RuneMaster, LordOfTheStorms, Necromancer, Demonologist, Shaman, Reaper, Archilich,
                    PriestessOfLight, Abbess, MaidenOfSun, MaidenOfIce, Herbalist, Alchemist,
                    Matriarch, Preacher, Medium, ForestMaiden, RuneHealer
                    ]
                    
TotalCharacters = len(GamingCharacters) #Necessary to determine the upper limit of random generation


