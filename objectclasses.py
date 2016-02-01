"""
Last updated: 1.30.2016
"""

###################################################################################################

from random import random
from random import randint

###################################################################################################

class Stack:

    def __init__(self,name,player=None):
        ###
        ### Every stack of cards is initialized with just a name
        ### and an (optional) owner. Cards will then have to be
        ### added to it using methods; it starts life empty.
        ###
        ######## Stack attributes ########
        self.name = name
        self.stack = []
        self.left = len(self.stack)
        self.top = None
        self.bottom = None
        self.owner = player

    ######## Stack Methods ########

    def add_to_top(self,card):
        #
        # This method puts the specified card on the top of the Stack.
        #
        # Change the card's "owner" attribute so that it now belongs to the owner of this stack/deck.
        #   (Note: will be "None" if stack has no owner- e.g., main deck, weaknesses stack, etc.)
        card.owner = self.owner
        # Updates the stack to include the specified card on TOP of the existing stack.
        self.stack = [card] + self.stack
        # Resets the stack's "left" attribute.
        self.left = len(self.stack)
        # Resets the stack's "top" attribute.
        self.top = self.stack[0]
        # Resets the stack's "bottom" attribute ONLY if the top and bottom card are the same
        #   (i.e., there is only one card in the stack).
        if self.left == 1:
            self.bottom = self.top

    def add_to_bottom(self,card):
        #
        # This method puts the specified card on the bottom of the Stack.
        #
        # Change the card's "owner" attribute so that it now belongs to the owner of this stack/deck.
        #   (Note: will be "None" if stack has no owner- e.g., main deck, weaknesses stack, etc.)
        card.owner = self.owner
        # Updates the stack to include the specified card on the BOTTOM of the existing stack.
        self.stack = self.stack + [card]
        # Resets the stack's "left" attribute.
        self.left = len(self.stack)
        # Resets the stack's "bottom" attribute.
        self.bottom = self.stack[self.left-1]
        # Resets the stack's "top" attribute ONLY if the top and bottom card are the same
        #   (i.e., there is only one card in the stack).
        if self.left == 1:
            self.top = self.bottom

    def remove_top_card(self):
        #
        # This method deletes the top-most card of the stack.
        # *** NOTE *** This method does NOT move that card to another location.
        #
###############################################################################
############ I'm actually not sure we need the following commented code
############ Since this method will only be used AFTER something has been
############ done with the top_card (i.e., it has been moved, read, etc.)
############ each situation will have to deal with the possibility of an
############ empty stack BEFORE this method is ever called. I may be wrong,
############ so I'm leaving it grayed out for now, but that's my hunch.
#########
 ######## If we are trying to remove the top card from an empty stack...
 #######if self.left == 0:
 #######    # ...and the stack is NOT part of a Player Deck...
 #######    if self.owner == None:
 #######        # Report that the stack is empty.
 #######        print("There are no more cards in this stack.")
 #######    # OR, if the specified stack is a Player's discard pile...
 #######    elif self.name == "My Discard Pile":
 #######        # Report that the pile is empty.
 #######        print("Discard pile is empty.")
 #######    # OTHERWISE, the stack must be a Player's drawdeck...
 #######    else:
 #######        # So it's time to shuffle their deck.
 #######        self.owner.deck.shuffle()
 ###############################################################################
        # Remove the top card from the stack.
        self.stack.remove(self.top)
        # Reset the stack's "left" attribute.
        self.left = len(self.stack)  
        # If there are any cards left in the stack, we want to reset the top card.
        # If there aren't, we want to leave the stack empty for now, and set top card to None.          
        if self.left > 0:
            self.top = self.stack[0]
        else:
            self.top = None
        # Reset the stack's bottom card ONLY if the top and bottom card are the same
        #   (i.e., there is only one card --or fewer-- in the stack)
        if self.left <= 1:
            self.bottom = self.top

    def remove_bottom_card(self):
        #
        # This method deletes the bottom-most card of the stack.
        # *** NOTE *** This method does NOT move that card to another location.
        #
