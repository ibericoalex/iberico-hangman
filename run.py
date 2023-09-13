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
