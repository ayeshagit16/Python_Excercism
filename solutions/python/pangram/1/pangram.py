import re

def is_pangram(sentence):
    '''
    Figure out if a sentence is a pangram.
    A pangram is a sentence using every letter of the alphabet at least once.
    '''
    compare = set("abcdefghijklmnopqrstuvwxyz")
    letters = "".join(re.findall(r"[A-Za-z]+", sentence))
    return set(letters.lower()) == compare
    
