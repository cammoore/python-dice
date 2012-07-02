'''
Created on Jul 1, 2012

@author: Cam Moore
'''
from cam.Die import Die

class CrapsGame(object):
    '''
    Simple Craps game. Keeps track of the point and the current roll.
    '''
    die_one = None
    die_two = None
    last_roll = 0 # the last roll of the dice
    previous_point = 0
    current_point = 0 # The point, 0 means off
    pass_line_winner = False
    comming_out = True
    
    def is_button_on(self):
        """Returns True if the button is on."""
        if self.current_point != 0:
            return True
        return False
    
    def is_button_off(self):
        """Returns True if the button is off."""
        return not self.is_button_on()
    
    def is_craps(self):
        """Returns true if the last roll was 2, 3, or 12."""
        if self.last_roll == 2 or self.last_roll == 3 or self.last_roll == 12:
            return True
        else:
            return False

    def is_eleven(self):
        """Returns True if the last roll was an eleven, False otherwise."""
        if self.last_roll == 11:
            return True
        else:
            return False
        
    def is_hard_eight(self):
        """Returns True if the last roll was a hard eight, False otherwise."""
        if self.die_one.val == 4 and self.die_two.val == 4:
            return True
        else:
            return False
        
    def is_hard_four(self):
        """Returns True if the last roll was a hard four, False otherwise."""
        if self.die_one.val == 2 and self.die_two.val == 2:
            return True
        else:
            return False
    
    def is_hard_six(self):
        """Returns True if the last roll was a hard six, False otherwise."""
        if self.die_one.val == 3 and self.die_two.val == 3:
            return True
        else:
            return False
    
    def is_hard_ten(self):
        """Returns True if the last roll was a hard ten, False otherwise."""
        if self.die_one.val == 2 and self.die_two.val == 2:
            return True
        else:
            return False
    
    def is_hard_way(self):
        """Returns True if the last roll was a hard way roll."""
        if self.is_hard_four() or self.is_hard_six() or self.is_hard_eight() or self.is_hard_ten():
            return True
        else:
            return False
        
    def is_point_on(self):
        """Returns True if the point is on, False otherwise."""
        if self.current_point != 0:
            return True
        else:
            return False
    
    def is_seven(self):
        """Returns true if the last roll was a 7."""
        if self.last_roll == 7:
            return True
        else:
            return False
        
    def roll_dice(self, verbose=False, d1_val=None, d2_val=None):
        """Rolls the dice and sets the point, etc.  If verbose prints out what the roll was.
        The value of the dice can be set using d1_val and d2_val."""
        if d1_val and d2_val:
            self.die_one.val = d1_val
            self.die_two.val = d2_val
        else:
            self.die_one.roll()
            self.die_two.roll()
        self.last_roll = self.die_one.val + self.die_two.val
        if verbose:
            if self.is_hard_way():
                print "Roll is hard %s." % self.last_roll
            else:
                print "Roll is %s." % self.last_roll
        if self.current_point == 0:
            # button is off. Check to see if we need to set the button.
            self.comming_out = True
            if self.is_craps():
                self.pass_line_winner = False
                if verbose:
                    print "%s Craps %s." % (self.last_roll, self.last_roll)
            if self.is_seven():
                self.pass_line_winner = True
                if verbose:
                    print "Seven, pay the line."
            if self.is_eleven():
                self.pass_line_winner = True
                if verbose:
                    print "Yo, pay the line."
            if not self.is_craps() and not self.is_seven() and not self.is_eleven():
                self.pass_line_winner = False
                self.previous_point = self.current_point
                self.current_point = self.last_roll
                self.comming_out = False
                if verbose:
                    print "Point is %s." % self.current_point
        else:
            self.comming_out = False
            # p;oint is on
            if self.is_craps():
                self.pass_line_winner = False
                if verbose:
                    print "%s Craps %s." % (self.last_roll, self.last_roll)
            if self.is_seven():
                self.pass_line_winner = False
                self.previous_point = self.current_point
                self.current_point = 0
                self.comming_out = True
                if verbose:
                    print "Seven out."
            if self.is_eleven():
                self.pass_line_winner = False
                if verbose:
                    print "Yo, eleven."
            if self.last_roll == self.current_point:
                self.pass_line_winner = True
                if verbose:
                    print "%s winner, pay the line" % self.last_roll
                self.previous_point = self.current_point
                self.current_point = 0 # button is off
            
            
    def __init__(self):
        '''
        Default Constructor.
        '''
        self.die_one = Die()
        self.die_two = Die()