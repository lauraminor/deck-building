"""
Last updated: 1.30.2016
"""

from objectclasses import *

#
# Template for Card object initialization:
# (name=string,type=string,power=int,draw=int,victorypoint=int,cost=int,defense=bool,attack=false,other=False)
#
# Upon initialization,
# card.owner = None

###################################################################################################
################################### STANDING STACK CARDS ##########################################
###################################################################################################

weakness = Card("Weakness",None,0,0,-1,0)
kick = Card("Kick","SuperPower",2,0,1,3)
vulnerability = Card("Vulnerability","Starter",0,0,0,0)
punch = Card("Punch","Starter",1,0,0,0)
supervillain = Card("BigBad","SuperVillain",3,0,5,10)

###################################################################################################
################################### SUPERVILLAIN CARDS ############################################
###################################################################################################

"""

    Specific Supervillain cards will eventually replace
    the pro tem 'supervillain' type I've defined above.

"""

###################################################################################################
####################################### MAIN DECK CARDS ###########################################
###################################################################################################


#### SIMPLE CARDS ####
catwoman = Card("Catwoman","Hero",2,0,1,2)
gorilla = Card("Gorilla Grodd","Villain",3,0,2,5)
kidflash = Card("Kid Flash","Hero",0,1,1,2)
superstrength = Card("Super Strength","SuperPower",5,0,2,7,)
doomsday = Card("Doomsday","Villain",4,0,2,6)
fastestman = Card("The Fastest Man Alive","Hero",0,2,1,5)

#### DEFENSE CARDS ####

lasso = Card("Lasso of Truth","Equipment",1,0,1,2,True)
speed = Card("Super Speed","SuperPower",0,1,1,3,True)
beetle = Card("Blue Beetle","Hero",3,0,2,6,True)
bulletproof = Card("Bulletproof","SuperPower",2,0,1,4,True)
cowl = Card("The Cape and Cowl","Equipment",2,0,1,4,True)
#### ATTACK CARDS ####
bane = Card("Bane","Villain",2,0,1,4,False,True)
poisonivy = Card("Poison Ivy","Villain",1,0,1,3,False,True)
starro = Card("Starro","Villain",0,0,2,7,False,True)
scarecrow = Card("Scarecrow","Villain",2,0,1,5,False,True)
harley = Card("Harley Quinn","Villain",1,0,1,2,False,True)

#### CONDITIONAL BONUS POWER CARDS ####

powerring = Card("Power Ring","Equipment",2,0,1,3,False,False,True)
swamp = Card("Swamp Thing","Hero",2,0,1,4,False,False,True)
hightech = Card("High-Tech Hero","Hero",1,0,1,3,False,False,True)
mera = Card("Mera","Hero",2,0,1,3,False,False,True)

#### DISCARD PILE FETCH CARDS ####

signal = Card("The Bat Signal","Equipment",1,0,1,5,False,False,True)
robin = Card("Robin","Hero",1,0,1,3)
manofsteel = Card("Man of Steel","Hero",3,0,3,8,False,False,True)
zatanna = Card("Zatanna Zatara","Hero",1,0,1,4,False,False,True)

#### SPECIAL VICTORY POINT CARDS ####

suicide = Card("Suicide Squad","Villain",2,0,None,4,False,False,True)
belt = Card("Utility Belt","Equipment",2,0,None,5,False,False,True)
arrow = Card("Green Arrow","Hero",2,0,None,5,False,False,True)
bizarro = Card("Bizarro","Villain",3,0,None,7,False,False,True)

#### DESTROY CARDS ####
heatvision = Card("Heat Vision","SuperPower",3,0,2,6,False,False,True)
nthmetal = Card("Nth Metal","Equipment",1,0,1,3,False,False,True)
lobo = Card("Lobo","Villain",3,0,2,7,False,False,True)
atlantis = Card("King of Atlantis","Hero",1,0,1,5,False,False,True)

#### CARDS THAT PLAY OTHER CARDS ####

emerald = Card("Emerald Knight","Hero",0,0,1,5,False,False,True)
jonzz = Card("J'onn J'onzz","Hero",0,0,2,6,False,False,True)
xray = Card("X-Ray Vision","SuperPower",0,0,1,3,False,False,True)
clayface = Card("Clayface","Villain",0,0,1,4,False,False,True)

#### GAIN CARDS ####

cheetah = Card("Cheetah","Villain",0,0,1,2,False,False,True)
supergirl = Card("Supergirl","Hero",0,0,1,4,False,False,True)
diana = Card("Princess Diana of Themyscira","Hero",0,0,2,7,False,False,True)
darkknight = Card("Dark Knight","Hero",2,0,1,5,False,False,True)

#### OTHER CARDS ####
riddler = Card("The Riddler","Villain",0,0,1,3,False,False,True)
bow = Card("Green Arrow's Bow","Equipment",2,0,1,4,False,False,True)
trident = Card("Aquaman's Trident","Equipment",2,0,1,3,False,False,True)
grundy = Card("Solomon Grundy","Villain",3,0,2,6,False,False,True)
twoface = Card("Two-Face","Villain",1,0,1,2,False,False,True)
penguin = Card("Penguin","Villain",0,0,1,3,False,False,True)
batmobile = Card("Batmobile","Villain",1,0,1,2,False,False,True)

#### LOCATION CARDS ####

