'''Determine if a triangle is equilateral, isosceles, or scalene.'''

def check_triangle(func):
    def wrapper(sides):
        a,b,c = sorted(sides)
        if any(side <= 0 for side in (a,b,c)):
            return False
        if a+b <= c:
            return False
        return func((a,b,c))
    return wrapper

@check_triangle
def equilateral(sides):
    '''An equilateral triangle has all three sides the same length.'''

    return sides[0] == sides[1] == sides[2]
    
@check_triangle    
def isosceles(sides):
    '''An isosceles triangle has at least two sides the same length. '''

    return sides[0] == sides[1] or sides[1] == sides[2]

@check_triangle
def scalene(sides):
    '''A scalene triangle has all sides of different lengths.'''
    
    return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]
