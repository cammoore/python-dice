'''
Created on Jun 29, 2012

@author: Cam Moore
'''
import random


class Die(object):
    '''
    Represents a single six sided dice.
    '''
    val = 1

    def roll(self):
        """Rolls the die and sets the value."""
        self.val = random.randint(1, 6)
        return self.val
    
    def get_val(self):
        """Returns the value of the die."""
        return self.val

    def __init__(self):
        '''
        Constructor
        '''
        