##############################################################################
#############
############# Same note as above (in remove_top_card).
#############
#############
######### If we are trying to remove the bottom card from an empty stack...
########if self.left == 0:
########    # ...and the stack is NOT part of a Player Deck...
########    if self.owner == None:
########        # Report that the stack is empty.
########        print("There are no more cards in this stack.")
########    # OR, if the specified stack is a Player's discard pile...
########    elif self.name == "My Discard Pile":
########        # Report that the pile is empty.
########        print("Discard pile is empty.")
########    # OTHERWISE, the stack must be a Player's drawdeck...
########    else:
########        # So it's time to shuffle their deck.
########        self.owner.deck.shuffle()
##############################################################################
        # Remove the bottom card from the stack.
        self.stack.remove(self.bottom)
        # Reset the stack's "left" attribute.
        self.left = len(self.stack)
        # Reset the stack's "bottom" attribute.
        self.bottom = self.stack[left-1]
        # Reset the stack's bottom card ONLY if the top and bottom card are the same
        #   (i.e., there is only one card --or fewer-- in the stack)
        if self.left == 1:
            self.top = self.bottom

    def shuffle(self):
        #
        # This method shuffles the cards in the existing stack into random order.
        #
        # For every index location in the stack...
        for i in range(self.left):
            # Create a random integer between that index and the last index in stack.
            j = randint(i,self.left-1)
            # And switch the cards located at those two integers.
            self.stack[i], self.stack[j] = self.stack[j], self.stack[i]
        # Reset the stack's "top" attribute.
        self.top = self.stack[0]
        # Reset the stack's "bottom" attribute.
        self.bottom = self.stack[self.left-1]

    def destroy_card(self,card):
        #
        # This method removes the specified card from the stack.
        # *** NOTE: since this version of the game does not allow for player
        #           interaction with the destroy pile, any data associated with 
        #           a destroyed card does not need to be saved before destroying.
        #
        self.stack.remove(card)

###################################################################################################

###################################################################################################

class Deck:

    def __init__(self,player):
        #
        # Initializing a Deck object requires a Player object for its sole parameter.
        #
        # *** NOTE ***  Initializing a Deck object will immediately initialize two Stack objects,
        #               both of which have the specified player as their self.owner attribute.
        #
        # *** NOTE ***  The game's "Main deck,"" which is not "owned" by any player, 
        #               is NOT a Deck object, since it does not require two stacks (draw/discard).
        #               It is instead instantiated as a Stack object.
        #
        ######## Deck attributes ########
        self.drawdeck = Stack("My Deck",player)
        self.discards = Stack("My Discard Pile",player)
        self.owner = player

    ######## Deck Methods ########

    def shuffle_deck(self):
        #
        # This method shuffles the discard pile into the new draw pile.
        #
        # This method should be called ONLY
        #   - at the beginning of the game (as part of the "deal_starting_decks" Game method)
        #   - when draw pile is empty AND that pile needs to be accessed.
        #
        # Make the contents of the draw pile equal to the contents of the discard pile.
        self.drawdeck.stack = self.discards.stack
        # Reset the discard pile as empty.
        self.discards.stack = []
        # Reset the "left" attribute in both draw pile and discard pile.
        self.drawdeck.left = len(self.drawdeck.stack)
        self.discards.left = len(self.discards.stack)
        # Call the Stack method "shuffle" on the Player's draw pile.
        self.drawdeck.shuffle()

    def read_discards(self):
        #
        # This method prints the contents of this deck's discard pile.
        #
        # For every card in this deck's discard pile...
        for i in range(self.discards.left):
            # Call the "read" Card method on that card.
            self.discards.stack[i].read()

    def reveal_top_card(self):
        #
        # This method reveals the top card of this deck's draw pile.
        #
        # If the draw pile is empty...
        if self.drawdeck.left == 0:
            # It's time to shuffle the deck.
            self.shuffle_deck()
        # Call the "read" Card method on that card.
        self.drawdeck.top.read()

    def discard_top_card(self):
        #
        # This method removes the top card of this deck's draw pile and adds it to its discard pile.
        #
        # If the draw pile is empty...
        if self.drawdeck.left == 0:
            # It's time to shuffle the deck.
            self.shuffle_deck()
        # Add the drawdeck's top card to the discard pile. 
        self.discards.add_to_top(self.drawdeck.stack[0])
        # Remove that card from the drawdeck.
        self.drawdeck.remove_top_card()

