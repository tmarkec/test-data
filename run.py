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
    while len(letter_word) > 0 and life > 0:
        print(f'you have {life} lives left')
        print(f'you used these:', ' '.join(used_letters))
        list_of_words = [letter if letter in used_letters else ('-') for letter in word]
        print(f'Current word:', ' '.join(list_of_words))
        player_letter = input("Guess letter? \n").upper()
        if player_letter in abc - used_letters:
            used_letters.add(player_letter)
            if player_letter in letter_word:
                clear_screen()
                letter_word.remove(player_letter)
            else:
                clear_screen()
                life -= 1
                print('letter is not in the word')
        elif player_letter in used_letters:
            clear_screen()
            print('Already used that letter')
        else:
            clear_screen()
            print('please try again, with letter')
    if life == 0:
        clear_screen()
        print('You lost the game.')
    else:
        clear_screen()
        print('Well done, you won')


game(word_list)