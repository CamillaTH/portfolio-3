import random
from Globals import Globals


class HangmanHelper:
    """
    Class that holds helper functions for the hangman game
    """

    @staticmethod
    def validate_game_choices(game_choice):
        """
       checks if input is 1 or 2 if not raise ValueError
       :param game_choice:
       :return: true if validates else false
       """
        try:
            if int(game_choice) != 1 and int(game_choice) != 2:
                raise ValueError("input needs to be 1 or 2!")
        except ValueError as ve:
            print(f"Invalid input: {ve}, try again.\n")
            return False

        return True

    @staticmethod
    def get_computer_word(difficultly):
        """
       Gets a random word from the easy or hard .txt list.
       When the user puts 1 as input the function gets the easy
       word list and when the user chooses 2 the hard word list
       :param difficultly:
       :return String:
       """
        
        if int(difficultly) == 1:
            file_path = "words/hangman_words_easy.txt"
        else:
            file_path = "words/hangman_words_hard.txt"

        words_list = []
        with open(file_path) as word_file:
            for word in word_file:
                words_list.append(word)

        # shuffle the list before picking a word from the list
        random.shuffle(words_list)

        return random.choice(words_list).upper()

    @staticmethod
    def validate_players_word_choice(word):
        """
       checks if input has no blank spaces is between 
       3 and 12 chars and alphabetic if not raise ValueError
       :param word:
       :return: true if validates else false
       """
        try:
            if " " in word:
                raise ValueError("Word can't have blank spaces")
            if not word.isalpha():
                raise ValueError("Word needs to be Alphabetic")
            if len(word) < 3 or len(word) > 12:
                raise ValueError("Word needs to be between 3 and 12 chars")
        except ValueError as ve:
            print(f"Invalid input: {ve}, try again.\n")
            return False

        return True

    @staticmethod
    def validate_players_letter_choice(letter):
        """
       checks if input is char and alphabetic if or word already ben guessed if not raise ValueError
       :param letter:
       :return: true if validates else false
       """
        try:
            if not letter.isalpha():
                raise ValueError("Letter needs to be Alphabetic")
            if len(letter) > 1:
                raise ValueError("Letter needs to be a single letter")
            if letter in Globals.guessed_letters:
                raise ValueError("You have already guessed that "
                                 "letter choose another one!")
        except ValueError as ve:
            print(f"Invalid input: {ve}, try again.\n")
            return False
        return True

    @staticmethod
    def resolve_chars_to_show():
        """
       resolves witch chars to show in the underscore string
       :return: string
       """
        return "".join([char if char in Globals.guessed_letters else "_" for char in Globals.word_to_guess])

    @staticmethod
    def resolve_rerun_game(run_again):
        """
       resolves if the user want to rerun the game or exit the game 1 for rerun 2 for exit
       :return: boolean 
       """
        try:
            if int(run_again) != 1 and int(run_again) != 2:
                raise ValueError("input needs to be 1 or 2!")
        except ValueError as ve:
            print(f"Invalid input: {ve}, try again.\n")
            return False
        # Rerun game
        if int(run_again) == 1:
            return True
        #exit game
        else:
            return False