###################################################################################################

###################################################################################################

class Hero:

    def __init__(self,hero_name,type_bonus=None,active=True):
    #
    #   Each Hero is initialized with a name, an optional Cardtype that triggers a Hero bonus,
    #   and an "Active" state, which will only be made false by certain cards in the game.
    #   Initializing a Hero object will also give it a 'triggered' list, which always begins
    #   at zero. This list may be used to determine when bonuses are (and are not) given.
    #
    ######## Hero Attributes ########
        self.name = hero_name
        self.bonus = type_bonus
        self.active = active
        self.triggered = []

    ######## Hero Methods ########

    def card_check(self,card):
        #
        # This method checks the specified cardtype against this Hero and returns
        #   a string based on that Hero's specific power.
        #
        # *** NOTE: This method is called by the "resolve" Card method.
        #
        # If that Card's cardtype attribute (a string) is identical to this hero's
        #   bonus type (another string)...
        if card.cardtype == self.bonus:
            # If this Hero is Superman...
            if self.name == "Superman":
                # Check to see whether this card name has triggered his power yet this turn.
                # If it hasn't...
                if card.name not in self.triggered:
                    # Add it to the triggered list, and return the string "Power."
                    self.triggered = self.triggered + [card.name]
                    return "Power"
                # Otherwise, no bonus is triggered.
                else:
                    return None
            # If this hero is Nightwing...
            elif self.name == "Nightwing":
                # If no card has triggered his power yet this turn...
                if len(self.triggered) == 0:
                    # Add this card name to the triggered list, and return the string "Power."
                    self.triggered = self.triggered + [card.name]
                    return "Power"
                # Or, if his power has only been triggered once so far this turn...
                elif len(self.triggered) == 1:
                    # Add this card name to the triggered list, and return the string "Draw."
                    self.triggered = self.triggered + [card.name]
                    return "Draw"
                # Otherwise, no bonus is triggered.
                else:
                    return None
            # If this hero is Batman...  
            elif self.name == "Batman":
                # Return "Power" regardless of how many times his power has been triggered this turn.
                return "Power"
            else:
                return None
        # If this hero is Green Lantern...
        elif self.name == "Green Lantern":
            # If this cardtype has not been played yet this turn, add it to the triggered list.
            if card.cardtype not in self.triggered:
                self.triggered = self.triggered + [card.cardtype]
            # Now, if there are three or more card types in the triggered list
            #   AND this hasn't been triggered yet on this turn...
            if (len(self.triggered) >= 3) and ("yes" not in self.triggered):
                # Add a string to the triggered list that shows that the power has been used this turn.
                self.triggered = self.triggered + ["yes"]
                # And return the appropriate string.
                return "2Power"
            # Otherwise, no bonus is triggered.
            else:
                return None
        # If this hero is Cyborg...
        elif self.name == "Cyborg":
            # If this card is a superpower OR equipment...
            if card.cardtype == "SuperPower":
            # and this cardtype has not been played this turn, add it to the triggered list.
                if card.cardtype not in self.triggered:
                    self.triggered = self.triggered + [card.cardtype]
                # otherwise...
                else:
                    # as long as your power hasn't been used yet...
                    if "yes" not in self.triggered:
                        # Add the string to show we've used the power...
                        self.triggered = self.triggered + ["yes"]
                        # And return the appropriate string.
                        return "Power"
                    # Otherwise, no bonus is triggered.
                    else:
                        return None
            elif card.cardtype == "Equipment":
            # and this cardtype has not been played this turn, add it to the triggered list.
                if card.cardtype not in self.triggered:
                    self.triggered = self.triggered + [card.cardtype]
                # otherwise...
                else:
                    # as long as your power hasn't been used yet...
                    if "yes" not in self.triggered:
                        # Add the string to show we've used the power...
                        self.triggered = self.triggered + ["yes"]
                        # And return the appropriate string.
                        return "Draw"
                    # Otherwise, no bonus is triggered.
                    else:
                        return None            
