'''dbc.py is such a mess it's easy to build from bottum up'''

from Cards import *
from Players import *
from dbcview import *

if __name__ == '__main__':
    game = True if userStringInput("Do you want to play a game? Y or N", ['Y','N']) == 'Y' else False

    '''Repeat Game loop'''
    while(game):

        print 'playing game'
        opp = userStringInput("Do you want an aggressive (A) opponent or an acquisative (Q) opponent?",['A','Q'])

        p1 = Player('Player 1')
        computer = Player('Computer')
        central = Central()

        central.populatedActive()
        p1.populateHand()
        computer.populateHand()

        initGame()


        x = userStringInput("Play another game?", ['Y','N'])
        if x == 'N':
            game = False

def initGame():
    print 'initing game'
