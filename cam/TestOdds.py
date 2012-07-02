'''
Created on Jun 30, 2012

@author: Cam Moore
'''
import unittest
from cam.Odds import Odds


class TestOdds(unittest.TestCase):
    """Test cases for the Odds class."""

    def setUp(self):
        """Sets up the tests."""
        self.odds = Odds()
        
    def test_place_bet_odds(self):
        """Tests the place bet odds."""
        bet = 5
        payout = 9
        point = 4
        self.assertEqual(payout, self.odds.place_bet_odds(point, bet), 
                         "Expecting %s got %s" % (payout, self.odds.place_bet_odds(point, bet)))
        point = 10
        self.assertEqual(payout, self.odds.place_bet_odds(point, bet), 
                         "Expecting %s got %s" % (payout, self.odds.place_bet_odds(point, bet)))
        payout = 7
        point = 5
        self.assertEqual(payout, self.odds.place_bet_odds(point, bet), 
                         "Expecting %s got %s" % (payout, self.odds.place_bet_odds(point, bet)))
        point = 9
        self.assertEqual(payout, self.odds.place_bet_odds(point, bet), 
                         "Expecting %s got %s" % (payout, self.odds.place_bet_odds(point, bet)))
        bet = 6
        point = 6
        self.assertEqual(payout, self.odds.place_bet_odds(point, bet), 
                         "Expecting %s got %s" % (payout, self.odds.place_bet_odds(point, bet)))
        point = 8
        self.assertEqual(payout, self.odds.place_bet_odds(point, bet), 
                         "Expecting %s got %s" % (payout, self.odds.place_bet_odds(point, bet)))
        bet = 5
        payout = 0
        self.assertEqual(payout, self.odds.place_bet_odds(point, bet), 
                         "Expecting %s got %s" % (payout, self.odds.place_bet_odds(point, bet)))
        bet = 7
        payout = 7
        self.assertEqual(payout, self.odds.place_bet_odds(point, bet), 
                         "Expecting %s got %s" % (payout, self.odds.place_bet_odds(point, bet)))
        
        
        
    def test_pass_odds(self):
        """Test the pass odds."""
        bet = 10
        payout = 20
        point = 4
        self.assertEqual(payout, self.odds.pass_odds(point, bet),
                         "Expecting %s got %s" % (payout, self.odds.pass_odds(point, bet)))
        point = 10
        self.assertEqual(payout, self.odds.pass_odds(point, bet),
                         "Expecting %s got %s" % (payout, self.odds.pass_odds(point, bet)))
        payout = 15
        point = 5
        self.assertEqual(payout, self.odds.pass_odds(point, bet),
                         "Expecting %s got %s" % (payout, self.odds.pass_odds(point, bet)))
        point = 9
        self.assertEqual(payout, self.odds.pass_odds(point, bet),
                         "Expecting %s got %s" % (payout, self.odds.pass_odds(point, bet)))
        payout = 12
        point = 6
        self.assertEqual(payout, self.odds.pass_odds(point, bet),
                         "Expecting %s got %s" % (payout, self.odds.pass_odds(point, bet)))
        point = 8
        self.assertEqual(payout, self.odds.pass_odds(point, bet),
                         "Expecting %s got %s" % (payout, self.odds.pass_odds(point, bet)))
        payout = 10
        point = 7
        self.assertEqual(payout, self.odds.pass_odds(point, bet),
                         "Expecting %s got %s" % (payout, self.odds.pass_odds(point, bet)))
        bet = 5
        payout = 6
        point = 5
        self.assertEqual(payout, self.odds.pass_odds(point, bet),
                         "Expecting %s got %s" % (payout, self.odds.pass_odds(point, bet)))
        point = 6
        self.assertEqual(payout, self.odds.pass_odds(point, bet),
                         "Expecting %s got %s" % (payout, self.odds.pass_odds(point, bet)))
        bet = 4
        payout = 0
        self.assertEqual(payout, self.odds.pass_odds(point, bet),
                         "Expecting %s got %s" % (payout, self.odds.pass_odds(point, bet)))
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