#           elif other scenarios for other superheroes...
#               ...
#               ...
        else:
            return None

###################################################################################################

flash = Hero("Flash")

###################################################################################################

class Player:

    def __init__(self,name,hero):
        ######## Player Attributes ########
        self.name = name
        self.hero = hero
        self.deck = Deck(self)
        self.hand = []
        self.power = 0
        self.cards_played = []
        self.next = None

    ######## Player Methods #########

    def draw_cards(self,count):
        #
        # This method draws the number of cards specified by the "count" parameter.
        #
        while count > 0:
            # If our draw pile is out of cards, time to shuffle our deck.
            if self.deck.drawdeck.left == 0:
                self.deck.shuffle_deck()
            # Add the top card of our newly shuffled draw pile to our hand.
            self.hand = self.hand + [self.deck.drawdeck.top]
            # Then delete that card from the draw pile.
            self.deck.drawdeck.remove_top_card()
            # One card has been added; decrement the count.
            count = count - 1

    def draw_hand(self,handsize=5):
        #
        # Draws a player's hand for the following turn. Default hand size is 5 cards.
        #
        # This method should be called:
        #   - at the start of the game, for each player.
        #   - at the end of each player's turn.
        #
        self.draw_cards(handsize)
#       for card in self.hand:
#           print(self.name,"is drawing a card...")
#           print(card.name)
#           print(card.owner.name)
        self.cards_played = []

    def add_to_discard(self,card):
        #
        # Takes a single card as a parameter.
        #
        # This method should be called:
        #   - at the start of the game, when each player is dealt their starting deck.
        #   - at the end of each player's turn, to add cards_played to discard pile.
        #   - every time that a card is gained by a player.
        #
        self.deck.discards.add_to_top(card)

    def read_hand(self):
        #
        # This method displays the contents of the player's hand.
        #
        handsize = len(self.hand)
        print()
        print("Here's your current hand:")
        print()
        for i in range(handsize):
            self.hand[i].read()

    def gain_card(self,card):
        #
        # Adds the specified card to the top of the Player's discard pile.
        #
        # If this Player is playing Aquaman AND the card costs 5 or less...
        if (self.hero.name == "Aquaman") and (card.cost <= 5)):
            # Prompt the player to choose whether to use Aquaman's power on this turn.
            choice = input("Would you like to put this card at the bottom of your deck? (Y / N) ")
            # If player says yes,
            #   put the card on the top of the player's deck.
            if choice == "Y" or choice == "y":
                self.deck.drawdeck.add_to_top(card)
            # If the player says no, gain the card normally.
            elif choice == "N" or choice == "n":
                self.deck.discards.add_to_top(card)
            # If the player's answer is incomprehensible, start this over.
            else:
                print("I'm sorry, I didn't catch that.")
                self.gain_card(card)
        # If the above condition is not true...
        else:
            # If this Player is playing Wonder Woman and this card is a villain...
            if (self.hero.name == "Wonder Woman") and ((card.cardtype == "Villain") or (card.cardtype == "SuperVillain")):
                # Add the card name to the triggered list.
                self.hero.triggered = self.hero.triggered + [card.name]
                print("You get to draw",len(self.hero.triggered),"extra card(s) next turn. How wonderful!")            
            # Gain the card normally.
            self.deck.discards.add_to_top(card)

    def purchase_card(self,card):
        if card.cost > self.power:
            print("That card is too expensive.")
        else:
            self.gain_card(card)
            self.power = self.power - card.cost

    def find_card_in_hand(self,string):
        print("Looking for a",string,"...")
        for i in range(len(self.hand)):
            if self.hand[i].name == string:
                return self.hand[i]
        return False

    def end_turn(self):
        #
        # This method ends the current player's turn, adds their played hand to the discard pile
        #   (as well as any cards not played this turn), and draws a new hand for that player.
        #
        # *** NOTE *** This method does NOT trigger the next player's turn.
        #
        # If there are any cards left unplayed in the Player's hand... 
        if len(self.hand) > 0:
            # Add them to the discard pile.
            for item in self.hand:
                self.add_to_discard(item)
            # And reset the player's hand to empty.
            self.hand = []
        # Discard all cards played by the player that turn.
        for item in self.cards_played:
            self.add_to_discard(item)
        # And reset that list to empty.
        self.cards_played = []
        # Reset the player's power to zero.
        self.power = 0
        # Draw a new hand for that player.
        # IF we're playing wonder woman, draw extra cards based on how many villains gained this turn.
        if self.hero.name == "Wonder Woman":
            self.draw_hand(5+len(self.hero.triggered))
        # Otherwise, draw a hand with the default number of cards.
        else:
            self.draw_hand()
        # Reset the bonus triggered by the player's superhero this turn.
        self.hero.triggered = []
        # Display end of turn.
        print("End of ",self.name,"'s turn.",sep='')

