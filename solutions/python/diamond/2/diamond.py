'''Given a letter, it prints a diamond starting with 'A', with the supplied letter at the widest point.'''
def rows(letter):
    '''
    The diamond kata takes as its input a letter, and outputs it in a diamond     shape.
    '''
    letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
    target_index = letters.index(letter)
    top_half = []
    for current_index in range(target_index + 1):
        current_letter = letters[current_index]
        leading_spaces = target_index - current_index
        inner_space = 2 * current_index - 1
        if current_letter == 'A':
            row = ' ' * leading_spaces + current_letter + ' ' * leading_spaces
            top_half.append(row)
        else:
            row = ' ' * leading_spaces + current_letter + ' ' * inner_space +                     current_letter + ' ' * leading_spaces
            top_half.append(row)
    botton_half = top_half[-2::-1]
    return top_half + botton_half
