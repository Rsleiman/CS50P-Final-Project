"""HIGHER OR LOWER
Four stages of the game:
1. Red or Black?
    - Ask user whether the following card will be red (hearts/diamond) or black (club/spade) [2 options]
    - Randomly draw a card from remaining 'deck'
    - If correct, move to next step
    - If incorrect, restart (but keep drawn cards out of deck)

2. Higher or Lower?
    - Ask user whether the following card will be higher or lower than the previous card drawn [2 options]
    - Randomly draw a card from remaining deck
    - If correct, move to next step
    - If incorrect, restart (but keep drawn cards out of deck)

3. In Between or Outside?
    - Ask user whether the rank of the following card will be in between the two previous cards or outside [2 options]
    - Randomly draw a card
    - If correct, move to next step
    - If incorrect, restart (but keep drawn cards out of deck)
    - If card rank equals either of the two previous cards, assume incorrect

4. Which suit?
    - Ask user which suit the next card will be [4 options]
    - If correct, user has won the game. Promt user to restart game (Reshuffle deck)
    - If incorrect, restart (but keep drawn cards out of deck)
"""

SUITS_ASCII = {"spade":"♠", "heart":'♥', "club":"♣", "diamond":"♦"}
RANKS_ASCII = {
    "ace":"A",
    "king":"K",
    "queen":"Q",
    "jack":"J",
    "ten":"10",
    "nine":"9",
    "eight":"8",
    "seven":"7",
    "six":"6",
    "five":"5",
    "four":"4",
    "three":"3",
    "two":"2",
    }

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    ...



    ## Error checking rank
    @property
    def rank(self):
        return self._rank


    @rank.setter
    def rank(self, rank):
        if rank.lower() not in RANKS_ASCII:
            raise ValueError("Invalid card number")
        self._rank = rank.lower()
    ##

    ## Error checking suit
    @property
    def suit(self):
        return self._suit


    @suit.setter
    def suit(self, suit):
        if suit.lower() not in SUITS_ASCII:
            raise ValueError("Invalid suit")
        self._suit = suit.lower()
    ##

    def ASCII(self, rank, suit):
        print(f"┌───────────┐\n\
        │{rank}          │\n\
        │{suit}          │\n\
        │           │\n\
        │           │\n\
        │           │\n\
        │          {suit}│\n\
        │          {rank}│\n\
        └───────────┘"
        )

        ## Add characters to shape the card
        ## Add rank in rank spots
        ## Add suit in suit spots
        ...
        return drawing

    ...

card = Card("ace", "club")
print(card.rank)
print(card.suit)

card.ASCII


print(u'\u2500')





### CONSTANTS
# full+deck
# ASCII version of ranks and suits (To display cards in the terminal)
# Numerical version of ranks and suits (To use for conditional statements in game functions)
# ASCII Drawing of an unturned card


### Variables:
# deck
# pile/history
# drawn_card

def game1():
    ## Display unturned card
    ## Ask user "Red or black?"
    ## Draw card
    ## if chose Red:
        ## if suit = diamond or hearts:
            ## Next game
        ## else:
            ## hide cards OR move cards to compact form above
            ## back to game 1
    show_unturned()
    # card1 = #blank
    # card2 = #blank
    while True:
        guess = input("Red or Black?\nr/b: ")
        if guess.lower() == "red" or guess == "r":
            #TODO
            break
        elif guess.lower() == "black" or guess.lower() == "b":
            #TODO
            break
        else:
            print("\nInvalid input: Please type either 'red'/'black' or 'r'/'b'")
            continue

def game2():
    # card1 = ____
    # card2 = #blank
    while True:
        guess = input("Higher or Lower?\nh/l: ")
        if guess.lower() == "higher" or guess.lower() == "h":
            #TODO
            break
        elif guess.lower() == "lower" or guess.lower() == "l":
            #TODO
            break
        else:
            print("\nInvalid input: Please type either 'higher'/'lower' or 'h'/'l'")
            continue

def game3():
    # card1 = ____
    # card2 = ____
    while True:
        guess = input("Between or Outside?\nb/o: ")
        if guess.lower() == "between" or guess.lower() == "b":
            #TODO
            break
        elif guess.lower() == "outside" or guess.lower() == "o":
            #TODO
            break
        else:
            print("\n Invalid input: Please type either 'between'/'outside' or 'b'/'o'")
            continue

def game4():
    while True:
        guess = input("Which suit?\ndiamonds/clubs/hearts/spades: ")
        spade = ["spade", "spades", "s", "♠"]
        heart = ["heart", "hearts", "h", "♥"]
        club = ["club", "clubs", "c", "♣"]
        diamond = ["diamond", "diamonds", "d", "♦"]
        if guess.lower() in spade:
            #TODO
            break
        elif guess.lower() in heart:
            #TODO
            break
        elif guess.lower() in club:
            #TODO
            break
        elif guess.lower() in diamond:
            #TODO
            break
        else:
            print("\n Invalid input: Please input a valid suit (spades/hearts/clubs/diamonds)")
            continue

def card_history(): #Needed??
    ...



"""
TODO:
    - Figure out if we want to show the user the previous cards in the event of them having to reset to game one
        - Do we want a compact version above the cards that show previous cards? Example:
            A| J| 2| 7| A|
            ♠| ♥| ♥| ♣| ♠|
    - Implement functions
    - Add colour to the cards



 """
