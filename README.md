<b>Hangman game</b>
           

Hangman is a python3 terminal project that let the user or users play the game hangman.

<b>Program features:</b>

 Program first let the user choose game mode, if the user write in 1 it's multiplayer game mode. if the input is not 1 or 2 validation is applied so the program will re ask for input until the input is 1 or 2. With multiplayer game mode the program then asks the user for a word for the other user to guess. The word have to be at least 3 chars and max 12 chars. Validation is applied if the user try to input less than 3 chars or more than 12 or if the word contains illegal non alphabetic charachters like 4 or ! etc.

 If the user instead write in 2 the user chooses singleplayer game mode. In this game mode the computer will randomly choose a word for you. So when choosing this game mode the program then asks the user what difficultly the user want. If the user choose 1 the program will randomly choose a word from a file with easy words. If the user choose 2  the program will randomly choose a word from a file with hard words. 

 When game mode is choosen the program will show the amount of chars the letter have by replaceing the letter with an underscore. Then the program will ask the user for to guess on letter at the time. Validation is applied that checks if the user input is a single letter and its alphabetic and that the letter have not already been guessed. If the guessed letter is not a part of the word to guess the program will count down the amount of guesses the user have that starts at 8. It will also visually show a hanged person with the correspondeing stages depending on what stage of the game the user are at. If the guessed letter is a part of the word to guess the progream will not count down the amount of guesses and it will reaveal the letters by replaceing the underscore with the letter/s. If the amount of guesses is 0 the program will reveal what the word was and the program ends.

<b>Deployment:</b>

The project is deployed at the platform Heroku at the following link:

https://camillath-portfolio-3-hangman.herokuapp.com/

To <b>run the program</b> click on the link above

<b>Dependencies:</b>

No external dependencies like ouath or google sheets is required.

<b>Libs:</b>

Libs that are used : random

<b>credit:</b>

Inspiration taken from the classic game hangman that you often played in school on the whiteboard.

<b>Bugs:</b>

There are no known bugs. But some bugs where discovered and fixed during development.

<b>Validation:</b>

The program validates the user input and raises error if the user input is not legal.

<b>Testing:</b>

Program is well tested the be able to handle sceanrios where the user inputs wrong values.
