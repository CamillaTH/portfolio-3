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
