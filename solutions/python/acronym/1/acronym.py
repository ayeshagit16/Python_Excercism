'''WAP to convert a phrase to its acronym.'''
import re
#import string

def abbreviate(words):
    '''
    Function to generate some jargon by writing a program that converts a     long name like Portable Network Graphics to its acronym (PNG).

    Punctuation is handled as follows: hyphens are word separators (like      whitespace); all other punctuation can be removed from the input.
    '''

    
    #cleaned = words.replace("-", " ")
    #cleaned = cleaned.translate(str.maketrans("", "", string.punctuation))
    #line_split = cleaned.split()
    cleaned = re.split(r"[-_\s]+", words)
    result = ""

    for item in cleaned:
        result += item[0]
    return result.upper()
