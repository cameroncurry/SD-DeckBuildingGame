from Player import *

class User(Player):
    
    '''User's move, will request user input from the view'''
    def move(self, computer, central, view):
        makingMove = True

        while makingMove:
            view.displayTurn(self,computer)
            cardOptions = [str(i) for i in np.arange(len(self.hand))]
            prompt="\nChoose Action:\nP = play all, [0-n] = play that card\nB = Buy Card, A = Attack\nE = end turn, Q = quit game"
            action = view.userStringInput(prompt+'\nEnter Action:',['P','B','A','E','Q'] + cardOptions)

            if action == 'P':
                self.playAll()

            elif action.isdigit():
                self.playCard(int(action))

            elif action == 'B':
                buying = True
                while buying:
                    view.displayBuyOptions(central,self)
                    buyOptions = [str(i) for i in np.arange(len(central.active))]
                    buyAction = view.userStringInput('Choose Option:',buyOptions+['S','E'])

                    if buyAction == 'E':
                        buying = False

                    elif buyAction == 'S':
                        supp_id = self.buySupplement(central)
                        view.showSupplementResult(supp_id)

                    elif buyAction.isdigit():
                        buy_id = self.buyCard(central,int(buyAction))
                        view.showBuyResult(buy_id)

            elif action == 'A':
                attackValue = self.willAttack()
                computer.beenAttacked(attackValue)

            elif action == 'E':
                self.endTurn()
                makingMove = False

            elif action == 'Q':
                return False

        return True
