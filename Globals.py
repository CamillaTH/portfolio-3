class Globals:
    """
    Global variables that stores information about the game progress
    """

    # max amount of guesses in the game
    max_guesses = 8
    # the amount of guesses the user have guessed
    guesses = 0
    # letters that the user have guessed
    guessed_letters = []
    # the word the user is guessing
    word_to_guess = ""
    # string array that holds the stages visually with 8 stages
    hangman_drawings = ['''
                  ______
                 |
                 |
                 |
                 ''', '''
                  ______
                 |     |
                 |     
                 |  
                   ''', '''
                  ______
                 |     0
                 |     
                 |
                   ''', '''
                  ______
                 |     0
                 |     |
                 |     
                   ''', '''
                  ______
                 |     0
                 |     |--
                 | 
                   ''', '''
                  ______
                 |     0
                 |   --|--
                 |   
                   ''', '''
                  ______
                 |     0
                 |   --|--
                 |     |
                   ''', '''
                  ______
                 |     0
                 |   --|--
                 |    | |  
                   ''']