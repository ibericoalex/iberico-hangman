# **Hangman Challenge - Portfolio Project 3**

This is a Python terminal game of Hangman. The game allows users to guess letters of a word until they either guess the entire word correctly or run out of attempts. The number of attempts is determined by the difficulty level chosen by the user.

Live deployment - [Hangman Challenge](heroku-link)

![Website mockup](./documentation/mock-up.png)

## How to play

Upon starting the game, users are prompted to enter their username. They are then greeted with a random greeting message and presented with a menu where they can choose to start the game, view the game rules, or exit the game.

When starting the game, users choose a difficulty level: Easy, Medium, or Hard. The difficulty level determines the number of attempts allowed and the length of the word to be guessed.

During the game, users are shown a series of underscores representing the letters of the word. They can guess one letter at a time. Correct guesses reveal the letter in the word, while incorrect guesses decrease the number of attempts left. The game provides feedback on incorrectly guessed letters and the number of attempts remaining.

The game ends when the user guesses the word correctly or runs out of attempts. After the game ends, users can choose to play again or return to the main menu.

## UX
### Site Purpose:
To offer a digital rendition of the classic hangman game, allowing users to test their word-guessing skills against the computer.

### Audience:
Targeted at individuals who enjoy word games and are looking for a quick and engaging game to pass the time.

### Communication:
The game provides clear instructions and feedback to the user at every step, ensuring a smooth and intuitive gameplay experience.

### Current User Goals:
To enjoy a game of hangman, choosing from various difficulty levels, and aiming to guess the word before running out of attempts.

### New User Goals:
To familiarize themselves with the game mechanics and enjoy a few rounds of hangman.

### Future Goals:
To introduce more features such as multiplayer mode, a hint system, and a wider variety of words.

## Flowchart
Before diving into the coding process, I created a flowchart to provide a clear roadmap for the program's implementation. This chart effectively outlines the program's structure, pinpointing areas for user input, system input validation, and the handling of any incorrect inputs.

![Flowchart](./documentation/mock-up.png)
## Features

### Existing Features
- Main Menu:
    - The game starts with a main menu that allows users to start the game, view the rules, or exit.

- Gameplay:
    - Once the game starts, users are prompted to guess letters to uncover a hidden word. They have a limited number of incorrect guesses, after which the game ends.

- Difficulty Levels:
    - Users can choose from three difficulty levels: easy, medium, or hard. Each level has its own set of word lengths and allowed incorrect guesses.

- User Input: Users can enter their username and choose a difficulty level.
- Random Word Selection: The game selects a random word based on the chosen difficulty level.
- Dynamic Feedback: The game provides feedback on guessed letters, remaining attempts, and incorrectly guessed letters.
- ASCII Art: The game uses ASCII art for welcome messages, game rules, win messages, and game over messages.
- Replayability: Users can play the game multiple times and choose different difficulty levels.
### Future Features
- Leaderboard: Implement a leaderboard to track and display top scores.
- Hints: Provide hints to users during the game.
- Multiplayer Mode: Allow multiple users to play against each other.
- Colors: Use a color scheme to distinguish specific areas of the text. 
- A wider variety of words and categories to choose from.

## Testing
### Validator Testing
- [CI PEP8 Online](https://pep8ci.herokuapp.com/). 
   - No errors were returned.
![PEP8 CI Validation](documentation/python-linter.png)

### Manual Testing
- Various tests were conducted to ensure the game runs smoothly and handles different user inputs gracefully
- Tested on my local terminal and the Code Institute Heroku terminal

## Bugs
### Solved Bugs
**Requirements.txt:** When I used the pip3 freeze > requirements.txt command, it generated the following list of dependencies:
![dependencies](documentation/heroku-dependencies.png)

However, when deploying to Heroku, I encountered the following error:
![dependencies](documentation/bug-heroku.png)

**Solution:** To resolve this issue, I had to manually edit the **requirements.txt** file and replace the section - **six @ file:///AppleInternal/BuildRoot/Library/Caches/com.apple.xbs/Sources/python3/python3-103/six-1.15.0-py2.py3-none-any.whl** with **six==1.15.0**. This adjustment ensured that the dependencies were correctly deployed to Heroku without errors.

### Remaining Bugs
- No remaining bugs