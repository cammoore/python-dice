'''
Created on Jun 30, 2012

@author: Cam Moore
'''

class Odds(object):
    '''
    Represents the odds.
    Pass odds: pays at the true odds of 2-to-1 if 4 or 10 is the point, 
            3-to-2 if 5 or 9 is the point, and 6-to-5 if 6 or 8 is the point.
    Come bet odds: pays at the true odds of 2-to-1 if 4 or 10 is the point, 
            3-to-2 if 5 or 9 is the point, and 6-to-5 if 6 or 8 is the point.
    Place bet odds: numbers (4, 10) $5 pays $9, numbers (5, 9) $5 pays $7,
            numbers (6, 8) $6 pays $7
    '''

    def pass_odds(self, point=6, bet=10):
        """Returns the pass odds for the given point and odds bet."""
        if point == 4 or point == 10:
            return 2 * bet
        if point == 5 or point == 9:
            return 3 * (bet / 2)
        if point == 6 or point == 8:
            return 6 * (bet / 5)
        return bet
        
    def come_bet_odds(self, point=6, bet=10):
        """Returns the come bet odds for the given point and odds bet."""
        if point == 4 or point == 10:
            return 2 * bet
        if point == 5 or point == 9:
            return 3 * (bet / 2)
        if point == 6 or point == 8:
            return 6 * (bet / 5)
        return bet

    def place_bet_odds(self, point=6, bet=10):
        """Returns the place bet odds for the given point and odds bet."""
        if point == 4 or point == 10:
            return 9 * (bet / 5)
        if point == 5 or point == 9:
            return 7 * (bet / 5)
        if point == 6 or point == 8:
            return 7 * (bet / 6)
        return bet
        

    def __init__(self):
        '''
        Constructor
        '''
        