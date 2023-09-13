import os
import random
import ascii_art 
from words import word_list
from hangman_pics import HANGMAN_PICS

MAX_GUESSES_BY_DIFFICULTY = {
    "1": 5,
    "2": 6,
    "3": 8
}

LETTER_COUNT_BY_DIFFICULTY = {
    "1": {
        'min': 3,
        'max': 3
    },
    "2": {
        'min': 4,
        'max': 6
    },
    "3":{
        'min': 7,
        'max': 150
    },
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_word(difficulty):
    word_length_config = LETTER_COUNT_BY_DIFFICULTY[difficulty]
    return random.choice([word for word in word_list if word_length_config['min'] <= len(word) <= word_length_config['max']])

def get_difficulty(username):
    print(f"\nHello, {username}! Choose a difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    difficulty = input("Enter a number (1/2/3):\n")
    while difficulty not in ["1", "2", "3"]:
        difficulty = input(f"Invalid choice, {username}. Please choose again (1/2/3):\n")
    return difficulty

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
    else:
        print(f"Sorry, {username}. You ran out of guesses. The word was: {word}")
    input("\nPress Enter to return to the main menu...\n")

def take_menu_input(username):
    clear_screen()
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

def print_rules():
    clear_screen()
    print(ascii_art.GAME_RULES_MESSAGE[0])    

def main():
    print(ascii_art.WELCOME_MESSAGE[0])
    username = input("Enter your username:\n")
    clear_screen()
    print(random.choice([f"Let's have some fun, {username}!", f"Ready to guess, {username}?", f"Can you beat the game, {username}?"]))

    while True:  # This loop will keep the game running until the user chooses to exit
        menu_input = take_menu_input(username)
        if menu_input == "1":
            play_game(username)
        elif menu_input == "2":
            print_rules()
            input("\nPress Enter to return to the main menu...\n")  # This will pause the screen until the user presses Enter
        elif menu_input == "3":
            print(f"Thanks for playing, {username}! Goodbye!")
            break  # This will exit the loop and end the game

if __name__ == "__main__":
    main()