import itertools, random
from Cards import *

'''Class representing the central line'''
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
