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