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
        if helper.resolve_chars_to_show() == Globals.word_to_guess:
            print(helper.resolve_chars_to_show())
            print("You won, you guessed the right word!\n")
            break
        # if true user have not exceeded max guesses
        if Globals.guesses < Globals.max_guesses:
            # the guessed char is not a part of the word to guess
            if user_guess not in Globals.word_to_guess:
                # increment number of guesses by 1
                Globals.guesses = Globals.guesses + 1
            else:
                # user gussed the correct char
                print(f"The letter {user_guess} is correct!")
            print(f"You have {Globals.max_guesses - Globals.guesses} guesses left\n")
            if Globals.guesses < 8 and Globals.guesses > 0:
                # show the user how many wrong guesses visually
                print(Globals.hangman_drawings[Globals.guesses-1])
            print(helper.resolve_chars_to_show())
            # max guesses is achieved end program 
            if Globals.guesses == Globals.max_guesses:
                print(Globals.hangman_drawings[Globals.guesses-1])
                print(f"The word was {Globals.word_to_guess}\n")
                print("You are hanged! Better luck next time!\n")
                break
            print("_______________________________________\n")


init()