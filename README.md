# High-Low Card Game
#### Video Demo:  <https://youtu.be/l-ameRQLqCc>
## Description:
### Game explanation
This is a digital version of a quick and simple card game I used to play. We called it High-Low.
The goal of the game is to make the correct guess about the next card through 4 different stages in a row.
The stages are as follows:
1. Is the next card red or black?
2. Is the rank of the next card higher or lower than the first card?
3. Is the rank of the next card in between the previous two cards or not?
4. What suit it the final card?

To win, you must make correct guesses 4 times in a row (i.e successfully beat all 4 stages without making a mistake) before the deck runs out.
If you make an incorrect guess, you have to restart to stage 1 and repeat until you win or until the deck runs out (in which case you lose).

The user interacts with the VSCode Terminal, they are shown ASCII representations of cards, and they make guesses and progess through the game by typing in their input.

### Structure of code
I used OOP to code the project. And it is a bit overkill considering the required minimum of just 3 functions. But I wanted to push my abilities to a further extent.

There are two classes: CardGame, and Card

#### 1. CardGame
Most of the functionality is in here, and the game starts when CardGame() is called.

This class variables are three lists:
- These class variables keep track of the draw pile, discard pile, and the pile of cards that are in play (I call it 'play_pile'). These class variables are lists that contain tuples representing the cards in a deck. For example, an Ace of Spades is represented as ("spade", "ace").

The methods are as follows:
- __init__() calls the welcome() method, which introduces the game and lets the player explore the rules of each stage.
- reset() will empty the discard and play pile, and reset the deck. So after reset() is called, discard_pile and play_pile are empty lists, while draw_pile will contain 52 tuples representing all of the cards in a deck. This is the first method that makes use of the Card class, which I'll explain in detail later.
- start_game() creates the logic for the progession of each stage. This method will progress the player through the next stage if they guess correctly, take the player back to stage 1 if they guess incorrectly, and prompt a restart if the draw pile runs out of cards.
- If the player successfully beats all 4 stages in a row, start_game() will call victory(), which simply prints "Victory!"
- In the case of victory() or the deck running out of cards, restart_prompt() will be called which allows the user to input whether they want to restart or exit the game
- game1() - game4() provide the functionality for each game. It asks the relevant question, and executes the corresponding conditional statements and returns a True or False value depending on the user's input.
- rank_to_num(rank) allows me to convert the rank values of a card into their corresponding 'strengths' (eg. a King in numerical form should be represented as 13) This allows me to directly compare the value of a face card to a number card (I can now say: "king" > "nine (in terms of strength))
- draw_card() will randomly choose an element in draw_pile and return its tuple value
- show(cards, hidden_card = False) will print out the ASCII representation of 'cards' (usually the current play_pile) on the terminal for the user to see. If 'hidden_card' is set to True, an additional unrevealed card will be shown which gives the user the impression of a card that has been drawn but is yet to be flipped (like in a poker game).
- discard(cards) will move all of the tuples in 'cards' (also usually the currect play_pile) into discard_pile

#### 2. Card
This class is sort of a sub-class of CardGame in the sense that it is solely made to be used in the CardGame class. It is never called directly by the user. It makes the code look more structured and legible

The class variables in this class are two dictionaries and a string.
- For the dictionaries SUITS_ASCII and RANKS_ASCII, the keys are the values of the parameters of the Card() instance whenever it is created in the CardGame class. The values of these keys are the corresponding characters that will be printed on the terminal whenever we need an ASCII representation of the card (i.e whenever the show() method is called in CardGame)
- the string, 'hidden_card', provides an ASCII representation of the back of a generic card. So when show() hidden_card is set to True, this string will be printed as well at the end of the cards in play.

The methods are as follows:
- \__init__() initialises the parameters and does simple error checking. However, most of the error checking and value validity falls in the getters and setters below
- The suit/rank setters allow a bit of flexibility with regard to the allowed inputs for the parameters of a Card() instance. It also raised more legible errors in case I made a mistake early on in my project. The setters allowed me to input various values (like 'Spades', 'spades', 's' or 'K', 'King' 'k') and will always return the correct value (in this case: 'spade' and 'king') required for my code to work. The setters are a bit unnecessary for a project like this since the user never has to explicitly call the Card() function, and I never needed the additional flexibility when coding this project, but it was definitely good practice for me.
- \__repr__() simply does what \__repr__ should do
- \__str__() provided the printing functionality that I primarirly used for debugging purposes, but allowed me to make my show() function simpler as well. It prints out the ASCII representation of the Card() in question.




