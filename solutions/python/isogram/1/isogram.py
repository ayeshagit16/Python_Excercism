'''Determine if a word or phrase is an isogram.'''
#import re
def is_isogram(string):
    '''An isogram (also known as a "non-pattern word") is a word or phrase without a repeating         letter, however spaces and hyphens are allowed to appear multiple times.'''

    result = "".join(alpha for alpha in string.lower() if alpha.isalpha()) # way1
    #result = re.findall('[a-zA-z]', string.lower())    # way2
    phrase = set(result)
    return len(result) == len(phrase)
