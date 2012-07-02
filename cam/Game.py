'''
Created on Jun 29, 2012

@author: Cam Moore
'''
from cam.Die import Die
from cam.Odds import Odds

class Game(object):
    '''
    classdocs
    '''
    die_one = None
    die_two = None
    last_roll = 0 # the last roll of the dice
    point = 0 # The point that the button is on, 0 means off
    coming_out = True
    odds = None
    pass_line_bet = 0
    pass_line_odds = 0
    place_bets = [0]*11
        
    def point_on(self):
        """Returns True if the point is on."""
        if self.point != 0:
            return True
        return False
    
    def is_craps(self):
        """Returns true if the roll was craps (2, 3, or 12)."""
        total = self.last_roll
        if total == 2 or total == 3 or total == 12:
            return True
        else:
            return False
    
    def is_hard_four(self):
        """Returns True if the roll was a hard four (2, 2)."""
        if self.die_one.val == 2 and self.die_two.val == 2:
            return True
        else:
            return False
        
    def is_hard_six(self):
        """Returns True if the roll was a hard six (3, 3)."""
        if self.die_one.val == 3 and self.die_two.val == 3:
            return True
        else:
            return False
        
    def is_hard_eight(self):
        """Returns True if the roll was a hard eight (4, 4)."""
        if self.die_one.val == 4 and self.die_two.val == 4:
            return True
        else:
            return False
        
    def is_hard_ten(self):
        """Returns True if the roll was a hard ten (5, 5)."""
        if self.die_one.val == 5 and self.die_two.val == 5:
            return True
        else:
            return False
        
    def is_hard_way(self):
        """Returns True if the roll was a hard way."""
        if self.is_hard_four() or self.is_hard_six() or self.is_hard_eight() or \
        self.is_hard_ten():
            return True
        else:
            return False
        
    def is_seven(self):
        """Returns True if the roll was a 7."""
        if self.last_roll == 7:
            return True
        else:
            return False
        
    def is_eleven(self):
        """Returns True if the roll was an 11."""
        if self.last_roll == 11:
            return True
        else:
            return False
        
    def play_pass_line(self, bet):
        """Puts a bet on the pass line. Returns True if point is off, False
        otherwise and no pass line bet."""
        if self.point_on():
            return False
        else:
            self.pass_line_bet = bet 
            return True
    
    def play_pass_line_odds(self, bet):
        """Put odds on the pass line bet. Returns True if able to False otherwise."""
        if self.pass_line_bet > 0:
            self.pass_line_odds += bet
            return True
        else:
            return False
        
    def play_the_number(self, number, bet):
        """Places a bet on the given number."""
        if not self.point_on():
            return False
        else:
            if number != 7 and number < 11 and number > 3:
                self.place_bets[number] = bet 
            return True
    
    def have_place_bets(self):
        """Returns true if there are any place bets."""
        for i in self.place_bets:
            if i != 0:
                return True
        return False
    
    def roll(self, verbose=False, d1_value=None, d2_value=None):
        """Rolls the dice."""
        if d1_value and d2_value:
            self.die_one.val = d1_value
            self.die_two.val = d2_value
            total = d1_value + d2_value
        else:
            total = self.die_one.roll() + self.die_two.roll()
        if self.point == 0:
            self.coming_out = True
        self.last_roll = total
        if self.is_hard_way():
            if verbose:
                print "Roll is hard %s" % total
        else:
            if verbose:
                print "Roll is %s" % total
        if self.point == 0: # button is off
            if self.is_craps():
                if verbose:
                    print "%s Craps %s" % (self.last_roll, self.last_roll)
            if self.is_seven():
                if verbose:
                    print "Seven, Pay the Line"
            if self.is_eleven():
                if verbose:
                    print "Yo, Pay the Line"
            if not self.is_craps() and not self.is_seven() and not self.is_eleven():
                self.point = total
                if verbose:
                    print "Point is %s" % self.point
        else:
            self.coming_out = False
            # check for craps
            if self.is_craps():
                if verbose:
                    print "%s Craps %s" % (self.last_roll, self.last_roll)
            if self.is_seven():
                if verbose:
                    print "Seven Out"
            else: 
                if self.last_roll == self.point:
                    if verbose:
                        print "Pay the line"

    def winnings(self):
        """ Returns any winnings from the last roll."""
        if self.point == 0: # button is off
            if self.is_craps():
                self.pass_line_bet = 0
                self.pass_line_odds = 0  # should already be 0
                return 0
            if self.is_seven():
                self.point = 0 # should already be 0
                self.pass_line_odds = 0 # should already be 0
                return 2 * self.pass_line_bet
            if self.is_eleven():
                self.point = 0 # should already be 0
                return 2 * self.pass_line_bet
            return 0
        else:
            # check for craps
            if self.is_craps():
                return 0
            if self.is_seven():
                self.point = 0
                self.pass_line_bet = 0
                self.pass_line_odds = 0
                self.place_bets = [0]*11
                return 0
            if self.is_eleven():
                return 0
            if self.last_roll == self.point and not self.coming_out:
                winnings = 2 * self.pass_line_bet + self.odds.pass_odds(self.point, self.pass_line_odds) +\
                    self.pass_line_odds + self.odds.place_bet_odds(self.point, self.place_bets[self.point])
                self.point = 0
                return winnings
            return self.odds.place_bet_odds(self.point, self.place_bets[self.point])
        
    def __init__(self):
        '''
        Constructor
        '''
        self.die_one = Die()
        self.die_two = Die()
        self.point = 0
        self.odds = Odds()