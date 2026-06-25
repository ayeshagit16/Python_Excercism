'''Create a helpful program so that you don't have to remember the values of the bands.
    These colors are encoded as follows:
    
    black: 0
    brown: 1
    red: 2
    orange: 3
    yellow: 4
    green: 5
    blue: 6
    violet: 7
    grey: 8
    white: 9
'''
def color_code(color):
    '''Return the numerical value associated with a particular color band'''
    color_code = enumerate(colors())
    for num, colr in color_code:
        if color == colr:
            return num


def colors():
    '''List the different band colors'''
    return [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]
