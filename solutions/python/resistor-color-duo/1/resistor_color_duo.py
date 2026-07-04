'''WAP to build something using Raspberry Pi'''
def value(colors):
    '''The first 2 bands of a resistor have a simple encoding scheme: each color maps to a single number. For example, if they printed a brown band (value 1) followed by a green band (value 5), it would translate to the number 15.'''
    
    color_code = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}
    return int(str(color_code[colors[0]]) + str(color_code[colors[1]]))
