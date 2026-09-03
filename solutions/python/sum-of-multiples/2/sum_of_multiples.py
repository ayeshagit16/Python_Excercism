'''
Write the code that calculates the energy points that get awarded to players when they complete a level.
'''

def sum_of_multiples(limit, multiples):
    '''
    The energy points are awarded according to the following rules:

    For each magical item, take the base value and find all the multiples     of that value that are less than the level number.
    Combine the sets of numbers.
    Remove any duplicates.
    Calculate the sum of all the numbers that are left.
    '''
    
    multiples_list = []
    res = 0
        
    for num in multiples:
        if num == 0:
            continue
        multiples_list.append(set(range(num, limit, num)))

    if len(multiples_list) >= 1:
        res = sum(set.union(*multiples_list))
    return res