batcave = Card("The Batcave","Location",0,0,1,5,False,False,True)
titans = Card("Titans Tower","Location",0,0,1,5,False,False,True)
watchtower = Card("The Watchtower","Location",0,0,1,5,False,False,True)
arkham = Card("Arkham Asylum","Location",0,0,1,5,False,False,True)
fortress = Card("Fortress of Solitude","Location",0,0,1,5,False,False,True)

###################################################################################################
####################################### DECK & STACK CREATION #####################################
###################################################################################################

for i in range(20):
    weakness = Card("Weakness",None,0,0,-1,0)

for i in range(16):
    kick = Card("Kick","SuperPower",2,0,1,3)

for i in range(16):
    vulnerability = Card("Vulnerability","Starter",0,0,0,0)

for i in range(36):
    punch = Card("Punch","Starter",1,0,0,0)

for i in range(12):
    supervillain = Card("BigBad","SuperVillain",3,0,5,10)

def create_maindeck():    
    allcards = []
    for i in range(6):
        suicide = Card("Suicide Squad","Villain",2,0,None,4,False,False,True)

    for i in range(4):
        kidflash = Card("Kid Flash","Hero",0,1,1,2)
        speed = Card("Super Speed","SuperPower",0,1,1,3,True)
        nthmetal = Card("Nth Metal","Equipment",1,0,1,3,False,False,True)

    for i in range(3):
        catwoman = Card("Catwoman","Hero",2,0,1,2)
        superstrength = Card("Super Strength","SuperPower",5,0,2,7,)
        lasso = Card("Lasso of Truth","Equipment",1,0,1,2,True)
        bulletproof = Card("Bulletproof","SuperPower",2,0,1,4,True)
        cowl = Card("The Cape and Cowl","Equipment",2,0,1,4,True)
        powerring = Card("Power Ring","Equipment",2,0,1,3,False,False,True)
        signal = Card("The Bat Signal","Equipment",1,0,1,5,False,False,True)
        robin = Card("Robin","Hero",1,0,1,3)
        belt = Card("Utility Belt","Equipment",2,0,None,5,False,False,True)
        arrow = Card("Green Arrow","Hero",2,0,None,5,False,False,True)
        heatvision = Card("Heat Vision","SuperPower",3,0,2,6,False,False,True)
        bow = Card("Green Arrow's Bow","Equipment",2,0,1,4,False,False,True)
        trident = Card("Aquaman's Trident","Equipment",2,0,1,3,False,False,True)
        scarecrow = Card("Scarecrow","Villain",2,0,1,5,False,True)

    for i in range(2):
        poisonivy = Card("Poison Ivy","Villain",1,0,1,3,False,True)
        gorilla = Card("Gorilla Grodd","Villain",3,0,2,5)
        doomsday = Card("Doomsday","Villain",4,0,2,6)
        bane = Card("Bane","Villain",2,0,1,4,False,True)
        harley = Card("Harley Quinn","Villain",1,0,1,2,False,True)
        swamp = Card("Swamp Thing","Hero",2,0,1,4,False,False,True)
        hightech = Card("High-Tech Hero","Hero",1,0,1,3,False,False,True)
        mera = Card("Mera","Hero",2,0,1,3,False,False,True)
        xray = Card("X-Ray Vision","SuperPower",0,0,1,3,False,False,True)
        clayface = Card("Clayface","Villain",0,0,1,4,False,False,True)
        cheetah = Card("Cheetah","Villain",0,0,1,2,False,False,True)
        supergirl = Card("Supergirl","Hero",0,0,1,4,False,False,True)
        grundy = Card("Solomon Grundy","Villain",3,0,2,6,False,False,True)
        twoface = Card("Two-Face","Villain",1,0,1,2,False,False,True)
        penguin = Card("Penguin","Villain",0,0,1,3,False,False,True)
        batmobile = Card("Batmobile","Villain",1,0,1,2,False,False,True)
        riddler = Card("The Riddler","Villain",0,0,1,3,False,False,True)
        zatanna = Card("Zatanna Zatara","Hero",1,0,1,4,False,False,True)

    for i in range(1):
        fastestman = Card("The Fastest Man Alive","Hero",0,2,1,5)
        beetle = Card("Blue Beetle","Hero",3,0,2,6,True)    
        starro = Card("Starro","Villain",0,0,2,7,False,True)    
        manofsteel = Card("Man of Steel","Hero",3,0,3,8,False,False,True)
        lobo = Card("Lobo","Villain",3,0,2,7,False,False,True)
        atlantis = Card("King of Atlantis","Hero",1,0,1,5,False,False,True)
        emerald = Card("Emerald Knight","Hero",0,0,1,5,False,False,True)
        jonzz = Card("J'onn J'onzz","Hero",0,0,2,6,False,False,True)
        bizarro = Card("Bizarro","Villain",3,0,None,7,False,False,True)
        diana = Card("Princess Diana of Themyscira","Hero",0,0,2,7,False,False,True)
        darkknight = Card("Dark Knight","Hero",2,0,1,5,False,False,True)
        batcave = Card("The Batcave","Location",0,0,1,5,False,False,True)
        titans = Card("Titans Tower","Location",0,0,1,5,False,False,True)
        watchtower = Card("The Watchtower","Location",0,0,1,5,False,False,True)
        arkham = Card("Arkham Asylum","Location",0,0,1,5,False,False,True)
        fortress = Card("Fortress of Solitude","Location",0,0,1,5,False,False,True)
        

