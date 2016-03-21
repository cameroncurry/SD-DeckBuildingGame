from time import sleep
from Player import *

class Computer(Player):

    def __init__(self,aggressive):
        super(Computer,self).__init__("Computer")
        self.aggressive = aggressive


    '''Computer game logic implemented here'''
    def move(self,player,central,view):

        view.displayTurn(self,player)
        sleep(0.5)
        self.playAll()
        view.displayTurn(self,player)
        sleep(0.5)


        view.showComputerActions("Computer attacking with strength %s" % self.attack)
        sleep(0.25)

        attackValue = self.willAttack()
        player.beenAttacked(attackValue)

        view.showComputerActions("Computing Buying Cards")

        if self.money > 0:
            cb = True
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
                            view.showComputerActions("Computer Bought Card")
                            sleep(0.2)
                    else:
                        supp_id = self.buySupplement(central)
                        if supp_id == 0:
                            view.showComputerActions("Supplement Bought")
                            sleep(0.2)

                else:
                    cb = False
                if self.money == 0:
                    cb = False


        view.showComputerActions("Computer Turn Ending")
        self.endTurn()
        sleep(1)
