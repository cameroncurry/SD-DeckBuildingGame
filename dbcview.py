
class DBCView:
    def userStringInput(self,prompt, validInputs, complaint="Please Enter Valid Input:", retries=4):
        while True:
            x = raw_input(str(prompt)+"\n")
            if x in validInputs:
                return x
            retries = retries - 1
            if retries < 0:
                raise IOError('refusenik user')
            print complaint,', '.join('{}'.format(i) for i in validInputs)

    def displayTurn(self,P1,P2):

        plyr = "%s's Turn"%P1.name
        print "\n\n%s"%plyr
        print len(plyr)*"-"

        print "\n\t%s Health: %d\t%s Health: %d"%(P1.name,P1.health,P2.name,P2.health)

        print "\n\t\tHand\t\t\tActive Area"
        print "\t\t" + len("Hand")*"-" +"\t\t\t"+len("Active Area")*"-"

        #for i in range(0, max(len(P1.hand), len(central.active))):



        if(len(P1.hand) > 0):
            print 4*" ","Name\tAttack\tMoney"
            for i in range(0,len(P1.hand)):
                card = P1.hand[i]
                print "[%d] %s\t  %s\t  %s"%(i,card.name,card.get_attack(),card.get_money())
        else:
            print "EMPTY"

        print "active"
        for i in range(0,len(P1.active)):
            print P1.active[i].name

        print "Money:",P1.money,"  Attack:",P1.attack
        print "\nChoose Action: (P = play all, [0-n] = play that card, B = Buy Card, A = Attack, E = end turn, Q = quit game)"


    def displayBuyOptions(self,central):
        print "Available Cards"
        for i in range(0,len(central.active)):
            print "[%d]"%i,central.active[i]
        print "Choose a card to buy [0-n], S for supplement, E to end buying"

    def showSupplementResult(self,supp_id):
        if supp_id == 0:
            print "Supplement bought"
        elif supp_id == 1:
            print "Insufficient money to buy"
        elif supp_id == 2:
            print "No Supplement Left"

    def showBuyResult(self,buy_id):
        if buy_id == 0:
            print "Card Bought"
        elif buy_id == 1:
            print "Insufficient money to buy"
