import random
from words import word_list
import string
import os

def get_word(word_list):
    words = random.choice(word_list)
    return words.upper()


def clear_screen():
    """
    Clear the console.
    numlines is an optional argument used only as a fall-back.
    """
    if os.name == "posix":
        # Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system('CLS')
    else:
        # Fallback for other operating systems.
        print('\n' * numlines)


def game(word_list):
    word = get_word(word_list)
    letter_word = set(word)
    abc = set(string.ascii_uppercase)
    used_letters = set()
    life = 5
    

game(word_list)