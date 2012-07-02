'''
Created on Jun 30, 2012

@author: cmoore
'''
import unittest
from cam.Game import Game


class TestGame(unittest.TestCase):
    """Test cases for the Game class."""
    
    def setUp(self):
        """Sets up the tests."""
        self.game = Game()

    def testName(self):
        self.game.play_pass_line(5)
        self.game.roll(d1_value=1, d2_value=3)
        self.assertEqual(True, self.game.coming_out, "msg")
        self.assertEqual(0, self.game.winnings(), "msg")
        self.game.roll(d1_value=3, d2_value=1)
        self.assertEqual(10, self.game.winnings(), "Expected 10 got %s" % self.game.winnings())
    
    def testHardways(self):
        # set hard four
        self.game.roll(d1_value=2, d2_value=2)
        self.assertTrue(self.game.is_hard_four(), "didn't get hard 4")
        self.game.roll(d1_value=3, d2_value=1)
        self.assertFalse(self.game.is_hard_four(), "Got hard 4 when not")
        # set hard six
        self.game.roll(d1_value=3, d2_value=3)
        self.assertTrue(self.game.is_hard_six(), "didn't get hard 6")
        self.game.roll(d1_value=5, d2_value=1)
        self.assertFalse(self.game.is_hard_six(), "Got hard 6 when not")
        # set hard eight
        self.game.roll(d1_value=4, d2_value=4)
        self.assertTrue(self.game.is_hard_eight(), "didn't get hard 8")
        self.game.roll(d1_value=3, d2_value=5)
        self.assertFalse(self.game.is_hard_eight(), "Got hard 8 when not")
        # set hard ten
        self.game.roll(d1_value=5, d2_value=5)
        self.assertTrue(self.game.is_hard_ten(), "didn't get hard 10")
        self.game.roll(d1_value=6, d2_value=4)
        self.assertFalse(self.game.is_hard_ten(), "Got hard 10 when not")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()