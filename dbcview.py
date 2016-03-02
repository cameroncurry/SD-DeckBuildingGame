
def view_userStringInput(prompt, validInputs, complaint="Please Enter Valid Input:", retries=4):
    while True:
        x = raw_input(str(prompt)+"\n")
        if x in validInputs:
            return x
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint,', '.join('{}'.format(i) for i in validInputs)

def view_displayTurn(player,computer):
    print player.name, "Health", player.health
    print computer.name, "Health", computer.health
    print player.name,'Hand'
    for i in range(0,len(player.hand)):
        print "[%d]"%i,player.hand[i]
    print "Money:",player.money,"  Attack:",player.attack
    print "\nChoose Action: (P = play all, [0-n] = play that card, B = Buy Card, A = Attack, E = end turn, Q = quit game)"


def view_displayBuyOptions(central):
    print "Available Cards"
    for i in range(0,len(central.active)):
        print "[%d]"%i,central.active[i]
    print "Choose a card to buy [0-n], S for supplement, E to end buying"

def view_showSupplementResult(supp_id):
    if supp_id == 0:
        print "Supplement bought"
    elif supp_id == 1:
        print "Insufficient money to buy"
    elif supp_id == 2:
        print "No Supplement Left"

def view_showBuyResult(buy_id):
    if buy_id == 0:
        print "Card Bought"
    elif buy_id == 1:
        print "Insufficient money to buy"