###################################################################################################

###################################################################################################

class Card:

    def __init__(self,name,cardtype,power,draw,vp,cost,defense=False,attack=False,other=False,text=""):
        # Card attributes
        self.name = name
        self.cardtype = cardtype
        self.power = power
        self.draw = draw
        self.vp = vp
        self.cost = cost
        self.defense = defense
        self.attack = attack
        self.other = other
        self.owner = None
        self.text = text
 
    ######## Card Methods ########

    def read(self):
        print(self.name," (",self.cardtype,") ",self.power," Power, ",self.vp," VPs",sep='')
        print(self.text)

    def resolve(self):
        # Display card name.
        print(self.name)
        print(self.power)
        print(self.owner.name)
        # Add card's power (if any) to player's power this turn.
        self.owner.power = self.owner.power + self.power
        # Draw cards equal to the draw count (if any) on this card.
        print("draw = ",self.draw)
        self.owner.draw_cards(self.draw)
        #
        #
        #########################################################
        #### Add code here! Needs to account for other ##########
        #### kinds of card text: draw, x-ray, stuff like that. ##
        #########################################################
        #
        # Check to see if playing this card triggers a SuperHero power.
        if self.owner.hero.card_check(self) == "Power":
            print("You get 1 bonus power!")
            self.owner.power = self.owner.power + 1
        elif self.owner.hero.card_check(self) == "2Power":
            print("You get 2 bonus power!")
            self.owner.power = self.owner.power + 2
        elif self.owner.hero.card_check(self) == "Draw":
            print("You get a bonus draw!")
            self.owner.draw_cards(1)
            if (self.owner.name == "Flash") and (self.owner.hero.triggered == []):
                print("You get a bonus draw!")
                self.owner.hero.triggered = self.owner.hero.triggered + ["yes"]
                self.owner.draw_cards(1)
        else:
            print("No Superhero Bonuses!")
        # Add the card we just played to the list of cards played this turn.
        self.owner.cards_played = self.owner.cards_played + [self]
        # Remove that card from the player's hand.
        self.owner.hand.remove(self)
        print("Power so far:",self.owner.power)
            
###################################################################################################

punch = Card("Punch","Starter",1,0,0,0)
vulnerability = Card("Vulnerability","Starter",0,0,0,0)

###################################################################################################

class Game:
    #
    # Takes a [list] of Player objects as an argument
    #
    def __init__(self,players):
        # Announce new game
        print("Starting a new game...")
        #
        # Game Attributes
        #
        self.maindeck = Stack("Main Deck")
        self.num_players = len(players)
        self.play_order = Queue(self,players)
#       self.lineup = []

    ######## Game Methods ########

    def show_playorder(self):
        print("Here's your play order:")
        for i in range(self.num_players):
            print(self.play_order.sequence[i].name," (",self.play_order.sequence[i].hero.name,")",sep='')

    def deal_starting_decks(self):
        #
        # This method deals out the starting deck (seven punches and three vulnerabilities) to each player.
        #
        # For each player in the game...
        for player in self.play_order.sequence:
