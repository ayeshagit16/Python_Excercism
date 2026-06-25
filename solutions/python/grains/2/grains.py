def square(number):
    '''The number of grains on a given square'''
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number-1)


def total():
    '''The total number of grains on the chessboard'''
    sqr_count = 1
    res = 0
    total_grains = 0
    while sqr_count < 65:
        res = square(sqr_count)
        total_grains += res
        sqr_count += 1
    return total_grains
