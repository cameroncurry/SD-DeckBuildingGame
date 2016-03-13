
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
        print "\n\n\n%s"%plyr
        print len(plyr)*"-"

        print "\n\t\t\t%s Health: %d\n\t\t\t%s Health: %d"%(P1.name,P1.health,P2.name,P2.health)

        print "\n\t\tHand", "\t\t\t   Active Area"
        print "\t\t" + len("Hand")*"-", "\t\t\t   " + len("Active Area")*"-"

        print 5*" "+"Name\tAttack\tMoney", "\t\tName\t\tAttack\tMoney"

        for i in range(0, max(len(P1.hand), len(P1.active))):
            if(i<len(P1.hand)):
                card = P1.hand[i]
                print " [%d] %s\t  %s\t  %s"%(i,card.name,card.get_attack(),card.get_money()),
            else:
                print "\t\t\t",

            if(i<len(P1.active)):
                card = P1.active[i]
                print "\t\t%s \t\t  %s\t  %s"%(card.name,card.get_attack(),card.get_money())
            else:
                print

        print "\n\t\t\tMoney:",P1.money,"  Attack:",P1.attack

    def displayBuyOptions(self,central,P1):
        print "\n\n\tAvailable Cards\t\tMoney available: %d"%P1.money
        print "\t",len("Available Cards")*"-"
        print "Name\t\tCost\tAttack\tMoney"
        for i in range(0,len(central.active)):
            card = central.active[i]
            print "[%d] %s\t %s\t %s\t  %s"%(i,card.name,card.cost,card.get_attack(),card.get_money())

        print "\nSupplement"
        print len("Supplement")*"-"
        if len(central.supplement) > 0:
            card = central.supplement[0]
            print "[S] %s\t %s\t %s\t  %s"%(card.name,card.cost,card.get_attack(),card.get_money())
        else:
            print "EMPTY"

        print "\nChoose a card to buy [0-n], S for supplement, E to end buying"

    def showSupplementResult(self,supp_id):
        if supp_id == 0:
            print "\n\nSupplement bought"
        elif supp_id == 1:
            print "\n\nInsufficient money to buy"
        elif supp_id == 2:
            print "\n\nNo Supplement Left"

    def showBuyResult(self,buy_id):
        if buy_id == 0:
            print "\n\nCard Bought"
        elif buy_id == 1:
            print "\n\nInsufficient money to buy"

    def showComputerActions(self,prompt):
        print "\n\t\t"+prompt+""
