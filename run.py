from Globals import Globals
from HangmanHelper import HangmanHelper

def init():
    """
    Function thats init the program and starts the game
    """

    # create instance of HangmanHelper class to be able to use helper functions
    helper = HangmanHelper()
    # create instance of globlas class 
    globals = Globals()

    # take input from the user what game mode
    # and validate it re-run until user enter correct input
    while True:
        game_mode = input(
            "Welcome to hangman! For multiplayer (your friend chooses a word) "
            "press 1 for single-player press 2 (computer chooses word):\n")
        if helper.validate_game_choices(game_mode):
            break
        else:
            continue
    

init()