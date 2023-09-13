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
