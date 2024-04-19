import random, time, os

class Card:
    SUITS_ASCII = {"spade": "♠", "heart": '♥', "club": "♣", "diamond": "♦"}
    RANKS_ASCII = {
        "ace": "A",
        "king": "K",
        "queen": "Q",
        "jack": "J",
        "ten": "10",
        "nine": "9",
        "eight": "8",
        "seven": "7",
        "six": "6",
        "five": "5",
        "four": "4",
        "three": "3",
        "two": "2"
    }
    hidden_card = "┌───────────┐\n\
│░░░░░░░░░░░│\n\
│░░░░░░░░░░░│\n\
│░░░░░░░░░░░│\n\
│░░░░░░░░░░░│\n\
│░░░░░░░░░░░│\n\
│░░░░░░░░░░░│\n\
│░░░░░░░░░░░│\n\
└───────────┘"

    def __init__(self, suit:str, rank):

        self.suit = suit
        self.rank = rank

        # Check if card has been drawn previously
        if (self.suit, self.rank) in CardGame.discard_pile:
            raise ValueError("Card has already been drawn")

        # Card.discard_pile.append(f"{self.rank.title()} of {self.suit+'s'}")
        # CardGame.discard_pile.append((self.suit, self.rank))


    # Suit getter and setter
    @property
    def suit(self):
        return self.__suit

    @suit.setter
    def suit(self, value:str):
        if value.lower() in Card.SUITS_ASCII: # Testing perfect match case-insensitive
            self.__suit = value.lower()
        elif value.lower()[:-1] in Card.SUITS_ASCII: # Testing for match with valid plural
            self.__suit = value[:-1].lower()
        elif len(value) == 1:   # Testing for valid abbreviation
            self.__suit = next((key for key in Card.SUITS_ASCII.keys() if key.startswith(value)), None) # Convert value to unabbreviated form
        else:
            raise Exception(f"'{value}' not a valid suit")

        self.suit_ASCII = Card.SUITS_ASCII[self.__suit]


    # Rank getter and setter
    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, value):
        value = str(value).upper() # Convert to string and uppercase as needed
        if value.lower() in Card.RANKS_ASCII: # Testing perfect match case-insensitive
            self.__rank = value.lower()
        elif value.lower()[:-1] in Card.RANKS_ASCII: # Testing for match with valid plural
            self.__rank = value[:-1].lower()
        elif value in Card.RANKS_ASCII.values(): # Testing if values have been used instead of keys
            value = list(Card.RANKS_ASCII.keys())[list(Card.RANKS_ASCII.values()).index(value)] # Convert from value to key
            self.__rank = value
        else:
            raise Exception(f"'{value}' not a valid rank")

        self.rank_ASCII = Card.RANKS_ASCII[self.__rank]



    # Representation functionality
    def __repr__(self):
        return(f"Card({self.__suit}, {self.__rank}")

    # Printing the cards on console
    def __str__(self):
        if self.rank_ASCII == "10":
            return(f"┌───────────┐\n\
│{self.rank_ASCII}         │\n\
│{self.suit_ASCII}          │\n\
│           │\n\
│           │\n\
│           │\n\
│         {self.rank_ASCII}│\n\
│          {self.suit_ASCII}│\n\
└───────────┘")

        else:
            return(f"┌───────────┐\n\
│{self.rank_ASCII}          │\n\
│{self.suit_ASCII}          │\n\
│           │\n\
│           │\n\
│           │\n\
│          {self.rank_ASCII}│\n\
│          {self.suit_ASCII}│\n\
└───────────┘")

