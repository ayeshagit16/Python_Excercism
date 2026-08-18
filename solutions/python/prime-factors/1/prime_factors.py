'''Compute the prime factors of a given natural number.

A prime number is only evenly divisible by itself and 1.

Note that 1 is not a prime number.
'''
def factors(value):
    '''
    Function to compute the prime factors of a given natural number.
    '''
    res = []
    divisor = 2

    if value == 1:
        return res
    while value > 1:
        if value % divisor == 0:
            value = value / divisor
            res.append(divisor)
        else:
            divisor += 1
    return res
