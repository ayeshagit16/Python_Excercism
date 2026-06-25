'''Calculate the points scored in a single toss of a Darts game.'''

import math

def score(x, y):
    '''
    Darts is a game where players throw darts at a target.
    If the dart lands outside the target, player earns no points (0 points).
    If the dart lands in the outer circle of the target, player earns 1 point.
    If the dart lands in the middle circle of the target, player earns 5 points.
    If the dart lands in the inner circle of the target, player earns 10 points.
    '''
    distance = math.sqrt((x)**2 + (y)**2)

    if distance <= 1:
        points = 10
    elif distance <= 5:
        points = 5
    elif distance <= 10:
        points = 1
    else:
        points = 0
    return points
        
