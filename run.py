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