'''Take a nested array of any depth and return a fully flattened array.'''


def flatten(iterable):
    '''Falttening a deeply nested array containing null values as None'''
    flattened_list = []

    for item in iterable:
        if item is None:
            continue
        elif isinstance(item, list):
            flattened_list.extend(flatten(item))
        else:
            flattened_list.append(item)

    return flattened_list
