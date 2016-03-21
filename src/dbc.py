from Cards import *
from Computer import *
from User import *
from Central import *
from DBCView import *

if __name__ == '__main__':

    view = DBCView()

    view.welcome()

    newgame = True if view.userStringInput("Do you want to play a game? Y or N", ['Y','N']) == 'Y' else False

    '''Loop to play a new game'''
    while(newgame):

        if view.userStringInput("Do you want an aggressive (A) opponent or an acquisative (Q) opponent?",['A','Q']) == 'A':
            aggressive = True
        else:
            aggressive = False

        p1 = User("Player 1")
        p1.populateHand()

        computer = Computer(aggressive)
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
                    game = False
                    if p1.health > computer.health:
                        view.displayWinner(p1,"Wins on Health - No Cards Remaining in Game")
                    elif computer.health > p1.health:
                        view.displayWinner(computer,"Wins on Health - No Card Remaining in Game")
                    else:
                        if p1.handStrength() > computer.handStrength():
                            view.displayWinner(p1,"Wins on Card Strength - No Card Remaining in Game")
                        elif computer.handStrength() > p1.handStrength():
                            view.displayWinner("Wins on Card Strength - No Card Remaining in Game")
                        else:
                            view.displayWinner(None)

        x = view.userStringInput("Play another game?", ['Y','N','Q'])
        if x == 'N' or x == 'Q':
            newgame = False