#           print(player.name)
            # Add seven punches to their discard pile.
            for i in range(7):
                p = Card("Punch","Starter",1,0,0,0)
                player.add_to_discard(p)
            # Add three vulnerabilities to their discard pile.
            for i in range(3):
                v = Card("Vulnerability","Starter",0,0,0,0)
                player.add_to_discard(v)
            # Shuffle that pile into their deck.
            player.deck.shuffle_deck()

    def draw_starting_hands(self):
        for player in self.play_order.sequence:
            player.draw_hand()


###################################################################################################



###################################################################################################


class Queue:
    # takes a Game and a list of Players as arguments
    def __init__(self,game,players):
        #
        self.sequence = players
        num_players = len(self.sequence)
        # Randomize the list.
        # For each Player's indexed location in the list...
        for i in range(num_players):
            # Select a random integer between 0 and the last indexed location in the list...
            j = randint(0,num_players-1)
            # And switch the current Player's location with the Player at that random index.
            self.sequence[i], self.sequence[j] = self.sequence[j], self.sequence[i]
        #
        # We now have a randomized play order!
        # Now, we want to cycle through the list to see if any of our players are playing Flash.
        for i in range(num_players):
            # If so, switch that Player's place in the queue with whoever is first in the queue.
            if self.sequence[i].hero.name == "Flash":
                self.sequence[i], self.sequence[0] = self.sequence[0], self.sequence[i]
        #
        # Now it's time to make it a true queue, by assigning a "next" attribute to each item in the queue.
        #
        # Set the first in the queue.
        self.first = self.sequence[0]
        # And the last.
        self.last = self.sequence[num_players-1]
        # If we only have two players, this part is easy.
        if num_players == 2:
            # Set the first player's "next" attribute to the second player.
            self.first.next = self.last
        else:
            # But if we have more than two, we need to assign each item's "next" attribute
            #   to the player at the next index-- until we get to the final item, that is!
            for i in range(num_players-1):
                self.sequence[i].next = self.sequence[i+1]
        # Finally, set the last player's "next" attribute to the first player.
        # (This will be true no matter how many players are in the game,
        #   to ensure that we cycle back to the first player upon reaching the end of the play queue.)
        self.last.next = self.first
        #
        # *** NOTE: This is essentially a one-directional queue: each player can "see" who goes after them,
        #           but not who went before them. I think that should work fine with this game, since it
        #           rarely, as far I'm aware, requires looking backwards in the play queue. If we discover this 
        #           to be a more pertinent part of the game than we thought, however, we should add code to this
        #           section (and a prev attribute to the Player class) to account for it.
        #

###################################################################################################

###################################################################################################

class Turn:

    def __init__(self,player,gamedeck,lineup=[],kicks=[]):
        #### Turn Attributes ####
        self.lineup = lineup
        self.kicks = kicks
        self.player = player
        self.played_count = 0
        self.main_deck = gamedeck
        # Add cards to the lineup until it is full.
        self.restore_lineup()
        # Turn starts immediately, beginning with first phase.
        # Turn will not progress unless a player has been assigned to the turn.
        if self.player != None:
            self.phase_one()
#       Supervillain turn
#       elif...
        else:
            self.end_turn()

    def restore_lineup(self,cards=5):
        print("Restoring Lineup...")
        print()
#       print(len(self.lineup))
        while len(self.lineup) < cards:
            linecard = self.main_deck.top
            self.main_deck.remove_top_card()
            self.lineup = self.lineup + [linecard]
#           print(linecard.name)
        print("Here's your Line-Up:")
        print()
        for i in range(len(self.lineup)):
            print(self.lineup[i].name," (Cost: ",self.lineup[i].cost,")",sep='')

    def find_card_in_lineup(self,string):
        print("Looking for a",string,"...")
        for i in range(len(self.lineup)):
            if self.lineup[i].name == string:
                return self.lineup[i]
        return False

