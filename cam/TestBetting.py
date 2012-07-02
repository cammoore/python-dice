'''
Created on Jul 1, 2012

@author: cmoore
'''
import unittest
from cam.Betting import Betting
from cam.CrapsGame import CrapsGame


class TestBetting(unittest.TestCase):


    def setUp(self):
        self.betting = Betting(CrapsGame())


    def testSimple(self):
        self.betting.play_pass_line(5)
        self.betting.game.roll_dice(d1_val=4, d2_val=3)
        self.assertTrue(self.betting.game.is_seven(), "msg")
        self.assertEqual(10, self.betting.check_winnings(), "msg")
        self.assertFalse(self.betting.play_come_bet(5), "msg")
        self.assertEqual(10, self.betting.check_winnings(), "msg")
        
    def testPassLine(self):
        self.betting.play_pass_line(5)
        self.betting.game.roll_dice(d1_val=4, d2_val=3)
        self.assertEqual(10, self.betting.check_winnings(), "got %s not 10" % self.betting.check_winnings())
        self.betting.play_pass_line(5)
        self.betting.game.roll_dice(d1_val=4, d2_val=2)
        self.betting.play_pass_line_odds(10)
        self.betting.game.roll_dice(d1_val=4, d2_val=2)
        self.assertEqual(5 + 5 + 10 + 12, self.betting.check_winnings(), "32 != %s" % self.betting.check_winnings())
        
        
    def testCraps(self):
        self.betting.play_pass_line(5)
        self.betting.game.roll_dice(d1_val=1, d2_val=2)
        self.assertTrue(self.betting.game.is_craps(), "msg")
        self.assertEqual(0, self.betting.check_winnings(), "msg")
        self.assertEqual(0, self.betting.pass_line_bet, "msg")
        
    def testPlaceBets(self):
        self.betting.play_pass_line(5)
        self.betting.game.roll_dice(d1_val=1, d2_val=5)
        self.betting.place_the_number(8, 6)
        self.betting.game.roll_dice(d1_val=5, d2_val=3)
        self.assertEqual(7, self.betting.check_winnings(), "msg")
        
    def testComeBets(self):
        self.betting.play_pass_line(5)
        self.betting.game.roll_dice(verbose=True, d1_val=1, d2_val=5)
        self.betting.play_pass_line_odds(10)
        self.betting.play_come_bet(5)
        self.betting.game.roll_dice(verbose=True, d1_val=2, d2_val=5)
        self.assertEqual(10, self.betting.check_winnings(), "msg")
        self.assertFalse(self.betting.play_come_bet(5), "msg")
        self.betting.game.roll_dice(verbose=True, d1_val=1, d2_val=5)
        self.assertEqual(0, self.betting.check_winnings(), "msg")
        self.assertTrue(self.betting.play_come_bet(5), "msg")
        self.betting.game.roll_dice(verbose=True, d1_val=1, d2_val=3)
        self.assertEqual(0, self.betting.check_winnings(), "msg")        
        self.assertTrue(self.betting.play_come_bet_odds(4, 10), "msg")
        self.betting.game.roll_dice(verbose=True, d1_val=2, d2_val=2)
        self.assertEqual(40, self.betting.check_winnings(verbose=True), "expected 40 got %s" % self.betting.check_winnings())        
      
    def testPlaceAndPass(self):
        self.betting.play_pass_line(5)
        self.betting.game.roll_dice(verbose=True, d1_val=1, d2_val=5)
        self.betting.check_winnings(verbose=True)
        self.betting.play_pass_line_odds(10)
        self.betting.place_the_number(4, 5)
        self.betting.place_the_number(5, 5)
        self.betting.place_the_number(8, 6)
        self.betting.place_the_number(9, 5)
        self.betting.place_the_number(10, 5)
        self.betting.game.roll_dice(verbose=True, d1_val=1, d2_val=4)
        self.betting.check_winnings(verbose=True)
        self.betting.game.roll_dice(verbose=True, d1_val=2, d2_val=4)
        self.assertEqual(32, self.betting.check_winnings(verbose=True), "got %s" % self.betting.check_winnings())
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()