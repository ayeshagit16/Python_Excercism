'''Write a program that shows the actual number of eggs in the coop.'''
def egg_count(display_value):
    '''
    Convert the value to binary and count the '1' bits to find the number       of eggs.
    '''
    
    return bin(display_value).count('1')
