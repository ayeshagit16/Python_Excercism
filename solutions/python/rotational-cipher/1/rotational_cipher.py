'''WAP to create an implementation of the rotational cipher, also sometimes called the Caesar cipher.'''

import string


def rotate(text, key):
    '''
    The Caesar cipher is a simple shift cipher that relies on transposing all the letters in the alphabet using an integer key between 0 and 26. Using a key of 0 or 26 will always yield the same output due to modular arithmetic. The letter is shifted for as many values as the value of the key.

The general notation for rotational ciphers is ROT + <key>. The most commonly used rotational cipher is ROT13.
    '''
    lower_letters = list(string.ascii_lowercase)
    upper_letters = list(string.ascii_uppercase)
    new_text = ''
    for letter in text:
        if letter in lower_letters:
            new_index = (lower_letters.index(letter) + key) % 26
            new_text += lower_letters[new_index]
        elif letter in upper_letters:
            new_index = (upper_letters.index(letter) + key) % 26
            new_text += upper_letters[new_index]
        else:
            new_text += letter
    return new_text
