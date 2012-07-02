'''
Created on Jun 29, 2012

@author: Cam Moore
'''
from cam.Game import Game
from cam.Odds import Odds
from statlib import stats

if __name__ == '__main__':
    g = Game()
    o = Odds()
    stake = 100
    line_bet = 5
    line_odds = 10
    atm = 0
    stakes = []
    atms = []
    profits = []

    for j in range(1, 50):    
        stake = 100
        atm = 0
        for i in range(1, 50):
            if stake < line_bet:
                stake += 100
                atm += 100
            if stake > 250:
                # bank 100
                stake -= 100
                atm -= 100
            # place line bet if we can
            if stake >= line_bet:
                if g.play_pass_line(line_bet):
                    stake -= line_bet
            # place the line odds if we can
            if stake >= line_odds and g.point_on() and g.pass_line_odds == 0:
                g.play_pass_line_odds(line_odds)
                stake -= line_odds
            # place place bets if we can
            p_on = g.point_on()
            have_place = g.have_place_bets()
            if stake >= 32 and p_on and not have_place:
#                print "Playing across"
                for i in [4, 5, 6, 8, 9, 10]:
                    if i != 6 and i != 8 and i != g.point:
                        g.play_the_number(i, 5)
                        stake -= 5
                    if i != g.point and (i == 6 or i == 8):
                        g.play_the_number(i, 6)
                        stake -= 6
#           print "Stake = %s" % stake
            g.roll(verbose=False)
            win = g.winnings()
#            print "rolled %s won $%s" % (g.last_roll, win)
            if win:
                stake += win
        print "Ending Stake = %s, ATM withdraws = %s" % (stake, atm)
        stakes.append(stake)
        atms.append(atm)
        profits.append(stake - atm)

    print "Stake (min, mean, max) = (%s, %s, %s)" % (min(stakes), stats.mean(stakes), max(stakes))
    print "ATM (min, mean, max) = (%s, %s, %s)" % (min(atms), stats.mean(atms), max(atms))
    print "Profits (min, mean, max) = (%s, %s, %s)" % (min(profits), stats.mean(profits), max(profits))
    hist = stats.histogram(profits)
    stake_bins = hist[0]
    stake_start = hist[1]
    stake_width = hist[2]
    print "Profits histogram:"
    for b in stake_bins:
        print "%s - %s: %s" % (stake_start, stake_start + stake_width, b)
        stake_start += stake_width
    a_hist = stats.histogram(atms)
    a_bins = a_hist[0]
    a_start = a_hist[1]
    a_width = a_hist[2]
#    print "ATM histogram:"
    for a in a_bins:
#        print "%s - %s: %s" % (a_start, a_start + a_width, a)
        a_start += a_width
