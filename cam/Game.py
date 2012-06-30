'''
Created on Jun 29, 2012

@author: Cam Moore
'''
from cam.Die import Die

class Game(object):
    '''
    classdocs
    '''
    die_one = None
    die_two = None
    point = 0 # The point that the button is on, 0 means off
    
    def roll_num(self):
        """Returns the value of the role as an Integer."""
        return self.die_one.val + self.die_two.val
    
    def is_craps(self):
        """Returns true if the roll was craps (2, 3, or 12)."""
        total = self.roll_num()
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
        if self.roll_num() == 7:
            return True
        else:
            return False
        
    def is_eleven(self):
        """Returns True if the roll was an 11."""
        if self.roll_num() == 11:
            return True
        else:
            return False 
    
    def roll(self):
        """Rolls the dice."""
        total = self.die_one.roll() + self.die_two.roll()
        if self.is_hard_way():
            print "Roll is hard %s" % total
        else:
            print "Roll is %s" % total
        if self.point == 0: # button is off
            if self.is_craps():
                print "%s Craps %s" % (self.roll_num(), self.roll_num())
            if self.is_seven():
                print "Seven, Pay the Line"
            if self.is_eleven():
                print "Yo, Pay the Line"
            if not self.is_craps() and not self.is_seven():
                self.point = total
                print "Point is %s" % self.point
        else:
            # check for craps
            if self.is_seven():
                print "Seven Out"
                self.point = 0
            else: 
                if self.roll_num() == self.point:
                    print "Pay the line"
                    self.point = 0

    def __init__(self):
        '''
        Constructor
        '''
        self.die_one = Die()
        self.die_two = Die()
        self.point = 0