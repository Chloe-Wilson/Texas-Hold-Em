import GlobalVariables as GV

def value(card):
    splitCard = card.split()
    if splitCard[0] == 'Ace':
        return 14
    if splitCard[0] == 'Two':
        return 2
    if splitCard[0] == 'Three':
        return 3
    if splitCard[0] == 'Four':
        return 4
    if splitCard[0] == 'Five':
        return 5
    if splitCard[0] == 'Six':
        return 6
    if splitCard[0] == 'Seven':
        return 7
    if splitCard[0] == 'Eight':
        return 8
    if splitCard[0] == 'Nine':
        return 9
    if splitCard[0] == 'Ten':
        return 10
    if splitCard[0] == 'Jack':
        return 11
    if splitCard[0] == 'Queen':
        return 12
    if splitCard[0] == 'King':
        return 13

def card(value):
    if value == 0:
        return 'Two'
    elif value == 1:
        return 'Three'
    elif value == 2:
        return 'Four'
    elif value == 3:
        return 'Five'
    elif value == 4:
        return 'Six'
    elif value == 5:
        return 'Seven'
    elif value == 6:
        return 'Eight'
    elif value == 7:
        return 'Nine'
    elif value == 8:
        return 'Ten'
    elif value == 9:
        return 'Jack'
    elif value == 10:
        return 'Queen'
    elif value == 11:
        return 'King'
    elif value == 12:
        return 'Ace'

def hand(cards):
    cardsValues = []
    tmp = cards[0].split()
    cardsValues.append(tmp[0])
    tmp = cards[1].split()
    cardsValues.append(tmp[0])
    tmp = cards[2].split()
    cardsValues.append(tmp[0])
    tmp = cards[3].split()
    cardsValues.append(tmp[0])
    tmp = cards[4].split()
    cardsValues.append(tmp[0])
    tmp = cards[5].split()
    cardsValues.append(tmp[0])
    tmp = cards[6].split()
    cardsValues.append(tmp[0])

    cardsSuits = []
    tmp = cards[0].split()
    cardsSuits.append(tmp[2])
    tmp = cards[1].split()
    cardsSuits.append(tmp[2])
    tmp = cards[2].split()
    cardsSuits.append(tmp[2])
    tmp = cards[3].split()
    cardsSuits.append(tmp[2])
    tmp = cards[4].split()
    cardsSuits.append(tmp[2])
    tmp = cards[5].split()
    cardsSuits.append(tmp[2])
    tmp = cards[6].split()
    cardsSuits.append(tmp[2])

    count = []
    count.append(cardsValues.count('Two'))
    count.append(cardsValues.count('Three'))
    count.append(cardsValues.count('Four'))
    count.append(cardsValues.count('Five'))
    count.append(cardsValues.count('Six'))
    count.append(cardsValues.count('Seven'))
    count.append(cardsValues.count('Eight'))
    count.append(cardsValues.count('Nine'))
    count.append(cardsValues.count('Ten'))
    count.append(cardsValues.count('Jack'))
    count.append(cardsValues.count('Queen'))
    count.append(cardsValues.count('King'))
    count.append(cardsValues.count('Ace'))

    if cardsSuits.count('Spades') >= 5 or cardsSuits.count('Diamonds') >= 5 or cardsSuits.count('Hearts') >= 5 or cardsSuits.count('Clubs') >= 5:
        if cardsSuits.count('Spades') >= 5:
            flushSuit = 'Spades'
        elif cardsSuits.count('Diamonds') >= 5:
            flushSuit = 'Diamonds'
        elif cardsSuits.count('Hearts') >= 5:
            flushSuit = 'Hearts'
        elif cardsSuits.count('Diamonds') >= 5:
            flushSuit = 'Clubs'

        flush = []
        tick = 0
        while tick < 7:
            if cards[tick].split()[2] == flushSuit:
                flush.append(cards[tick].split()[0])
        if 'Jack' in flush and 'Queen' in flush and 'King' in flush and 'Ace' in flush and 'Ten' in flush:
            return 'Royal Flush', None, None
        if (
                'Ace' in flush and 'Two' in flush and 'Three' in flush and 'Four' in flush and 'Five' in flush) or (
                'Six' in flush and 'Two' in flush and 'Three' in flush and 'Four' in flush and 'Five' in flush) or (
                'Six' in flush and 'Seven' in flush and 'Three' in flush and 'Four' in flush and 'Five' in flush) or (
                'Six' in flush and 'Seven' in flush and 'Eight' in flush and 'Four' in flush and 'Five' in flush) or (
                'Six' in flush and 'Seven' in flush and 'Eight' in flush and 'Nine' in flush and 'Five' in flush) or (
                'Six' in flush and 'Seven' in flush and 'Eight' in flush and 'Nine' in flush and 'Ten' in flush) or (
                'Jack' in flush and 'Seven' in flush and 'Eight' in flush and 'Nine' in flush and 'Ten' in flush) or (
                'Jack' in flush and 'Queen' in flush and 'Eight' in flush and 'Nine' in flush and 'Ten' in flush) or (
                'Jack' in flush and 'Queen' in flush and 'King' in flush and 'Nine' in flush and 'Ten' in flush):
            return 'Straight Flush', flush[4], None
        elif 4 in count:
            return 'Four of a Kind', card(count.index(4)), None
        elif 3 in count and 2 in count:
            return 'Full House', card(count.index(3)), card(count.index(2))
        else:
            return 'Flush', flush[4], None
    elif 4 in count:
        return 'Four of a Kind', card(count.index(4)), None
    elif 3 in count and 2 in count:
        return 'Full House', card(count.index(3)), card(count.index(2))
    elif 'Jack' in cardsValues and 'Queen' in cardsValues and 'King' in cardsValues and 'Nine' in cardsValues and 'Ten' in cardsValues:
        return 'Straight', 'King', None
    elif 'Jack' in cardsValues and 'Queen' in cardsValues and 'Eight' in cardsValues and 'Nine' in cardsValues and 'Ten' in cardsValues:
        return 'Straight', 'Queen', None
    elif 'Jack' in cardsValues and 'Seven' in cardsValues and 'Eight' in cardsValues and 'Nine' in cardsValues and 'Ten' in cardsValues:
        return 'Straight', 'Jack', None
    elif 'Six' in cardsValues and 'Seven' in cardsValues and 'Eight' in cardsValues and 'Nine' in cardsValues and 'Ten' in cardsValues:
        return 'Straight', 'Ten', None
    elif 'Six' in cardsValues and 'Seven' in cardsValues and 'Eight' in cardsValues and 'Nine' in cardsValues and 'Five' in cardsValues:
        return 'Straight', 'Nine', None
    elif 'Six' in cardsValues and 'Seven' in cardsValues and 'Eight' in cardsValues and 'Four' in cardsValues and 'Five' in cardsValues:
        return 'Straight', 'Eight', None
    elif 'Six' in cardsValues and 'Seven' in cardsValues and 'Three' in cardsValues and 'Four' in cardsValues and 'Five' in cardsValues:
        return 'Straight', 'Seven', None
    elif 'Six' in cardsValues and 'Two' in cardsValues and 'Three' in cardsValues and 'Four' in cardsValues and 'Five' in cardsValues:
        return 'Straight', 'Six', None
    elif 'Ace' in cardsValues and 'Two' in cardsValues and 'Three' in cardsValues and 'Four' in cardsValues and 'Five' in cardsValues:
        return 'Straight', 'Five', None
    elif 3 in count:
        return 'Three of a Kind', card(count.index(3)), None
    elif count.count(2) >= 2:
        return 'Two Pair', card(count.index(2)), card(count.index(2))
    elif 2 in count:
        return 'Pair', card(count.index(2)), None
    else:
        print('High')
        return 'High ' + cardsValues[6], None, None


