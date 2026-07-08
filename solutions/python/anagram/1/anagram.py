'''
Given a target word and one or more candidate words, your task is to find the candidates that are anagrams of the target.

An anagram is a rearrangement of letters to form a new word: for example "owns" is an anagram of "snow". A word is not its own anagram: for example, "stop" is not an anagram of "stop"
'''
from collections import Counter
def find_anagrams(word, candidates):
    '''function to find anagrams'''
    
    new_word = Counter(word.lower())
    expected = [item
                for item in candidates
                if word.lower() != item.lower() and new_word == Counter(item.lower())
               ]
    return expected