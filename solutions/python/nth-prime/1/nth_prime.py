'''Given a number n, determine what the nth prime is.'''

from math import isqrt

def prime(number):
    '''
    Determine the nth prime number by checking if it divisible by any number other than 1 and itself.
    Checking till the square root is enough because every composite number has at least one factor no greater than its square root.
    '''
    
    if number < 1:
        raise ValueError("there is no zeroth prime")

    num = 1
    prime_nums = []

    while len(prime_nums) < number:
        prime_flag = True
        num += 1
        for item in range(2, isqrt(num) + 1):
            if num % item == 0:
                prime_flag = False
                break
        if prime_flag:
            prime_nums.append(num)

    return prime_nums[-1]   
