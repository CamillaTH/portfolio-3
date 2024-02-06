import unittest
from HangmanHelper import HangmanHelper
from unittest.mock import patch


class HangmanHelperTestFunctions(unittest.TestCase):

    def test_validate_game_choices_valid_input(self):
        self.assertTrue(HangmanHelper.validate_game_choices("1"))
        self.assertTrue(HangmanHelper.validate_game_choices("2"))

    def test_validate_game_choices_invalid_input(self):
         with patch('builtins.input', side_effect=["6"]):
             self.assertFalse(HangmanHelper.validate_game_choices("6"))

    def test_validate_players_letter_choice_invalid_non_alphabetic(self):
        self.assertFalse(HangmanHelper.validate_players_letter_choice("123"))

    def test_validate_players_letter_choice_invalid_multiple_letters(self):
        self.assertFalse(HangmanHelper.validate_players_letter_choice("abc"))

    def test_validate_players_letter_choice_valid(self):
        self.assertTrue(HangmanHelper.validate_players_letter_choice("b"))
