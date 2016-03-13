import itertools, random, numpy as np
from Cards import *

class Player(object):

    def __init__(self,name):
        self.name = name
        self.health = 30
        self.deck = list(itertools.chain.from_iterable([8*[Serf()],2*[Squire()]]))
        self.hand = []
        self.active = []
        self.handsize = 5
        self.discard = []
        self.money = 0
        self.attack = 0

    def move(self):
        pass

    def populateHand(self):
        for i in range(0,self.handsize):
            if(len(self.deck) == 0):
                random.shuffle(self.discard)
                self.deck = self.discard
                self.discard = []
            self.hand.append(self.deck.pop())

    def playAll(self):
        while len(self.hand) > 0:
            self.playCard(0)

    def playCard(self,index):
        card = self.hand.pop(index)
        self.money += card.get_money()
        self.attack += card.get_attack()
        self.active.append(card)

    def willAttack(self):
        value = self.attack
        self.attack = 0
        return value

    def beenAttacked(self,attackValue):
        self.health -= attackValue

    def endTurn(self):
        self.money = 0
        self.attack = 0
        self.discardHand()
        self.discardActive()
        self.populateHand()

    def discardHand(self):
        while len(self.hand) > 0:
            self.discard.append(self.hand.pop())

    def discardActive(self):
        while len(self.active) > 0:
            self.discard.append(self.active.pop())

    '''buySupplement()
    Return 0: supplement was bought
    Return 1: Insufficient money to buy supplement
    Return 2: No supplements left
    '''
    def buySupplement(self,central):
        if len(central.supplement) > 0:
            if self.money >= central.supplement[0].cost:
                self.money -= central.supplement[0].cost
                self.discard.append(central.supplement.pop())
                return 0
            else:
                return 1
        else:
            return 2

    '''buyCard()
    Return 0: card was bought
    Return 1: Insufficient money to buy
    '''
    def buyCard(self,central,index):
        if self.money >= central.active[index].cost:
            self.money -= central.active[index].cost
            self.discard.append(central.active.pop(index))
            if len(central.deck) > 0:
                central.active.append(central.deck.pop())
            else:
                central.activeSize -= 1
            return 0

        else:
            return 1


class User(Player):
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


class Central(object):
    def __init__(self):
        self.active = []
        self.activeSize = 5
        self.supplement = 10*[Levy()]
        self.deck = list(itertools.chain.from_iterable(
                    [
                    4*[Archer()],
                    4*[Baker()],
                    3*[Swordsman()],
                    2*[Knight()],
                    3*[Tailor()],
                    3*[Crossbowman()],
                    3*[Merchant()],
                    4*[Thug()],
                    4*[Thief()],
                    2*[Catapault()],
                    2*[Caravan()],
                    2*[Assassin()]
                    ]))
        random.shuffle(self.deck)

    def populateActive(self):
        for i in range(0,self.activeSize):
            self.active.append(self.deck.pop())
