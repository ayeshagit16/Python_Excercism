'''Raindrops Challenge'''
def convert(number):
    '''
    Your task is to convert a number into its corresponding raindrop sounds.

    If a given number:

    is divisible by 3, add "Pling" to the result.
    is divisible by 5, add "Plang" to the result.
    is divisible by 7, add "Plong" to the result.
    is not divisible by 3, 5, or 7, the result should be the number as a string.
    '''
    divisible_by_3 = (number%3 == 0)
    divisible_by_5 = (number%5 == 0)
    divisible_by_7 = (number%7 == 0)
    result = ""
    if divisible_by_3:
        result += "Pling"
    if divisible_by_5:
        result += "Plang"
    if divisible_by_7:
        result += "Plong"

    if not result:
        return str(number)
    else:
        return result
