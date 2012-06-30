'''
Created on Jun 29, 2012

@author: Cam Moore
'''
from cam.Game import Game
from cam.Die import Die

foo = Game()
d1 = Die()

if __name__ == '__main__':
    g = foo
    for i in range(1, 30):
        g.roll()
