def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
        
    factors = [num for num in range(1, number) if number%num == 0]
    total = sum(factors)
    result = "deficient"
    if total == number:
        result = "perfect"
    elif total > number:
        result = "abundant"
    return result
        