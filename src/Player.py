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

    '''abstract move method'''
    '''not necessarily used as subclasses require arguments to move,
    but implemented to show that any additional Player type will be assumed to implement some move method'''
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

    '''when ending a turn player loses accumulated money and attack
    also discard the current hand and populates a new hand from the deck'''
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

    '''hand strength is the sum of attack & money values in hand'''
    def handStrength(self):
        strength = 0
        for card in self.hand:
            strength += card.get_attack + card.get_money
        return strength

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
