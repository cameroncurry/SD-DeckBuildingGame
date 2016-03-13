'''
All game cards are implemented here

Changes made:
Each card type is now a subclass of Card
clan field has been taken out of the card class as it is not used in the game
'''

class Card(object):
    def __init__(self, name, values=(0, 0), cost=1):
        self.name = name
        self.cost = cost
        self.values = values
    def __str__(self):
                return 'Name %s costing %s with attack %s and money %s' % (self.name, self.cost, self.values[0], self.values[1])
    def get_attack(self):
        return self.values[0]
    def get_money(self):
            return self.values[1]

class Archer(Card):
    def __init__(self):
        self.name = 'Archer'
        self.cost = 2
        self.values = (3,0)

class Assassin(Card):
    def __init__(self):
        self.name = 'Assassin'
        self.cost = 4
        self.values = (5,0)

class Baker(Card):
    def __init__(self):
        self.name = 'Baker'
        self.cost = 2
        self.values = (0,3)

class Caravan(Card):
    def __init__(self):
        self.name = 'Caravan'
        self.cost = 5
        self.values = (1,5)

class Catapault(Card):
    def __init__(self):
        self.name = 'Catapault'
        self.cost = 6
        self.values = (7,0)

class Crossbowman(Card):
    def __init__(self):
        self.name = 'Crossbowman'
        self.cost = 3
        self.values = (4,0)

class Knight(Card):
    def __init__(self):
        self.name = 'Knight'
        self.cost = 5
        self.values = (6,0)

class Levy(Card):
    def __init__(self):
        self.name = 'Levy'
        self.cost = 2
        self.values = (1,2)

class Merchant(Card):
    def __init__(self):
        self.name = 'Merchant'
        self.cost = 4
        self.values = (0,5)

class Serf(Card):
    def __init__(self):
        self.name = 'Serf'
        self.cost = 0
        self.values = (0,1)

class Squire(Card):
    def __init__(self):
        self.name = 'Squire'
        self.cost = 0
        self.values = (1,0)

class Swordsman(Card):
    def __init__(self):
        self.name = 'Swordsman'
        self.cost = 3
        self.values = (4,0)

class Tailor(Card):
    def __init__(self):
        self.name = 'Tailor'
        self.cost = 3
        self.values = (0,4)

class Thief(Card):
    def __init__(self):
        self.name = 'Thief'
        self.cost = 1
        self.values = (1,1)

class Thug(Card):
    def __init__(self):
        self.name = 'Thug'
        self.cost = 1
        self.values = (2,0)
