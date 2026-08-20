'''WORD COUNTER'''
import re
from collections import Counter


def count_words(sentence):
    ''' Count how many times each word occurs in a subtitle of a drama.'''
    words = re.findall(r"[a-zA-Z0-9]+(?:'[a-zA-Z0-9]+)*", sentence.lower())
    return Counter(words)
