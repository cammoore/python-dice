'''
Created on Jul 1, 2012

@author: cmoore
'''
from cam.Odds import Odds

class Betting(object):
    '''
    Represents the different bets on a Craps table for a single player.
    '''
    pass_line_bet = 0
    pass_line_odds = 0
    place_bets = [0] * 11
    come_bet = 0
    come_bets = [0] * 11
    come_bets_odds = [0] * 11
    game = None
    o = None
    
    def play_pass_line(self, bet):
        """Places a bet on the pass line. Returns True if the bet is placed, False otherwise."""
        if self.game.is_point_on():
            return False
        else:
            self.pass_line_bet = bet
            return True
            
    def play_pass_line_odds(self, bet):
        """Places odds on the pass line. Return True if pass line is bet, False otherwise."""
        if self.game.is_point_on() and self.pass_line_bet != 0:
            self.pass_line_odds = bet
            return True
        else:
            return False
    
    def remove_pass_line_odds(self):
        """Returns the pass line odds and sets them to 0."""
        o = self.pass_line_odds
        self.pass_line_odds = 0
        return o
    
    def place_the_number(self, number, bet):
        """Places a bet on the given number. Returns True if bet placed, False otherwise."""
        if self.game.is_point_on() and number != 7 and number < 11 and number > 3:
            self.place_bets[number] = bet
            return True
        return False
    
    def remove_place_bet(self, number):
        """Returns the place bet and sets it to 0."""
        if number != 7 and number < 11 and number > 3:
            b = self.place_bets[number]
            self.place_bets[number] = 0
            return b
        return 0
    
    def have_place_bets(self):
        """Returns True if there are any place bets, False otherwise."""
        if sum(self.place_bets) > 0:
            return True
        return False
    
    def play_come_bet(self, bet):
        """Places a come bet. Returns True if bet is placed, False otherwise."""
        if self.game.is_point_on() and self.come_bet == 0:
            self.come_bet = bet
            return True
        return False
    
    def play_come_bet_odds(self, number, odds):
        """Places odds on come bet at number. Returns True if bet is placed, False otherwise."""
        if number > 3 and number != 7 and number < 11 and self.come_bets[number] != 0:
            self.come_bets_odds[number] = odds
            return True
        return False
    
    def remove_come_bet_odds(self, number):
        """Returns the come bet odds and sets it to 0."""
        if number > 3 and number != 7 and number < 11:
            o = self.come_bets_odds[number]
            self.come_bets_odds[number] = 0
            return o
        return 0
        
    def clear_pass_line(self):
        """Clears all pass line bets."""
        self.pass_line_bet = 0
        self.pass_line_odds = 0

    def clear_place_bets(self):
        """Clears all place bets."""
        self.place_bets = [0]*11
        
    def clear_come_bets(self):
        """Clears all come bets."""
        self.come_bets = [0] * 11
        self.come_bets_odds = [0] * 11
        
    def show_bets(self):
        """Returns a string representation of the current bets."""
        ret = "Pass line (%s): %s, odds %s\n" % (self.game.current_point, self.pass_line_bet, self.pass_line_odds)
        for i in [4, 5, 6, 8, 9, 10]:
            ret += ' [p%s' % i + ':  %s]' % self.place_bets[i]
        ret += '\n'
        for i in [4, 5, 6, 8, 9, 10]:
            ret += ' [c%s' % i + ':  %s odds %s]' % (self.come_bets[i], self.come_bets_odds[i])        
        return ret    
    
    def check_winnings(self, verbose=False):
        """Returns any winnings from the game's last roll. Updates Come bets."""
        g = self.game     
