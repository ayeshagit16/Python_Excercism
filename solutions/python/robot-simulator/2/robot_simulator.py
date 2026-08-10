'''
A robot factory's test facility needs a program to verify robot movements.

The robots have three possible movements:

turn right
turn left
advance
'''
# Globals for the directions
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot:
    '''
    Robots are placed on a hypothetical infinite grid, facing a particular direction (north, east, south, or west) at a set of {x,y} coordinates, e.g., {3,8}, with coordinates increasing to the north and east.

The robot then receives a number of instructions, at which point the testing facility verifies the robot's new position, and in which direction it is pointing.

The letter-string "RAALAL" means:
Turn right
Advance twice
Turn left
Advance once
Turn left yet again
    '''
    
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos

    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)
    
    def turn_right(self):
        self.direction = (self.direction + 1) % 4

    def turn_left(self):
        self.direction = (self.direction - 1) % 4

    def advance(self):
        '''Calculate number of advances as per the coordinates and direction'''
        
        moves = {
            NORTH: (0, 1),
            EAST: (1, 0),
            SOUTH: (0, -1),
            WEST: (-1, 0),
        }
        dx, dy = moves[self.direction]
        self.x_pos += dx
        self.y_pos += dy
    
    def move(self, instructions):
        '''Mapping instructions with their associated methods'''

        instruction = {
        "R": self.turn_right,
        "L": self.turn_left,
        "A": self.advance,
        }
        for command in instructions:
            instruction[command]()
