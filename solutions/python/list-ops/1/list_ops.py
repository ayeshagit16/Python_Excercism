'''Implement basic list operations.'''
def append(list1, list2):
    '''Given two lists, add all items in the second list to the end of the first list'''
    
    return list1 + list2


def concat(lists):
    '''Given a series of lists, combine all items in all lists into one flattened list'''
    
    new_concat_list = []
    for item in lists:
        if isinstance(item, list):
            new_concat_list.extend(item)
        else:
            new_concat_list.append(item)
    return new_concat_list


def filter(function, list):
    '''Given a predicate and a list, return the list of all items for which predicate(item) is True'''
    
    new_list = []
    for item in list:
        if function(item):
            new_list.append(item)
    return new_list


def length(list):
    '''Given a list, return the total number of items within it'''
    
    count = 0
    for item in list:
        count += 1
    return count


def map(function, list):
    '''Given a function and a list, return the list of the results of applying function(item) on all items'''
    
    new_map_list = []
    res = 0
    for item in list:
        res = function(item)
        new_map_list.append(res)
    return new_map_list

def foldl(function, list, initial):
    '''Given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left'''
    
    foldl_res = initial
    for item in list:
        foldl_res = function(foldl_res, item)
    return foldl_res


def foldr(function, list, initial):
    '''Given a function, a list, and an initial accumulator, fold (reduce) each item into the accumulator from the right'''
    
    foldr_res = initial
    for item in list[::-1]:
        foldr_res = function(foldr_res, item)
    return foldr_res


def reverse(list):
    '''Given a list, return a list with all the original items, but in reversed order'''
    
    return list[::-1]
