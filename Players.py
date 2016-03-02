import itertools, random
from Cards import *

centralDeck = list(itertools.chain.from_iterable(
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

playerDeck = list(itertools.chain.from_iterable(
    [8*[Serf()],2*[Squire()]]
    ))

supplementDeck = 10*[Levy()]



class Player(object):
    def __init__(self,name,health=30,deck=playerDeck,hand=[],active=[],handsize=5,discard=[]):
        self.name = name
        self.health = health
        self.deck = deck
        self.hand = hand
        self.active = active
        self.handsize = handsize
        self.discard = discard

    def populateHand(self):
        for i in range(0,self.handsize):
            if(len(self.deck) == 0):
                random.shuffle(self.discard)
                self.deck = self.discard
                self.discard = []

            self.hand.append(self.deck.pop())


class Central(object):
    def __init__(self,active=[],activeSize=5,supplement=supplementDeck,deck=centralDeck):
        self.active = active
        self.activeSize = activeSize
        self.supplement = supplement
        self.deck = deck
        random.shuffle(deck)

    def populatedActive(self):
        for i in range(0,self.activeSize):
            self.active.append(self.deck.pop())


if __name__ == '__main__':
    p = Player("player 1")
