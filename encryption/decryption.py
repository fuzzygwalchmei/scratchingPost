import string
from encryption import letter_shift


def word_decrypt(word, shift):
    new_word = []
    shift = 0 - shift
    for letter in word:
        new_word.append(letter_shift(letter, shift))
    
    return ''.join(new_word)