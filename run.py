import os
import random
import time
from ascii_art import (
    WELCOME_MESSAGE, GAME_RULES_MESSAGE, WIN_MESSAGE, GAMEOVER_MESSAGE
)
from words import word_list
from hangman_pics import HANGMAN_PICS

MAX_GUESSES_BY_DIFFICULTY = {"1": 5, "2": 6, "3": 8}

LETTER_COUNT_BY_DIFFICULTY = {
    "1": {'min': 3, 'max': 3},
    "2": {'min': 4, 'max': 6},
    "3": {'min': 7, 'max': 150},
}


def clear_screen():
    """Clears the terminal or command prompt screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_random_greeting(username):
    """Returns a random greeting message."""
    greetings = [
        f"Let's have some fun, {username}!",
        f"Ready to guess, {username}?",
        f"Can you beat the game, {username}?"
    ]
    return random.choice(greetings)


def get_word(difficulty):
    """Returns a random word based on the chosen difficulty."""
    word_length_config = LETTER_COUNT_BY_DIFFICULTY[difficulty]
    filtered_words = [
        word for word in word_list
        if word_length_config['min'] <= len(word) <= word_length_config['max']
    ]
    return random.choice(filtered_words).upper()


def get_difficulty(username):
    """Prompts user for difficulty level and returns the choice."""
    print("\nChoose a difficulty level:\n1. Easy\n2. Medium\n3. Hard")
    difficulty = input("Enter a number (1/2/3):\n")
    while difficulty not in ["1", "2", "3"]:
        difficulty = input(
            f"Invalid choice, {username}. Please choose again (1/2/3):\n"
        )
    return difficulty


def take_menu_input(username):
    """Prompts user for menu option and returns the choice."""
    menu_options = (
        "\nWhat would you like to do?\n"
        "1. Start Game\n"
        "2. View Rules\n"
        "3. Exit Game"
    )
    print(menu_options)
    choice_prompt = "Choose an option (1/2/3):\n"
    choice = input(choice_prompt)
    invalid_msg = f"Invalid choice, {username}. Please choose again.\n"
    while choice not in ["1", "2", "3"]:
        choice = input(invalid_msg)
    return choice


def print_rules():
    """Displays the game rules."""
    clear_screen()
    print(GAME_RULES_MESSAGE[0])


def play_game(username):
    """Handles the main game logic."""
    clear_screen()
    difficulty = get_difficulty(username)
    word = get_word(difficulty)
    guessed = ["_"] * len(word)
    incorrect_guesses = 0
    incorrect_guessed_letters = []
    max_guesses = MAX_GUESSES_BY_DIFFICULTY[difficulty]

    while "_" in guessed and incorrect_guesses < max_guesses:
        clear_screen()
        print(HANGMAN_PICS[incorrect_guesses])
        print(" ".join(guessed))
        incorrect_letters = ', '.join(incorrect_guessed_letters)
        incorrect_letters_msg = (
            f"Incorrectly guessed letters: {incorrect_letters}"
        )
        print(incorrect_letters_msg)
        attempts_msg = f"Attempts left: {max_guesses - incorrect_guesses}"
        print(attempts_msg)
        guess = input("Guess a letter:\n").upper()

        # Check if the guess is an alphabetical letter
        while not guess.isalpha() or len(guess) != 1:
            guess_msg = "Please enter a valid alphabetical letter:\n"
            guess = input(guess_msg).upper()

        already_guessed_msg = (
            f"You've already guessed that letter, {username}. Try again."
        )
        if guess in guessed or guess in incorrect_guessed_letters:
            print(already_guessed_msg)
            time.sleep(1)
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
        win_msg = f"Congratulations, {username}! You guessed the word: {word}"
        print(win_msg)
        print(WIN_MESSAGE[0])
    else:
        game_over_msg = (
            f"Sorry, {username}. You ran out of guesses. The word was: {word}"
        )
        print(game_over_msg)
        print(GAMEOVER_MESSAGE[0])
    input("\nPress Enter to return to the main menu...\n")


def main():
    """Main function to run the game."""
    print(WELCOME_MESSAGE[0])
    username = input("Enter your username:\n")

    while not username.strip():
        print("No input found. Please enter your username.")
        username = input("Enter your username:\n")
    clear_screen()
    print(get_random_greeting(username))

    while True:
        menu_input = take_menu_input(username)
        if menu_input == "1":
            play_game(username)
        elif menu_input == "2":
            print_rules()
            input("\nPress Enter to return to the main menu...\n")
        elif menu_input == "3":
            print(f"Thanks for playing, {username}! Goodbye!")
            break


if __name__ == "__main__":
    main()
