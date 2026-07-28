'''
Create a scrabble word game where players place letter tiles on a board to form words. Each letter has a value. A word's score is the sum of its letters' values.
'''

LETTER_VALUES = {
        'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1,
        'l': 1, 'n': 1, 'r': 1, 's': 1, 't': 1,
        'd': 2, 'g': 2,
        'b': 3, 'c': 3, 'm': 3, 'p': 3,
        'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
        'k': 5,
        'j': 8, 'x': 8,
        'q': 10, 'z': 10,
    }

def score(word):
    '''
    Compute a word's Scrabble score by summing the values of its letters.
    '''
    
    return sum(LETTER_VALUES[letter] for letter in word.lower())  
