'''
Created on Jul 2, 2012

@author: Cam Moore
'''
from cam.CrapsGame import CrapsGame
from cam.Betting import Betting
from statlib import stats


if __name__ == '__main__':
    game = CrapsGame()
    across = Betting(game)
    six_eight = Betting(game)
    come = Betting(game)
    stake1 = 100
    stake2 = 100
    stake3 = 100
    line_bet = 5
    line_odds = 10
    atm1 = 0
    atm2 = 0
    atm3 = 0
    stakes1 = []
    stakes2 = []
    stakes3 = []
    atms1 = []
    atms2 = []
    atms3 = []
    profits1 = []
    profits2 = []
    profits3 = []
    debug = False
    
    
    for j in range(1, 20):
        stake1 = 100
        stake2 = 100
        stake3 = 100
        atm1 = 0
        atm2 = 0
        atm3 = 0
        num_come_bets = 0
        for i in range(1, 50):
            # Do the banking first
            if stake1 < 42: # need more money
                stake1 += 100
                atm1 += 100
            if stake1 > 250: # deposit some of our winnings
                stake1 -= 100
                atm1 -= 100
            # Do the banking first
            if stake2 < 27: # need more money
                stake2 += 100
                atm2 += 100
            if stake2 > 250: # deposit some of our winnings
                stake2 -= 100
                atm2 -= 100
            # Do the banking first
            if stake3 < 20: # need more money
                stake3 += 100
                atm3 += 100
            if stake3 > 250: # deposit some of our winnings
                stake3 -= 100
                atm3 -= 100
            # play the line
            if stake1 > line_bet and game.is_button_off:
                if across.play_pass_line(line_bet):
                    stake1 -= line_bet
                    if debug:
                        print "Across: pass line bet %s" % line_bet
            # play the line
            if stake2 > line_bet and game.is_button_off:
                if six_eight.play_pass_line(line_bet):
                    stake2 -= line_bet
                    if debug:
                        print "6_8: pass line bet %s" % line_bet
            # play the line
            if stake3 > line_bet and game.is_button_off:
                if come.play_pass_line(line_bet):
                    stake3 -= line_bet
                    if debug:
                        print "Come: pass line bet %s" % line_bet
            # play pass line odds
            if stake1 > line_odds and game.is_button_on() and across.pass_line_odds == 0:
                if across.play_pass_line_odds(line_odds):
                    stake1 -= line_odds
                    if debug:
                        print "Across: pass line odds %s" % line_odds
            # play pass line odds
            if stake2 > line_odds and game.is_button_on() and six_eight.pass_line_odds == 0:
                if six_eight.play_pass_line_odds(line_odds):
                    stake2 -= line_odds
                    if debug:
                        print "6_8: pass line odds %s" % line_odds
            # play pass line odds
            if stake3 > line_odds and game.is_button_on() and come.pass_line_odds == 0:
                if come.play_pass_line_odds(line_odds):
                    stake3 -= line_odds
                    if debug:
                        print "Come: pass line odds %s" % line_odds
            # do the extra betting
            have_place1 = across.have_place_bets()
            if stake1 > 27 and game.is_button_on() and not have_place1:
                for i in [4, 5, 6, 8, 9, 10]:
                    if i != 6 and i != 8 and i != game.current_point:
                        across.place_the_number(i, 5)
                        stake1 -= 5
                    if i != game.current_point and (i == 6 or i == 8):
                        across.place_the_number(i, 6)
                        stake1 -= 6
                if debug:
                    print "Across: placing across, stake = %s" % stake1 
            have_place2 = six_eight.have_place_bets()
            if stake2 > 12 and game.is_button_on() and not have_place2:
                for i in [6, 8]:
                    if i != game.current_point:
                        six_eight.place_the_number(i, 6)
                        stake2 -= 6
                if debug:
                    print "6_8: placing 6 and 8, stake = %s" % stake2 
            if stake3 > line_bet and num_come_bets < 3:
                if come.play_come_bet(line_bet):
                    num_come_bets += 1
                    stake3 -= line_bet
                    if debug:
                        print "Come: come bet %s stake = %s" % (line_bet, stake3)
#            print "Across:"
#            print across.show_bets()
#            print "\n6_8:"
#            print six_eight.show_bets()
#            print "\nCome:"
#            print come.show_bets()
            # Roll the dice    
            game.roll_dice(verbose=False)
#            print "before winnings s1 = %s, s2 = %s, s3 = %s" % (stake1, stake2, stake3)
            # Check the winnings
            win1 = across.check_winnings(verbose=False)
            if win1:
                stake1 += win1
            win2 = six_eight.check_winnings(verbose=False)
            if win2:
                stake2 += win2
            win3 = come.check_winnings(verbose=False)
            if win3:
                stake3 += win3
#            print "Roll<%s> s1 = %s, s2 = %s, s3 = %s" % (i, stake1, stake2, stake3)
            # make sure all come bets have odds
            for c_b in come.come_bets_wo_odds():
                if come.play_come_bet_odds(c_b, line_odds):
                    stake3 -= line_odds
                    if debug:
                        print "Come: come bet odds of %s on %s" % (line_odds, c_b)
            num_come_bets = come.num_come_bets()
            
        print "Ending Profits p1: %d, p2: %d p3: %d" % ((stake1 - atm1), (stake2 - atm2), (stake3 - atm3))
        profits1.append(stake1 - atm1)
        profits2.append(stake2 - atm2)
        profits3.append(stake3 - atm3)
       
#    print "Stake (min, mean, max) = (%s, %s, %s)" % (min(stakes), stats.mean(stakes), max(stakes))
#    print "ATM (min, mean, max) = (%s, %s, %s)" % (min(atms), stats.mean(atms), max(atms))
    print "Profits1 (min, mean, max) = (%s, %s, %s)" % (min(profits1), stats.mean(profits1), max(profits1))
    print "Profits2 (min, mean, max) = (%s, %s, %s)" % (min(profits2), stats.mean(profits2), max(profits2))
    print "Profits3 (min, mean, max) = (%s, %s, %s)" % (min(profits3), stats.mean(profits3), max(profits3))
