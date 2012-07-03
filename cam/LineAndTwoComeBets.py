'''
Created on Jul 2, 2012

@author: Cam Moore
'''
from cam.CrapsGame import CrapsGame
from cam.Betting import Betting
from statlib import stats


if __name__ == '__main__':
    g = CrapsGame()
    b = Betting(g)
    stake = 100
    line_bet = 5
    line_odds = 10
    atm = 0
    stakes = []
    atms = []
    profits = []
    debug = True
    
    
    for j in range(1, 2):
        stake = 100
        atm = 0
        num_come_bets = 0
        for i in range(1, 50):
            # Do the banking first
            if stake < line_bet: # need more money
                stake += 100
                atm += 100
            if stake > 250: # deposit some of our winnings
                stake -= 100
                atm -= 100
            # play the line
            if stake > line_bet and g.is_button_off:
                if b.play_pass_line(line_bet):
                    stake -= line_bet
                    if debug:
                        print "pass line bet %s" % line_bet
            if stake > line_odds and g.is_button_on() and b.pass_line_odds == 0:
                if b.play_pass_line_odds(line_odds):
                    stake -= line_odds
                    if debug:
                        print "pass line odds %s" % line_odds
            if stake > line_bet and num_come_bets < 3:
                if b.play_come_bet(line_bet):
                    num_come_bets += 1
                    stake -= line_bet
                    if debug:
                        print "come bet %s" % line_bet    
            g.roll_dice(verbose=debug)
            for c_b in b.come_bets_wo_odds():
                if b.play_come_bet_odds(c_b, line_odds):
                    stake -= line_odds
                    if debug:
                        print "come bet odds of %s on %s" % (line_odds, c_b)
            
            num_come_bets = b.num_come_bets()
            
            if debug:
                print b.show_bets()
            win = b.check_winnings(verbose=debug)
            if win:
                stake += win
            if debug:
                print "Roll %s stake = %s" % (i, stake)

        print "Ending Stake = %s, ATM withdraws = %s" % (stake, atm)
        stakes.append(stake)
        atms.append(atm)
        profits.append(stake - atm)
       
#    print "Stake (min, mean, max) = (%s, %s, %s)" % (min(stakes), stats.mean(stakes), max(stakes))
#    print "ATM (min, mean, max) = (%s, %s, %s)" % (min(atms), stats.mean(atms), max(atms))
    print "Profits (min, mean, max) = (%s, %s, %s)" % (min(profits), stats.mean(profits), max(profits))
    hist = stats.histogram(profits)
    stake_bins = hist[0]
    stake_start = hist[1]
    stake_width = hist[2]
    print "Profits histogram:"
    for b in stake_bins:
        print "%s - %s: %s" % (stake_start, stake_start + stake_width, b)
        stake_start += stake_width
