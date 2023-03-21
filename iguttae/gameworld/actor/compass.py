from enum import Enum

class Compass(Enum):
    '''
    Represents a valid direction in our gameworld's compass
    '''

    NORTH = 0
    '''Compass North'''
    
    NORTHEAST = 1
    '''Compass Northeast'''
    
    EAST = 2
    '''Compass East'''
    
    SOUTHEAST = 3
    '''Compass Southeast'''
    
    SOUTH = 4
    '''Compass South'''
    
    SOUTHWEST = 5
    '''Compass Southwest'''
    
    WEST = 6
    '''Compass West'''
    
    NORTHWEST = 7
    '''Compass Northwest'''
    
    UP = 8
    '''Up, as in "closer to the sky"'''
    
    DOWN = 9
    '''Down, as in "further from the sky"'''
    
    IN = 10
    '''In, as in "towards the inside of something"'''
    
    OUT = 11
    '''Out, as in "towards the outside of something"'''
    
    INVALID = 12
    '''Here just to have some sane known-invalid'''