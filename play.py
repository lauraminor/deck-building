"""
Last edited: 1.30.2016
"""

#############################################################################################################

from objectclasses import *
from cards import *

#############################################################################################################
#
# Start a new game!
#
#
# Initialize the heroes that will be used in this game.
# Assign names to these heroes.
#
superman = Hero("Superman","SuperPower")
batman = Hero("Batman","Equipment")
flash = Hero("Flash")
nightwing = Hero("Nightwing","Equipment")
wonderwoman = Hero("Wonder Woman","Villain")
#
# Initialize the different players that will play this game.
# Assign a name and a hero to each player.
#
# *** THIS WILL EVENTUALLY BE PLAYER INPUT ***
#
#
p1 = Player("Player One",superman)
p2 = Player("Player Two",wonderwoman)
#
ps = [p1,p2]
#
# Initialize a new iteration of the game.
# Assign our list of players to this game.
#
print()
new_game = Game(ps)
#
# Determine the play order for the game.
#
print()
new_game.show_playorder()
print()
#
#
# Initialize three static stacks of kicks, weaknesses, and supervillains, respectively.
#
kicks = Stack("Kicks")
for i in range(16):
    kicks.add_to_top(kick)
weaknesses = Stack("Weaknesses")
for i in range(20):
    weaknesses.add_to_top(weakness)
supervillains = Stack("SuperVillains")
for i in range(12):
    supervillains.add_to_top(supervillain)
#
# Initialize the main deck.
#
# Add all the cards from the main deck stash
for i in range(6):
    new_game.maindeck.add_to_top(suicide)
for i in range(4):
    new_game.maindeck.add_to_top(kidflash)
    new_game.maindeck.add_to_top(speed)
    new_game.maindeck.add_to_top(nthmetal)
for i in range(3):
    new_game.maindeck.add_to_top(catwoman)
    new_game.maindeck.add_to_top(superstrength)
    new_game.maindeck.add_to_top(lasso)
    new_game.maindeck.add_to_top(bulletproof)
    new_game.maindeck.add_to_top(cowl)
    new_game.maindeck.add_to_top(powerring)
    new_game.maindeck.add_to_top(signal)
    new_game.maindeck.add_to_top(robin)
    new_game.maindeck.add_to_top(belt)
    new_game.maindeck.add_to_top(arrow)
    new_game.maindeck.add_to_top(heatvision)
    new_game.maindeck.add_to_top(bow)
    new_game.maindeck.add_to_top(trident)
    new_game.maindeck.add_to_top(scarecrow)
for i in range(2):
    new_game.maindeck.add_to_top(poisonivy)
    new_game.maindeck.add_to_top(gorilla)
    new_game.maindeck.add_to_top(doomsday)
    new_game.maindeck.add_to_top(bane)
    new_game.maindeck.add_to_top(harley)
    new_game.maindeck.add_to_top(swamp)
    new_game.maindeck.add_to_top(hightech)
    new_game.maindeck.add_to_top(mera)
    new_game.maindeck.add_to_top(xray)
    new_game.maindeck.add_to_top(clayface)
    new_game.maindeck.add_to_top(cheetah)
    new_game.maindeck.add_to_top(supergirl)
    new_game.maindeck.add_to_top(grundy)
    new_game.maindeck.add_to_top(twoface)
    new_game.maindeck.add_to_top(penguin)
    new_game.maindeck.add_to_top(batmobile)
    new_game.maindeck.add_to_top(riddler)
    new_game.maindeck.add_to_top(zatanna)
for i in range(1):
    new_game.maindeck.add_to_top(fastestman)
    new_game.maindeck.add_to_top(beetle)
    new_game.maindeck.add_to_top(starro)
    new_game.maindeck.add_to_top(manofsteel)
    new_game.maindeck.add_to_top(lobo)
    new_game.maindeck.add_to_top(atlantis)
    new_game.maindeck.add_to_top(emerald)
    new_game.maindeck.add_to_top(jonzz)
    new_game.maindeck.add_to_top(bizarro)
    new_game.maindeck.add_to_top(diana)
    new_game.maindeck.add_to_top(darkknight)
    new_game.maindeck.add_to_top(batcave)
    new_game.maindeck.add_to_top(titans)
    new_game.maindeck.add_to_top(watchtower)
    new_game.maindeck.add_to_top(arkham)
    new_game.maindeck.add_to_top(fortress)
#
# Once the main deck has enough cards, shuffle it.
new_game.maindeck.shuffle()
#
#
# Describe the starting stacks to the player.
# For each static stack, display cardtype and number of cards in the stack. (These stacks are face up.)
# For main deck, display only number of cards in the stack. (Main deck is face down.)
#
print()
print("Starting stacks:")
print()
print(kicks.name,": ",kicks.left,sep='')
print(weaknesses.name,": ",weaknesses.left,sep='')
print(supervillains.name,": ",supervillains.left,sep='')
print()
print(new_game.maindeck.name,": ",new_game.maindeck.left," cards.",sep='')
print()
#
#
print("Dealing starting decks...")
new_game.deal_starting_decks()
print()

#for player in new_game.play_order.sequence:
#    print(player.deck.owner.name)
print("Drawing starting hands...")
new_game.draw_starting_hands()
print()

#
# It's the first player's turn!
# Initialize a new turn based on the established play order.
#
this_turn = Turn(new_game.play_order.sequence[0],new_game.maindeck,[],kicks.stack)
#
# Until Supervillain stack is empty...
while supervillains != []:
    #
    # Preserve current lineup and kicks for next turn.
    newline = this_turn.lineup
    newkicks = this_turn.kicks
    # Set up next player's turn.
    next_player = this_turn.player.next
    # It's the next guy's turn now!
    this_turn = Turn(next_player,new_game.maindeck,newline,newkicks)