class CardGame:
    draw_pile = []
    play_pile = []
    discard_pile = []

    # Should I define these as class variables? Or only instantiate them in the __init__ method?


    def __init__(self):
        os.system('cls||clear')
        self.welcome()

    def welcome(self):
        print("Welcome to High-Low")
        print("Expand the terminal/console for a better viewing experience")
        input("\nPress Enter to continue...")

        os.system('cls||clear')
        print("There are 4 minigames:\n")
        print("1. Red or black?,\n2. Higher or lower?,\n3. In between or outside?,\n4. Which suit?")
        print("\nSuccessfully beat all four minigames in a row before the deck of cards runs out to win!")
        print("If you fail a minigame, start from the beginning")
        while True:
            output = input("\nPress Enter to begin... OR input 1, 2, 3, or 4 to understand the rules of each minigame\n\n")
            if output == "1":
                os.system('cls||clear')
                print("MINIGAME 1:\nGuess if the next card will be a red or black card")
                continue
            elif output == "2":
                os.system('cls||clear')
                print("MINIGAME 2:\nGuess if the next card will be higher or lower than the previous card")
                continue
            elif output == "3":
                os.system('cls||clear')
                print("MINIGAME 3:\nGuess if the next card will be in between the previous two cards, or outside the previous two cards")
                continue
            elif output == "4":
                os.system('cls||clear')
                print("MINIGAME 4:\nGuess the suit of the next card")
                continue
            else:
                os.system('cls||clear')
                break

        self.reset()


    def reset(self):
        os.system('cls||clear')
        self.play_pile = []
        self.draw_pile = []
        self.discard_pile = []
        for suit in Card.SUITS_ASCII:
            for rank in Card.RANKS_ASCII:
                self.draw_pile.append((suit, rank))

        # TESTING WITH SMALLER DECK
        # self.draw_pile = self.draw_pile[0:4]

        print("Deck has been reset")
        time.sleep(1)
        self.start_game()


    def start_game(self):
        """Main game functionality
        TODO: Ensure that games get interrupted if deck runs out of cards"""
        while len(self.draw_pile) > 0:
            if self.game1():
                input("Correct! Press Enter to continue...")
                if len(self.draw_pile) == 0:
                    break
            else:
                self.discard(self.play_pile)
                input("Incorrect. Press Enter to restart...")
                continue

            if self.game2():
                input("Correct! Press Enter to continue...")
                if len(self.draw_pile) == 0:
                    break
            else:
                self.discard(self.play_pile)

                input("Incorrect. Press Enter to restart...")
                continue

            if self.game3():
                input("Correct! Press Enter to continue...")
                if len(self.draw_pile) == 0:
                    break
            else:
                self.discard(self.play_pile)
                input("Incorrect. Press Enter to restart...")
                continue

            if self.game4():
                input("Correct! Press Enter to continue...")
                self.victory() # Functionality to break from start_game function entirely
                return
            else:
                self.discard(self.play_pile)
                if len(self.draw_pile) == 0:
                    break
                input("Incorrect. Press Enter to restart...")
                continue

        os.system('cls||clear')
        print("Ran out of cards! Game over")
        time.sleep(1)

        self.restart_prompt()


    def restart_prompt(self):
        while True:
            ans = input("Restart game? 'y'/'n':\n")
            if ans.lower() == "y" or ans.lower() == "yes" :
                self.reset()
                break

            elif ans.lower() == "n" or ans.lower() == "no":
                os.system('cls||clear')
                print("Thanks for playing!")
                break
            else:
                os.system('cls||clear')
                print("Not valid answer, input 'yes'/'y' or 'no'/'n'")
                continue


    def game1(self):
            os.system('cls||clear')
            self.show(self.play_pile, hidden_card = True)
            while True:
                guess = input("Red or black?\n")
                os.system('cls||clear')
                if guess.lower() == "red" or guess.lower() == "r":
                    card = self.draw_card()
                    self.show(self.play_pile)
                    if card[0] == "diamond" or card[0] == "heart":
                        return True
                    else:
                        return False
                elif guess.lower() == "black" or guess.lower() == "b":
                    card = self.draw_card()
                    self.show(self.play_pile)
                    if card[0] == "club" or card[0] == "spade":
                        return True
                    else:
                        return False
                else:
                    os.system('cls||clear')
                    self.show(self.play_pile, hidden_card = True)
                    print("Not valid answer, input 'red'/'r' or 'black'/'b'")

                    continue


    def game2(self):
        os.system('cls||clear')
        self.show(self.play_pile, hidden_card = True)
        while True:
            guess = input("Higher or lower?\n")
            os.system('cls||clear')
            if guess.lower() == "higher" or guess.lower() == "h":
                card = self.draw_card()
                self.show(self.play_pile)
                num1 = self.rank_to_num(self.play_pile[-2][1])
                num2 = self.rank_to_num(card[1])
                if num2 > num1:
                    return True
                else:
                    return False
            elif guess.lower() == "lower" or guess.lower() == "l":
                card = self.draw_card()
                self.show(self.play_pile)
                num1 = self.rank_to_num(self.play_pile[-2][1])
                num2 = self.rank_to_num(card[1])
                if num2 < num1:
                    return True
                else:
                    return False
            else:
                os.system('cls||clear')
                self.show(self.play_pile, hidden_card = True)
                print("Not valid answer, input 'higher'/'h' or 'lower'/'l'")
                continue


    def game3(self):
        os.system('cls||clear')
        self.show(self.play_pile, hidden_card = True)
        while True:
            guess = input("In between or outside?\n")
            os.system('cls||clear')
            if guess.lower() == "between" or guess.lower() == "b":
                card = self.draw_card()
                self.show(self.play_pile)
                num1 = self.rank_to_num(self.play_pile[-3][1])
                num2 = self.rank_to_num(self.play_pile[-2][1])
                num3 = self.rank_to_num(card[1])
                if num1 < num3 < num2 or num2 < num3 < num1:
                    return True
                else:
                    return False
            elif guess.lower() == "outside" or guess.lower() == "o":
                card = self.draw_card()
                self.show(self.play_pile)
                num1 = self.rank_to_num(self.play_pile[-3][1])
                num2 = self.rank_to_num(self.play_pile[-2][1])
                num3 = self.rank_to_num(card[1])
                if num1 <= num3 <= num2 or num2 <= num3 <= num1:
                    return False
                else:
                    return True
            else:
                os.system('cls||clear')
                self.show(self.play_pile, hidden_card = True)
                print("Not valid answer, input 'between'/'b' or 'outside'/'o'")
                continue


    def game4(self):
        os.system('cls||clear')
        self.show(self.play_pile, hidden_card = True)
        while True:
            guess = input("Which suit?\n")
            os.system('cls||clear')
            if guess.lower() == "diamond" or guess.lower() == "d":
                card = self.draw_card()
                self.show(self.play_pile)
                if card[0] == "diamond":
                    return True
                else:
                    return False
            elif guess.lower() == "heart" or guess.lower() == "h":
                card = self.draw_card()
                self.show(self.play_pile)
                if card[0] == "heart":
                    return True
                else:
                    return False
            elif guess.lower() == "club" or guess.lower() == "c":
                card = self.draw_card()
                self.show(self.play_pile)
                if card[0] == "club":
                    return True
                else:
                    return False
            elif guess.lower() == "spade" or guess.lower() == "s":
                card = self.draw_card()
                self.show(self.play_pile)
                if card[0] == "spade":
                    return True
                else:
                    return False
            else:
                os.system('cls||clear')
                self.show(self.play_pile, hidden_card = True)
                print("Not valid answer, input 'diamond'/'d', 'heart'/'h', 'club'/'c' or 'spade'/'s'")

                continue


    def rank_to_num(self, rank):
        dictionary = {
            "ace":14, "king":13, "queen":12, "jack":11,
            "ten":10, "nine":9, "eight":8, "seven":7,
            "six":6, "five":5, "four":4, "three":3,
            "two":2
            }
        return dictionary[rank]


    def victory(self):
        """Break from self.start_game() loop, prompt restart, with input error looping"""
        print("Victory!")
        time.sleep(1)
        self.restart_prompt()

        # while True:
        #     ans = input("Restart game? 'y'/'n':\n")
        #     if ans.lower() == "y" or ans.lower() == "yes" :
        #         self.reset()
        #     elif ans.lower() == "n" or ans.lower() == "no":
        #         print("Thanks for playing!")
        #     else:
        #         print("Not valid answer, input 'yes'/'y' or 'no'/'n'")
        #         continue


    def draw_card(self):
        card = self.draw_pile.pop(self.draw_pile.index(random.choice(self.draw_pile)))
        self.play_pile.append(card)
        return card


    def show(self, cards:list, hidden_card = False):
        """Show on console the current play_pile from left to right"""
        if len(cards) > 10:
            print("Too many cards in play to display")
        else:
            output = []
            line = []

            if hidden_card:
                for i in range(9):
                    for card in cards:
                        string = Card(card[0],card[1]).__str__()
                        row = string.split("\n")[i]
                        line.append(row)
                    line.append(Card.hidden_card.split("\n")[i])
                    output.append(line)
                    line = []

            else:
                for i in range(9):
                    for card in cards:
                        string = Card(card[0],card[1]).__str__()
                        row = string.split("\n")[i]
                        line.append(row)

                    output.append(line)
                    line = []

            for lines in output:
                for card in lines:
                    print(card, end=" ")
                print()


    def discard(self, cards:list):
        """Move cards in play_pile to discard_pile"""
        for card in cards:
            self.discard_pile.append(card)
        self.play_pile = []


if __name__ == "__main__":
    game = CardGame()
