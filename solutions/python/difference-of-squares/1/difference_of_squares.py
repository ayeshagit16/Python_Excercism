def square_of_sum(number):
    '''
    Function to get the square of the sum of the first ten natural            numbers
    '''
    
    square_sum = sum(range(number+1))
    return square_sum ** 2


def sum_of_squares(number):
    '''
    Function to get the sum of the squares of the first ten natural           numbers
    '''
    
    return sum(num**2 for num in range(number+1))
    


def difference_of_squares(number):
    '''
    Difference between the square of the sum of the first ten natural         numbers and the sum of the squares of the first ten natural numbers
    '''
    
    return square_of_sum(number) - sum_of_squares(number)
