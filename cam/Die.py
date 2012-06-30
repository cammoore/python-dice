'''
Created on Jun 29, 2012

@author: ALX
'''
import random


class Die(object):
    '''
    Represents a single six sided dice.
    '''
    val = 1

    def roll(self):
        self.val = random.randint(1, 6)
        return self.val
    
    def get_val(self):
        return self.val

    def __init__(self):
        '''
        Constructor
        '''
        