def run():
    playerHand = list(GV.river)
    playerHand.append(GV.player[0])
    playerHand.append(GV.player[1])
    playerHand.sort(key=value)
    a, b, c = hand(playerHand)

    aiHand = list(GV.river)
    aiHand.append(GV.ai[0])
    aiHand.append(GV.ai[1])
    aiHand.sort(key=value)
    d, e, f = hand(aiHand)

    if a == 'Royal Flush':
        if d == 'Royal Flush':
            GV.results = 2
        else:
            GV.results = 1
    elif a == 'Straight Flush':
        if d == 'Royal Flush':
            GV.results = 0
        elif d == 'Straight Flush':
            if value(b) > value(e):
                GV.results = 1
            elif value(b) == value(e):
                if value(playerHand[6].split()[0]) > value(aiHand[6].split()[0]):
                    GV.results = 1
                elif value(playerHand[6].split()[0]) == value(aiHand[6].split()[0]):
                    GV.results = 2
                else:
                    GV.results = 0
            else:
                GV.results = 0
        else:
            GV.results = 1
    elif a == 'Four of a Kind':
        if d == 'Royal Flush' or d == 'Straight Flush':
            GV.results = 0
        elif d == 'Four of a Kind':
            if value(b) > value(e):
                GV.results = 1
            elif value(b) == value(e):
                if value(playerHand[6].split()[0]) > value(aiHand[6].split()[0]):
                    GV.results = 1
                elif value(playerHand[6].split()[0]) == value(aiHand[6].split()[0]):
                    GV.results = 2
                else:
                    GV.results = 0
            else:
                GV.results = 0
        else:
            GV.results = 1

    elif a == 'Full House':
        if d == 'Royal Flush' or d == 'Straight Flush' or d == 'Four of a Kind':
            GV.results = 0
        elif d == 'Full House':
            if value(b) > value(e):
                GV.results = 1
            elif value(b) == value(e):
                if value(c) > value(f):
                    GV.results = 1
                elif value(c) == value(f):
                    if value(playerHand[6].split()[0]) > value(aiHand[6].split()[0]):
                        GV.results = 1
                    elif value(playerHand[6].split()[0]) == value(aiHand[6].split()[0]):
                        GV.results = 2
                    else:
                        GV.results = 0
                else:
                    GV.results = 0
            else:
                GV.results = 0
        else:
            GV.results = 1

    elif a == 'Flush':
        if d == 'Royal Flush' or d == 'Straight Flush' or d == 'Four of a Kind' or d == 'Full House':
            GV.results = 0
        elif d == 'Flush':
            if value(b) > value(e):
                GV.results = 1
            elif value(b) == value(e):
                if value(playerHand[6].split()[0]) > value(aiHand[6].split()[0]):
                    GV.results = 1
                elif value(playerHand[6].split()[0]) == value(aiHand[6].split()[0]):
                    GV.results = 2
                else:
                    GV.results = 0
            else:
                GV.results = 0
        else:
            GV.results = 1

    elif a == 'Straight':
        if d == 'Royal Flush' or d == 'Straight Flush' or d == 'Four of a Kind' or d == 'Full House' or d == 'Flush':
            GV.results = 0
        elif d == 'Straight':
            if value(b) > value(e):
                GV.results = 1
            elif value(b) == value(e):
                if value(playerHand[6].split()[0]) > value(aiHand[6].split()[0]):
                    GV.results = 1
                elif value(playerHand[6].split()[0]) == value(aiHand[6].split()[0]):
                    GV.results = 2
                else:
                    GV.results = 0
            else:
                GV.results = 0
        else:
            GV.results = 1

    elif a == 'Three of a Kind':
        if d == 'Royal Flush' or d == 'Straight Flush' or d == 'Four of a Kind' or d == 'Full House' or d == 'Flush' or d == 'Straight':
            GV.results = 0
        elif d == 'Three of a Kind':
            if value(b) > value(e):
                GV.results = 1
            elif value(b) == value(e):
                if value(playerHand[6].split()[0]) > value(aiHand[6].split()[0]):
                    GV.results = 1
                elif value(playerHand[6].split()[0]) == value(aiHand[6].split()[0]):
                    GV.results = 2
                else:
                    GV.results = 0
            else:
                GV.results = 0
        else:
            GV.results = 1

    elif a == 'Two Pair':
        if d == 'Royal Flush' or d == 'Straight Flush' or d == 'Four of a Kind' or d == 'Full House' or d == 'Flush' or d == 'Straight' or d == 'Three of a Kind':
            GV.results = 0
        elif d == 'Two Pair':
            if value(b) > value(e):
                GV.results = 1
            elif value(b) == value(e):
                if value(c) > value(f):
                    GV.results = 1
                elif value(c) == value(f):
                    if value(playerHand[6].split()[0]) > value(aiHand[6].split()[0]):
                        GV.results = 1
                    elif value(playerHand[6].split()[0]) == value(aiHand[6].split()[0]):
                        GV.results = 2
                    else:
                        GV.results = 0
                else:
                    GV.results = 0
            else:
                GV.results = 0
        else:
            GV.results = 1

    elif a == 'Pair':
        if d == 'Royal Flush' or d == 'Straight Flush' or d == 'Four of a Kind' or d == 'Full House' or d == 'Flush' or d == 'Straight' or d == 'Three of a Kind' or d == 'Two Pair':
            GV.results = 0
        elif d == 'Pair':
            if value(b) > value(e):
                GV.results = 1
            elif value(b) == value(e):
                if value(playerHand[6].split()[0]) > value(aiHand[6].split()[0]):
                    GV.results = 1
                elif value(playerHand[6].split()[0]) == value(aiHand[6].split()[0]):
                    GV.results = 2
                else:
                    GV.results = 0
            else:
                GV.results = 0
        else:
            GV.results = 1

    elif a.split()[0] == 'High':
        if d.split()[0] != 'High':
            GV.results = 0
        else:
            if value(playerHand[6].split()[0]) > value(aiHand[6].split()[0]):
                GV.results = 1
            elif value(playerHand[6].split()[0]) == value(aiHand[6].split()[0]):
                GV.results = 2
            else:
                GV.results = 0
