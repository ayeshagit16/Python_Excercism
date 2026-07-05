'''WAP to build label using  Raspberry pi'''
def label(colors):
    '''
    In Resistor Color Duo you decoded the first two colors. For instance: orange-orange got the main value 33. The third color stands for how many zeros need to be added to the main value. The main value plus the zeros gives us a value in ohms.
    '''
    color_code = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}
    resistor_color = int(f"{color_code[colors[0]]}{color_code[colors[1]]}")
    resistor_value = resistor_color * pow(10, color_code[colors[2]])
    if resistor_value >= 1000000000:
        resistor_value = f"{resistor_value/1000000000:g} gigaohms"
    elif resistor_value < 1000000000 and resistor_value >= 1000000:
        resistor_value = f"{resistor_value/1000000:g} megaohms"
    elif resistor_value < 1000000 and resistor_value >= 1000:
        resistor_value = f"{resistor_value/1000:g} kiloohms"
    else:
        resistor_value = f"{resistor_value} ohms"
    return resistor_value
