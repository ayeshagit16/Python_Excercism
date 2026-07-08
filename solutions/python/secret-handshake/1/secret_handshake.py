'''Secret Handshake Problem'''
def commands(binary_str):
    '''
    Your task is to convert a number between 1 and 31 to a sequence of actions in the secret handshake.

The sequence of actions is chosen by looking at the rightmost five digits of the number once it's been converted to binary. Start at the right-most digit and move left.

The actions for each number place are:

00001 = wink
00010 = double blink
00100 = close your eyes
01000 = jump
10000 = Reverse the order of the operations in the secret handshake
    '''
    actions_map = ["wink", "double blink", "close your eyes", "jump"]
    actions = [
        action
        for bit, action in zip(binary_str[-1:-5:-1], actions_map)
        if bit == "1"
    ]
    if len(binary_str) == 5 and binary_str[0] == "1":
        actions.reverse()
    return actions
