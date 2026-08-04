'''Calculate the square root of a given number.'''
def square_root(number):
    '''
    Function to calculate the square root of a given number using               Successive approximation using Newton's or Heron's method.
    '''
    
    guess = number / 2
    
    while guess * guess != number:
        guess = (guess + number / guess) / 2
    return guess
