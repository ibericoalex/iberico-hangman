import os
import random
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
    difficulty = input("Enter a number (1/2/3): ")
    while difficulty not in ["1", "2", "3"]:
        difficulty = input(f"Invalid choice, {username}. Please choose again (1/2/3): ")
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
        print(f"Incorrectly guessed letters, {username}: {', '.join(incorrect_guessed_letters)}")
        print(f"Attempts left, {username}: {MAX_GUESSES_BY_DIFFICULTY[difficulty] - incorrect_guesses}")
        guess = input("Guess a letter: ").upper()

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

    print(HANGMAN_PICS[incorrect_guesses])
    if "_" not in guessed:
        print(f"Congratulations, {username}! You guessed the word: {word}")
    else:
        print(f"Sorry, {username}. You ran out of guesses. The word was: {word}")