#   def select_card_to_buy(self,string):

    def phase_one(self):
        print()
        print(self.player.name,", you're up!",sep='')
        self.player.read_hand()
        self.play_phase()

    def play_phase(self):
        handsize = len(self.player.hand)
        print()
        print("Cards left:",handsize)
        print()
        # If the player is out of cards...
        if handsize == 0:
            # Skip to the next phase of the turn: purchasing cards.
            self.buy_phase()
        # Otherwise...
        else:
            print("Please type the name of the card you would like to play next.")
            print("Or, if you would now like to purchase a card, type P.")
            print("To look at the contents of your hand again, type H.")
            print("To end your turn, type 'end'.")
            prompt = input()
            # *** NOTE *** Card names are case-sensitive.
            # If the player chooses to end their turn, skip to the end_turn phase.
            if prompt == 'end':
                self.final_phase()
            # If the player chooses to, skip to the next phase of the turn: purchasing cards.
            elif prompt == "P" or prompt == "p":
                self.buy_phase()
            # If the player chooses to see their hand again, read hand and return to the beginning of this phase.
            elif prompt == "H" or prompt == "h":
                self.player.read_hand()
                self.play_phase()
            # Otherwise, play the card chosen by the player.
            else:
                # First, try to find the card typed by the player in the player's hand. If it's there...
                if self.player.find_card_in_hand(prompt) != False:
                    c = self.player.find_card_in_hand(prompt)
                    c.resolve()
                    self.play_phase()
                else:
                    print("You don't have a card called that in your hand.")
                    self.play_phase()

    def buy_phase(self):
        print("You have ",self.player.power," power to spend.",sep='')
        if self.player.power == 0:
            if self.player.hand != []:
                choice = input("You have no power to spend, but there are still cards in your hand. Would you like to play a card? (Y / N) ")
                if choice == "Y" or choice == "y":
                    self.play_phase()
                elif choice == "N" or choice == "n":
                    self.final_phase()
                else:
                    print("I'm sorry, I didn't catch that.")
                    self.buy_phase()
            else:
                self.final_phase()
        else:
            choice = input("Would you like to buy a card? (Y / N) ")
            if choice == "Y":
                #
                # Reveal lineup, prompt user for card name.
                print("Alrighty then!")
                # Prompt the user for a card name.
                print("The current Line-Up contains the following cards:")
                for item in self.lineup:
                    print(item.name," (",item.cost,") ",sep='')
                if self.kicks != []:
                    print("There are also ",len(self.kicks)," Kicks left in the Kicks stack.")
                cardname = input("What card would you like to purchase? ")
                if cardname == "Kick":
                    print('a kick!')
                    if self.kicks != []:
                        print('adding a kick to your deck...')
                        self.player.purchase_card(self.kicks[0])
                        print('removing a kick from the kstack...')
                        self.kicks.remove(self.kicks[0])
                        ('and moving on...')
                        self.buy_phase()
                    else:
                        print("There are no more Kicks available for purchase.")
                        self.buy_phase()
                elif self.find_card_in_lineup(cardname) != False:
                    card = self.find_card_in_lineup(cardname)
                    self.lineup.remove(card)
                    self.player.purchase_card(card)
                    print("Bought it!")
                    self.buy_phase()
                else:
                    print("That card is not in the lineup this turn.")
                    self.buy_phase()
            elif choice == "N":
                if len(self.player.hand) > 0:
                    choice = input("You have cards left in your hand. Would you like to play another card? (Y / N) ")
                    if choice == "Y" or choice == "y":
                        self.play_phase()
                    elif choice == "N" or choice == "n":
                        self.final_phase()
                    else:
                        print("I'm sorry, I didn't catch that.")
                        self.buy_phase()
                else:
                    self.final_phase()
            else:
                print("I didn't catch that.")
                self.buyphase()

    def final_phase(self):
        final = input("Would you like to end your turn? (Y / N) ")
        if final == "Y" or final == "y":
            self.player.end_turn()
        elif final == "N" or final == "n":
            self.buy_phase()
        else:
            print("I'm sorry, I didn't catch that.")
            self.final_phase()

###################################################################################################

###################################################################################################

