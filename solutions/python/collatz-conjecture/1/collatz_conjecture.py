'''
Given a positive integer, return the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture.
'''
def steps(number):
    '''
    Collatz Conjecture, a puzzle that has baffled thinkers for decades.

    The rules were deceptively simple. Pick any positive integer.

    If it's even, divide it by 2.
    If it's odd, multiply it by 3 and add 1.
    Then, repeat these steps with the result, continuing indefinitely.
    '''
    count = 0
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    
    if number == 1:
        return 0
    
    while number != 1:
        if number%2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        count += 1    
    return count