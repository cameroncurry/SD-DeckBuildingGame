'''dbc.py is such a mess it's easier to build from bottum up'''
import numpy as np
from Cards import *
from Players import *
from Computer import *
from dbcview import *

if __name__ == '__main__':

    view = DBCView()

    #newgame = True if view.userStringInput("Do you want to play a game? Y or N", ['Y','N']) == 'Y' else False
    newgame = True

    '''Repeat Game loop'''
    while(newgame):

        #opp = view.userStringInput("Do you want an aggressive (A) opponent or an acquisative (Q) opponent?",['A','Q'])
        opp = 'A'

        p1 = User("Player 1")
        p1.populateHand()

        computer = Computer(True)
        computer.populateHand()

        central = Central()
        central.populateActive()


        '''main game loop'''
        game = True
        while game:
            '''player 1 turn - returns false if quitting the game'''
            game = p1.move(computer,central,view)

            '''proceed only if user has not quit the game'''
            if game == True:

                '''check if user won before computer moves'''
                if computer.health <= 0:
                    game = False
                    view.displayWinner(p1)

                computer.move(p1,central,view)

                '''check if computer won or draw'''
                if p1.health <= 0:
                    game = False
                    view.displayWinner(computer)

                elif central.activeSize == 0:
                    print "No more cards available"
                    if p1.health > computer.health:
                        print "Player One Wins on Health"
                    elif computer.health > p1.health:
                        print "Computer Wins"
                    else:
                        pHT = 0
                        pCT = 0
                        if pHT > pCT:
                            print "Player One Wins on Card Strength"
                        elif pCT > pHT:
                            print "Computer Wins on Card Strength"
                        else:
                            print "Draw"

        x = view.userStringInput("Play another game?", ['Y','N','Q'])
        if x == 'N' or x == 'Q':
            newgame = False
