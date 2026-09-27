'''
Given a name and a number, WAP to produce a sentence using that name and that number as an ordinal numeral.
Rules:

Numbers ending in 1 (unless ending in 11) → "st"
Numbers ending in 2 (unless ending in 12) → "nd"
Numbers ending in 3 (unless ending in 13) → "rd"
All other numbers → "th"
'''

def line_up(name, number):
    '''
    Function to produce the senetence using name and number
    '''
    suffixes = {
        1: "st",
        2: "nd",
        3: "rd",
    }
    if number % 100 in {11, 12, 13}:
        number = str(number) + "th"
    else:
        last_digit = number % 10
        number = str(number) + suffixes.get(last_digit, "th")
    
    return f"{name.capitalize()}, you are the {number} customer we serve today. Thank you!"
