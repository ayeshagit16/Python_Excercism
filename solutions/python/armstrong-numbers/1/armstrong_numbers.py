'''Determine whether a number is an Armstrong number.'''
def is_armstrong_number(number):
    '''
    An Armstrong number is a number that is the sum of its own digits each raised to the power     of the number of digits.
    '''
    number_to_str = str(number)
    num_of_digits = len(number_to_str)
    total = 0

    for digit in number_to_str:
        total += int(digit) ** num_of_digits
    return total == number
