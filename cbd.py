'''dbc.py is such a mess it's easier to build from bottum up'''
import numpy as np
from Cards import *
from Players import *
from dbcview import *
from dbcmodel import *

if __name__ == '__main__':
    #newgame = True if view_userStringInput("Do you want to play a game? Y or N", ['Y','N']) == 'Y' else False
    newgame = True

    '''Repeat Game loop'''
    while(newgame):

        print 'playing game'
        #opp = view_userStringInput("Do you want an aggressive (A) opponent or an acquisative (Q) opponent?",['A','Q'])
        opp = 'A'

        p1 = Player("Player 1")
        p1.populateHand()

        computer = Player("Computer")
        computer.populateHand()

        central = Central()
        central.populatedActive()

        '''main game loop'''
        game = True
        while game:
            '''player 1 turn'''
            playerTurn = True
            while playerTurn:
                view_displayTurn(p1,computer)

                cardOptions = [str(i) for i in np.arange(len(p1.hand))]
                action = view_userStringInput('Enter Action:',['P','B','A','E','Q'] + cardOptions)

                if action == 'P':
                    p1.playAll()

                elif action.isdigit():
                    p1.playCard(int(action))

                elif action == 'B':
                    buying = True
                    while buying:
                        view_displayBuyOptions(central)
                        buyOptions = [str(i) for i in np.arange(len(central.active))]
                        buyAction = view_userStringInput('Choose Option:',buyOptions+['S','E'])

                        if buyAction == 'E':
                            buying = False

                        elif buyAction == 'S':
                            supp_id = p1.buySupplement(central)
                            view_showSupplementResult(supp_id)

                        elif buyAction.isdigit():
                            buy_id = p1.buyCard(central,int(buyAction))
                            view_showBuyResult(buy_id)

                elif action == 'A':
                    attackValue = p1.willAttack()
                    computer.beenAttacked(attackValue)

                elif action == 'E':
                    p1.endTurn()
                    playerTurn = False

                elif action == 'Q':
                    playerTurn = False
                    game = False



        x = view_userStringInput("Play another game?", ['Y','N'])
        if x == 'N':
            newgame = False
