from enum import Enum

class Verbosity(Enum):
    '''
    Represents how verbose something should be
    '''

    # TODO: Add silent mode
    SILENT          = 0
    
    # TODO: Add superbrief mode
    SUPERBRIEF      = 250
    
    # TODO: Add brief mode
    BRIEF           = 500
    
    VERBOSE         = 750
    '''
    Default mode.
    
    Show text every time we enter a place, show list of items,
    don't show item descriptions or character descriptions
    '''
    
    # TODO: Add Superverbose Mode
    SUPERVERBOSE    = 1000