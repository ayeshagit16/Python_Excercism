def square(number):
    if number not in range(1, 65):
        raise ValueError("square must be between 1 and 64")
    else:
        return 2 ** (number-1)


def total():
    sqr_count = 1
    res = 0
    total = 0
    while sqr_count < 65:
        res = square(sqr_count)
        total += res
        sqr_count += 1
    return total
