import itertools, random

from Cards import *
from Players import *
from dbcview import *
from cbd import *

if __name__ == '__main__':

    pO = {'name': 'player one', 'health': 30, 'deck': None, 'hand': None, 'active': None, 'handsize': 5,
                 'discard': None}

    pC = {'name': 'player computer', 'health': 30, 'deck': None, 'hand': None, 'active': None, 'handsize': 5,
               'discard': None}


    central = {'name': 'central', 'active': None, 'activeSize': 5, 'supplement': None, 'deck': None}

    sdc = [
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
        ]

    playeronedeck = [8*[Serf()],2*[Squire()]]


    pod = list(itertools.chain.from_iterable(playeronedeck))
    pO['deck'] = pod
    pO['hand'] = []
    pO['discard'] = []
    pO['active'] = []


    playertwodeck = [8*[Serf()], 2*[Squire()]]

    ptd = list(itertools.chain.from_iterable(playertwodeck))
    pC['deck'] = ptd
    pC['hand'] = []
    pC['discard'] = []
    pC['active'] = []

    supplement = 10*[Levy()]
    deck = list(itertools.chain.from_iterable(sdc))
    random.shuffle(deck)
    central['deck'] = deck
    central['supplement'] = supplement
    central['active'] = []

    #populate central active
    max = central['activeSize']
    count = 0
    while count < max:
        card = central['deck'].pop()
        central['active'].append(card)
        count = count + 1


    #player.populateHand
    for x in range(0, pO['handsize']):
        if (len(pO['deck']) == 0):
            random.shuffle(pO['discard'])
            pO['deck'] = pO['discard']
            pO['discard'] = []

        card = pO['deck'].pop()
        pO['hand'].append(card)

    for x in range(0, pO['handsize']):
        if len(pC['deck']) == 0:
            random.shuffle(pO['discard'])
            pC['deck'] = pC['discard']
            pC['discard'] = []
        card = pC['deck'].pop()
        pC['hand'].append(card)

    print "Available Cards"
    for card in central['active']:
        print card

    print "Supplement"
    if len(central['supplement']) > 0:
        print central['supplement'][0]

    view = DBCView()

    pG = view.userStringInput('Do you want to play a game? Y or N', ['Y','N'])
    cG = (pG=='Y')

    if(cG):
        oT = view.userStringInput("Do you want an aggressive (A) opponent or an acquisative (Q) opponent?",['A','Q'])
        aggressive = (oT=='A')

    while cG:
        money = 0
        attack = 0
        while True:

            print "\nPlayer Health %s" % pO['health']
            print "Computer Health %s" % pC['health']

            print "\nYour Hand"
            index = 0
            for card in pO['hand']:
                    print "[%s] %s" % (index, card)
                    index = index + 1
            print "\nYour Values"
            print "Money %s, Attack %s" % (money, attack)
            print "\nChoose Action: (P = play all, [0-n] = play that card, B = Buy Card, A = Attack, E = end turn)"

            act = raw_input("Enter Action: ")
            print act
            if act == 'P':
                if(len(pO['hand'])>0):
                    for x in range(0, len(pO['hand'])):
                        card = pO['hand'].pop()
                        pO['active'].append(card)
                        money = money + card.get_money()
                        attack = attack + card.get_attack()

                print "\nYour Hand"
                index = 0
                for card in pO['hand']:
                    print "[%s] %s" % (index, card)
                    index = index + 1

                print "\nYour Active Cards"
                for card in pO['active']:
                    print card
                print "\nYour Values"
                print "Money %s, Attack %s" % (money, attack)
            if act.isdigit():
                if( int(act) < len(pO['hand'])):
                    pO['active'].append(pO['hand'].pop(int(act)))
                    for card in pO['active']:
                        money = money + card.get_money()
                        attack = attack + card.get_attack()
                print "\nYour Hand"
                index = 0
                for card in pO['hand']:
                    print "[%s] %s" % (index, card)
                    index = index + 1

                print "\nYour Active Cards"
                for card in pO['active']:
                    print card
                print "\nYour Values"
                print "Money %s, Attack %s" % (money, attack)
            if (act == 'B'):

                notending = True
                while money > 0:
                    print "Available Cards"
                    ind = 0
                    for card in central['active']:
                        print "[%s] %s" % (ind,card)
                        ind = ind + 1
                    print "Choose a card to buy [0-n], S for supplement, E to end buying"
                    bv = raw_input("Choose option: ")
                    if bv == 'S':
                        if len(central['supplement']) > 0:
                            if money >= central['supplement'][0].cost:
                                money = money - central['supplement'][0].cost
                                pO['discard'].append(central['supplement'].pop())
                                print "Supplement Bought"
                            else:
                                print "insufficient money to buy"
                        else:
                            print "no supplements left"
                    elif bv == 'E':
                        notending = False
                        break;
                    elif bv.isdigit():
                        if int(bv) < len(central['active']):
                             if money >= central['active'][int(bv)].cost:
                                money = money - central['active'][int(bv)].cost
                                pO['discard'].append(central['active'].pop(int(bv)))
                                if( len(central['deck']) > 0):
                                    card = central['deck'].pop()
                                    central['active'].append(card)
                                else:
                                    central['activeSize'] = central['activeSize'] - 1
                                print "Card bought"
                             else:
                                print "insufficient money to buy"
                        else:
                             print "enter a valid index number"
                    else:
                        print "Enter a valid option"


            if act == 'A':
                pC['health'] = pC['health'] - attack
                attack = 0
            if act == 'E':
                if (len(pO['hand']) >0 ):
                    for x in range(0, len(pO['hand'])):
                        pO['discard'].append(pO['hand'].pop())


                if (len(pO['active']) >0 ):
                    for x in range(0, len(pO['active'])):
                        pO['discard'].append(pO['active'].pop())
                for x in range(0, pO['handsize']):
                    if len(pO['deck']) == 0:
                        random.shuffle(pO['discard'])
                        pO['deck'] = pO['discard']
                        pO['discard'] = []
                    card = pO['deck'].pop()
                    pO['hand'].append(card)
                break

        print "Available Cards"
        for card in central['active']:
            print card

        print "Supplement"
        if len(central['supplement']) > 0:
            print central['supplement'][0]

        print "\nPlayer Health %s" % pO['health']
        print "Computer Health %s" % pC['health']

        '''COMPUTER STARTS HERE'''

        money = 0
        attack = 0
        for x in range(0, len(pC['hand'])):
                        card = pC['hand'].pop()
                        pC['active'].append(card)
                        money = money + card.get_money()
                        attack = attack + card.get_attack()

        print " Computer player values attack %s, money %s" % (attack, money)
        print " Computer attacking with strength %s" % attack
        pO['health'] = pO['health'] - attack
        attack = 0
        print "\nPlayer Health %s" % pO['health']
        print "Computer Health %s" % pC['health']
        print " Computer player values attack %s, money %s" % (attack, money)
        print "Computer buying"
        if money > 0:
            cb = True
            templist = []
            print "Starting Money %s and cb %s " % (money, cb)
            while cb:
                templist = []
                if len(central['supplement']) > 0:
                    if central['supplement'][0].cost <= money:
                        templist.append(("S", central['supplement'][0]))
                for intindex in range (0, central['activeSize']):
                    if central['active'][intindex].cost <= money:
                        templist.append((intindex, central['active'][intindex]))
                if len(templist) >0:
                    highestIndex = 0
                    for intindex in range(0,len(templist)):
                        if templist[intindex][1].cost > templist[highestIndex][1].cost:
                            highestIndex = intindex
                        if templist[intindex][1].cost == templist[highestIndex][1].cost:
                            if aggressive:
                                if templist[intindex][1].get_attack() >templist[highestIndex][1].get_attack():
                                    highestIndex = intindex
                            else:
                                if templist[intindex][1].get_attack() >templist[highestIndex][1].get_money():
                                    highestIndex = intindex
                    source = templist[highestIndex][0]
                    if source in range(0,5):
                        if money >= central['active'][int(source)].cost:
                            money = money - central['active'][int(source)].cost
                            card = central['active'].pop(int(source))
                            print "Card bought %s" % card
                            pC['discard'].append(card)
                            if( len(central['deck']) > 0):
                                card = central['deck'].pop()
                                central['active'].append(card)
                            else:
                                central['activeSize'] = central['activeSize'] - 1
                        else:
                            print "Error Occurred"
                    else:
                        if money >= central['supplement'][0].cost:
                            money = money - central['supplement'][0].cost
                            card = central['supplement'].pop()
                            pC['discard'].append(card)
                            print "Supplement Bought %s" % card
                        else:
                            print "Error Occurred"
                else:
                    cb = False
                if money == 0:
                    cb = False
        else:
            print "No Money to buy anything"

        if (len(pC['hand']) >0 ):
            for x in range(0, len(pC['hand'])):
                pC['discard'].append(pC['hand'].pop())
        if (len(pC['active']) >0 ):
            for x in range(0, len(pC['active'])):
                pC['discard'].append(pC['active'].pop())
        for x in range(0, pC['handsize']):
                    if len(pC['deck']) == 0:
                        random.shuffle(pC['discard'])
                        pC['deck'] = pC['discard']
                        pC['discard'] = []
                    card = pC['deck'].pop()
                    pC['hand'].append(card)
        print "Computer turn ending"


        print "Available Cards"
        for card in central['active']:
            print card

        print "Supplement"
        if len(central['supplement']) > 0:
            print central['supplement'][0]

        print "\nPlayer Health %s" % pO['health']
        print "Computer Health %s" % pC['health']

        if pO['health'] <= 0:
            cG = False
            print "Computer wins"
        elif pC['health'] <= 0:
            cG = False
            print 'Player One Wins'
        elif central['activeSize'] == 0:
            print "No more cards available"
            if pO['health'] > pC['health']:
                print "Player One Wins on Health"
            elif pC['health'] > pO['health']:
                print "Computer Wins"
            else:
                pHT = 0
                pCT = 0
                if pHT > pCT:
                    print "Player One Wins on Card Strength"
                elif pCT > pHT:
                    print "Computer Wins on Card Strength"
                else:
                    print "Draw"
            cG = False
        if not cG:
            pG = raw_input("\nDo you want to play another game?:")
            cG = (pG=='Y')
            if cG:
                oT = raw_input("Do you want an aggressive (A) opponent or an acquisative (Q) opponent")
                aggressive = (oT=='A')
                pO = {'name': 'player one', 'health': 30, 'deck': None, 'hand': None, 'active': None,
                             'handsize': 5,
                             'discard': None}
                pC = {'name': 'player computer', 'health': 30, 'deck': None, 'hand': None, 'active': None, 'handsize': 5,
                            'discard': None}
                central = {'name': 'central', 'active': None, 'activeSize': 5, 'supplement': None, 'deck': None}
                sdc = [
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
                        ]
                playeronedeck = [8*[Serf()], 2*[Squire()]]

                pod = list(itertools.chain.from_iterable(playeronedeck))
                pO['deck'] = pod
                pO['hand'] = []
                pO['discard'] = []
                pO['active'] = []

                playertwodeck = [8*[Serf()], 2*[Squire()]]

                ptd = list(itertools.chain.from_iterable(playertwodeck))
                pC['deck'] = ptd
                pC['hand'] = []
                pC['discard'] = []
                pC['active'] = []

                supplement = 10*[Levy()]

                deck = list(itertools.chain.from_iterable(sdc))
                random.shuffle(deck)
                central['deck'] = deck
                central['supplement'] = supplement
                central['active'] = []

                for x in range(0, central['activeSize']):
                    card = central['deck'].pop()
                    central['active'].append(card)

                for x in range(0, pO['handsize']):
                    if len(pO['deck']) == 0:
                        random.shuffle(pO['discard'])
                        pO['deck'] = pO['discard']
                        pO['discard'] = []
                    card = pO['deck'].pop()
                    pO['hand'].append(card)

                for x in range(0, pO['handsize']):
                    if len(pC['deck']) == 0:
                        random.shuffle(pO['discard'])
                        pC['deck'] = pC['discard']
                        pC['discard'] = []
                    card = pC['deck'].pop()
                    pC['hand'].append(card)


                print "Available Cards"
                max = central['activeSize']
                count = 0
                while count < max:
                    print central['active'][count]
                    count = count + 1

                print "Supplement"
                if len(central['supplement']) > 0:
                    print central['supplement'][0]
    exit()