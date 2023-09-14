# Import necessary modules and libraries
import os
import random
import ascii_art
from words import word_list
from hangman_pics import HANGMAN_PICS

# Define constants for maximum guesses based on difficulty
MAX_GUESSES_BY_DIFFICULTY = {
    "1": 5,
    "2": 6,
    "3": 8
}

# Define constants for word length based on difficulty
LETTER_COUNT_BY_DIFFICULTY = {
    "1": {
        'min': 3,
        'max': 3
    },
    "2": {
        'min': 4,
        'max': 6
    },
    "3": {
        'min': 7,
        'max': 150
    },
}


# Function to clear the terminal or command prompt screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to get a word based on the chosen difficulty
def get_word(difficulty):
    word_length_config = LETTER_COUNT_BY_DIFFICULTY[difficulty]
    return random.choice([word for word in word_list if word_length_config['min'] <= len(word) <= word_length_config['max']])


# Function to get the difficulty level from the user
def get_difficulty(username):
    print(f"\nChoose a difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    difficulty = input("Enter a number (1/2/3):\n")
    while difficulty not in ["1", "2", "3"]:
        difficulty = input(f"Invalid choice, {username}. Please choose again (1/2/3):\n")
    return difficulty


# Function to handle the main game logic
def play_game(username):
    clear_screen()
    difficulty = get_difficulty(username)
    word = get_word(difficulty).upper()
    guessed = ["_"] * len(word)
    incorrect_guesses = 0
    incorrect_guessed_letters = []

    while "_" in guessed and incorrect_guesses < MAX_GUESSES_BY_DIFFICULTY[difficulty]:
        clear_screen()
        print(HANGMAN_PICS[incorrect_guesses])
        print(" ".join(guessed))
        print(f"Incorrectly guessed letters: {', '.join(incorrect_guessed_letters)}")
        print(f"Attempts left: {MAX_GUESSES_BY_DIFFICULTY[difficulty] - incorrect_guesses}")
        guess = input("Guess a letter:\n").upper()

        if guess in guessed or guess in incorrect_guessed_letters:
            print(f"You've already guessed that letter, {username}. Try again.")
            continue

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            incorrect_guesses += 1
            incorrect_guessed_letters.append(guess)
        clear_screen()
    print(HANGMAN_PICS[incorrect_guesses])
    if "_" not in guessed:
        print(f"Congratulations, {username}! You guessed the word: {word}")
        print(ascii_art.WIN_MESSAGE[0])
    else:
        print(f"Sorry, {username}. You ran out of guesses. The word was: {word}")
        print(ascii_art.GAMEOVER_MESSAGE[0])
    input("\nPress Enter to return to the main menu...\n")


# Function to handle the main menu input from the user
def take_menu_input(username):
    print(f"\nWhat would you like to do?")
    print("1. Start Game")
    print("2. View Rules")
    print("3. Exit Game")

    choice = input("Choose an option (1/2/3):\n")
    if choice not in ["1", "2", "3"]:
        print(f"Invalid choice, {username}. Please choose again.")
        return take_menu_input(username)
    else:
        return choice


# Function to display the game rules
def print_rules():
    clear_screen()
    print(ascii_art.GAME_RULES_MESSAGE[0])


# Main function to run the game
def main():
    print(ascii_art.WELCOME_MESSAGE[0])
    username = input("Enter your username:\n")
    clear_screen()
    print(random.choice([f"Let's have some fun, {username}!",
                         f"Ready to guess, {username}?",
                         f"Can you beat the game, {username}?"]))

    while True:  # Loop to keep the game running until the user chooses to exit
        menu_input = take_menu_input(username)
        if menu_input == "1":
            play_game(username)
        elif menu_input == "2":
            print_rules()
            input("\nPress Enter to return to the main menu...\n")
        elif menu_input == "3":
            print(f"Thanks for playing, {username}! Goodbye!")
            break


# Check to ensure the script is being run directly and not imported
if __name__ == "__main__":
    main()
