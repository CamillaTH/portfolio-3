import unittest
from HangmanHelper import HangmanHelper
from unittest.mock import patch
from Globals import Globals


class HangmanHelperTestFunctions(unittest.TestCase):

    def test_validate_game_choices_valid_input(self):
        """
       Tests that validation of game choices input are correct
       Should return True since 1 or 2 are valid
       """
        self.assertTrue(HangmanHelper.validate_game_choices("1"))
        self.assertTrue(HangmanHelper.validate_game_choices("2"))

    def test_validate_game_choices_invalid_input(self):
         """
         Tests that validation of game choices input are correct
         Should return False since 6 invalid
         """
         with patch('builtins.input', side_effect=["6"]):
             self.assertFalse(HangmanHelper.validate_game_choices("6"))

    def test_validate_players_letter_choice_invalid_non_alphabetic(self):
        """
         Tests that validation of letter choices input are correct
         Should return False since 123 invalid (only 1 letter and alphabetic)
         """
        self.assertFalse(HangmanHelper.validate_players_letter_choice("123"))

    def test_validate_players_letter_choice_invalid_multiple_letters(self):
        """
         Tests that validation of letter choices input are correct
         Should return False since abc invalid (only 1 letter)
         """
        self.assertFalse(HangmanHelper.validate_players_letter_choice("abc"))

    def test_validate_players_letter_choice_invalid_already_guessed(self):
        """
         Tests that validation of letter choices input are correct
         Should return False since b is already guessed
         """
        Globals.guessed_letters = ["b", "t", "v"]
        self.assertFalse(HangmanHelper.validate_players_letter_choice("b"))
        Globals.guessed_letters = []

    def test_validate_players_letter_choice_valid(self):
        """
         Tests that validation of letter choices input are correct
         Should return True since b is valid and not already guessed
         """
        self.assertTrue(HangmanHelper.validate_players_letter_choice("b"))
