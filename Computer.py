from Players import *

class Computer(Player):

    def __init__(self,aggressive):
        super(Computer,self).__init__("Computer")
        self.aggressive = aggressive

    def move(self,player,central,view):

        self.playAll()

        print " Computer player values attack %s, money %s" % (self.attack,self.money)
        print " Computer attacking with strength %s" % self.attack
        attackValue = self.willAttack()
        player.beenAttacked(attackValue)

        print "\nPlayer Health %s" % player.health
        print "Computer Health %s" % self.health
        print " Computer player values attack %s, money %s" % (self.attack, self.money)
        print "Computer buying"


        if self.money > 0:
            cb = True
            print "Starting Money %s and cb %s " % (self.money, cb)
            while cb:
                templist = []
                if len(central.supplement) > 0:
                    if central.supplement[0].cost <= self.money:
                        templist.append(("S", central.supplement[0]))
                for intindex in range (0, central.activeSize):
                    if central.active[intindex].cost <= self.money:
                        templist.append((intindex, central.active[intindex]))
                if len(templist) >0:
                    highestIndex = 0
                    for intindex in range(0,len(templist)):
                        if templist[intindex][1].cost > templist[highestIndex][1].cost:
                            highestIndex = intindex
                        if templist[intindex][1].cost == templist[highestIndex][1].cost:
                            if self.aggressive:
                                if templist[intindex][1].get_attack() >templist[highestIndex][1].get_attack():
                                    highestIndex = intindex
                            else:
                                if templist[intindex][1].get_attack() >templist[highestIndex][1].get_money():
                                    highestIndex = intindex
                    source = templist[highestIndex][0]

                    if source in range(0,5):
                        buy_id = self.buyCard(central,int(source))
                        if buy_id == 0:
                            print "Computer bought card"
                    else:
                        supp_id = self.buySupplement(central)
                        if supp_id == 0:
                            print 'Supplement Bought'

                else:
                    cb = False
                if self.money == 0:
                    cb = False
        else:
            print "No Money to buy anything"


        print "Computer turn ending"
        self.endTurn()
