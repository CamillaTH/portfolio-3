from Globals import Globals
from HangmanHelper import HangmanHelper


def init():
    """
    Function thats init the program and starts the game
    """

    # create instance of HangmanHelper class to be able to use helper functions
    helper = HangmanHelper()

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
    
    # if game_mode is 2 take input from the user which difficultly 
    # and validate it re-run until user enter correct input
    if int(game_mode) == 2:
        while True:
            difficultly = input("Please choose difficultly. Press 1 for easy 2 for hard:\n")
            if helper.validate_game_choices(difficultly):
                break
            continue
        Globals.word_to_guess = helper.get_computer_word(difficultly)
    
    # if game_mode is 1 take input from the user which
    # word the other use should guess
    else:
        while True:
            Globals.word_to_guess = input(
                "Now your friend have to write a word for you to guess (min 3 chars, max 12 chars, "
                "no blank spaces) :\n").upper()
            if helper.validate_players_word_choice(Globals.word_to_guess):
                break
            continue
    # print the amount of chars in the word as underscore for the user
    print(helper.resolve_chars_to_show())
    print("Now let's guess! \n")
    
    while True:
        user_guess = input("Type a letter\n").upper()
        if not helper.validate_players_letter_choice(user_guess):
            continue
        # add the guessed letter to GUESSED_LETTERS list
        Globals.guessed_letters.append(user_guess)


init()