#        last_roll = g.last_roll
        if g.is_button_off() and g.previous_point == 0:
            # button off and previously off
            if g.is_craps():
                if verbose:
                    print "Off, Craps pass line loses."
                self.clear_pass_line()
                self.come_bet = 0 # should be 0 already
                # nothing happens to place or come bets
                return 0
            if g.is_seven():
                # rolled seven pay the line
                self.pass_line_odds = 0 # should already be 0
                # clear come bets
                self.clear_come_bets()
                # nothing happens to place bets
                # rolled 7, pay the line
                w = 2 * self.pass_line_bet
                if verbose:
                    print "Off, Seven pay the line %s" % w
                return w
            
            if g.is_eleven():
                # rolled 11, pay the line
                w = 2 * self.pass_line_bet
                if verbose:
                    print "Off, Yo, pay the line %s" % w
                return w
        if g.is_button_off() and not g.pass_line_winner:
            # just rolled a seven out
            if verbose:
                print "Seven out. Clear line, come and place bets. Pay the come bet"
            # clear pass line
            self.clear_pass_line()
            # clear place bets
            self.clear_place_bets()
            # clear any come bets
            self.clear_come_bets()
            # pay come bet
            w = 2 * self.come_bet
            self.come_bet = 0
            return w
        if g.is_button_off() and g.pass_line_winner:
            # just rolled the previous point
            if verbose:
                print "%s winner pay the line." % g.last_roll
            # have a roll, pay existing come bets and place bets
            # pay any existing come bets
            pay_pass = 0
            pay_come = 0
            pay_place = 0
            w = 0
            if g.last_roll != 7 and g.last_roll != 11:
                w = self.o.come_bet_odds(g.last_roll, self.come_bets_odds[g.last_roll]) +\
                    self.come_bets_odds[g.last_roll] + 2 * self.come_bets[g.last_roll]
                if w > 0:
                    pay_come = w
                self.come_bets[g.last_roll] = 0
                # move come bet to number
                self.come_bets[g.last_roll] = self.come_bet
                # pay existing place bets
                if not g.comming_out:
                    pay_place = self.o.place_bet_odds(g.last_roll, self.place_bets[g.last_roll])
                    w += pay_place
                
            if g.pass_line_winner:
                # add pass line win
                pay_pass = 2 * self.pass_line_bet + self.o.pass_odds(g.last_roll, self.pass_line_odds) + self.pass_line_odds
                w += pay_pass
            if verbose:
                print "Roll %s paying pass %s, come %s, place %s" % (g.last_roll, pay_pass, pay_come, pay_place)
            return w
            
        if g.is_button_on():
            # button is on
            if g.is_craps():
                if verbose:
                    print "Craps Come bet loses."
                # clear come bet
                self.come_bet = 0
                # only pay craps bet
                return 0
            if g.is_seven():
                if verbose:
                    print "Seven out. Clear line, come and place bets. Pay the come bet"
                # come bet wins
                w = 2 * self.come_bet
                self.come_bet = 0
                # clear pass line
                self.clear_pass_line()
                # place bets lose
                self.clear_place_bets()
                # existing come bets lose
                self.clear_come_bets()
                return w
            if g.is_eleven():
                if verbose:
                    print "Yo, pay come bet."
                # only come bet wins
                w = 2 * self.come_bet
                self.come_bet = 0
                return w
            
            # have a roll, pay existing come bets and place bets
            # pay any existing come bets
            pay_pass = 0
            pay_come = 0
            pay_place = 0
            w = self.o.come_bet_odds(g.last_roll, self.come_bets_odds[g.last_roll]) +\
                self.come_bets_odds[g.last_roll] + 2 * self.come_bets[g.last_roll]
            if w > 0:
                pay_come = w
            self.come_bets[g.last_roll] = 0
            # move come bet to number
            self.come_bets[g.last_roll] = self.come_bet
            # pay existing place bets
            if not g.comming_out:
                pay_place = self.o.place_bet_odds(g.last_roll, self.place_bets[g.last_roll])
                w += pay_place
                
            if g.pass_line_winner:
                # add pass line win
                pay_pass = 2 * self.pass_line_bet + self.o.pass_odds(g.last_roll, self.pass_line_odds)
                w += pay_pass
            if verbose:
                print "Roll %s paying pass %s, come %s, place %s" % (g.last_roll, pay_pass, pay_come, pay_place)
            return w
                
    def __init__(self, game):
        '''
        Constructor
        '''
        self.game = game
        self.o = Odds()
        