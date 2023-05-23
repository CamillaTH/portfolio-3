from Globals import Globals
from HangmanHelper import HangmanHelper

def init():
    """
    Function thats init the program and starts the game
    """

    # create instance of Drawings class to be able to visually show the user how many guesses there are left.
    helper = HangmanHelper()

    game_mode = input("Welcome to hangman! For multiplayer (your friend chooses a word) press 1 for singleplayer (computer chooses word) press 2 :\n")
    
    
init()