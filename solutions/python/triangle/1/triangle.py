'''Determine if a triangle is equilateral, isosceles, or scalene.'''
def equilateral(sides):
    '''An equilateral triangle has all three sides the same length.'''
    side_1 = sides[0]
    side_2 = sides[1]
    side_3 = sides[2]
    if side_1 > 0 and side_2 > 0 and side_3 >0:
        if (side_1+side_2)>= side_3 and (side_2+side_3)>=side_1 and (side_1+side_3)>=side_2:
            return side_1 == side_2 == side_3
    return False
    
def isosceles(sides):
    side_1 = sides[0]
    side_2 = sides[1]
    side_3 = sides[2]
    if side_1 > 0 and side_2 > 0 and side_3 >0:
        if (side_1+side_2)>= side_3 and (side_2+side_3)>=side_1 and (side_1+side_3)>=side_2:
            return side_1 == side_2 or side_1 == side_3 or side_2 == side_3
    return False


def scalene(sides):
    side_1 = sides[0]
    side_2 = sides[1]
    side_3 = sides[2]
    if side_1 > 0 and side_2 > 0 and side_3 >0:
        if (side_1+side_2)>= side_3 and (side_2+side_3)>=side_1 and (side_1+side_3)>=side_2:
            return side_1 != side_2 and side_1 != side_3 and side_2 != side_3
    return False
