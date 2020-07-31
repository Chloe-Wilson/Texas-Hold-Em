from os import path
import os
import GlobalVariables as GV
from random import randint
import draw
import Results
from time import sleep
import pygame



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


def restoreMoney():
    if not path.exists("Money.txt"):
        f = open("Money.txt", 'w')
        f.write('1000')
        f.close()
    f = open("Money.txt", 'r')
    tmp = f.readlines()
    try:
        GV.money = float(tmp[0])
    except:
        GV.money = 1000.0
    if GV.money <= 0:
        GV.money = 1000

def saveMoney():
    if path.exists("Money.txt"):
        os.remove("Money.txt")
    f = open("Money.txt", 'w')
    f.write(str(GV.money))

def deal():
    # Reset Deck if 10 or less cards
    if not len(GV.deck) > 10:
        GV.deck = list(GV.fullDeck)

    # Deal player cards
    GV.player = []
    delt = randint(0, len(GV.deck) - 1)
    GV.player.append(GV.deck[delt])
    GV.deck.pop(delt)
    delt = randint(0, len(GV.deck) - 1)
    GV.player.append(GV.deck[delt])
    GV.deck.pop(delt)

    # Deal ai cards
    GV.ai = []
    delt = randint(0, len(GV.deck) - 1)
    GV.ai.append(GV.deck[delt])
    GV.deck.pop(delt)
    delt = randint(0, len(GV.deck) - 1)
    GV.ai.append(GV.deck[delt])
    GV.deck.pop(delt)

    # Deal river
    GV.river = []
    delt = randint(0, len(GV.deck) - 1)
    GV.river.append(GV.deck[delt])
    GV.deck.pop(delt)
    delt = randint(0, len(GV.deck) - 1)
    GV.river.append(GV.deck[delt])
    GV.deck.pop(delt)
    delt = randint(0, len(GV.deck) - 1)
    GV.river.append(GV.deck[delt])
    GV.deck.pop(delt)
    delt = randint(0, len(GV.deck) - 1)
    GV.river.append(GV.deck[delt])
    GV.deck.pop(delt)
    delt = randint(0, len(GV.deck) - 1)
    GV.river.append(GV.deck[delt])
    GV.deck.pop(delt)


def aiStrat():
    stratA = None
    stratB = None
    if value(GV.ai[0]) == 14:
        if value(GV.ai[1]) < 8:
            stratA = value(GV.ai[1]) - 1
        else:
            stratA = 14 - value(GV.ai[1])
    elif value(GV.ai[1]) == 14:
        if value(GV.ai[0]) < 8:
            stratA = value(GV.ai[0]) - 1
        else:
            stratA = 14 - value(GV.ai[0])
    if stratA == None:
        stratA = value(GV.ai[0]) - value(GV.ai[1])
    if stratA < 0:
        stratA *= -1
    stratB = value(GV.ai[0]) + value(GV.ai[1])

    if stratA < 5 and stratA != 0:
        if stratB > 16:
            coin = randint(0, 0 + stratA) - 2
            if coin < 0:
                coin = 0
        else:
            coin = randint(0, 0 + stratA)
    elif stratA == 0:
        if stratB > 18:
            coin = 0
        else:
            coin = randint(0, 3)
    elif stratB > 16:
        coin = randint(0, 9)
    elif stratB > 10:
        coin = randint(0, 10)
    else:
        coin = randint(0, 12)
    if coin > 9:
        coin = 9
    elif coin < 0:
        coin = 0

    if coin == 0:
        GV.aiStrat = 0
    elif 0 < coin < 3:
        GV.aiStrat = 1
    elif 2 < coin < 6:
        GV.aiStrat = 2
    elif 5 < coin < 9:
        GV.aiStrat = 3
    elif coin == 9:
        GV.aiStrat = 4
    else:
        print('Error aiStart coin was not between 0 and 9')
        GV.running = False

def flipCards():
    if GV.flippedCards == 0:
        draw.card(GV.river[0], 200, 330)
        draw.card(GV.river[1], 325, 330)
        draw.card(GV.river[2], 450, 330)
        GV.flippedCards = 3
    elif GV.flippedCards == 3:
        draw.card(GV.river[3], 575, 330)
        GV.flippedCards = 4
    elif GV.flippedCards == 4:
        draw.card(GV.river[4], 700, 330)
        GV.flippedCards = 5
    else:
        GV.faze = 9
        Results.run()
        return
    GV.firstTurn = True



def aiTurn():
    if GV.money == 0:
        draw.call()
        GV.aiPot = GV.playerPot
    if GV.aiStrat == 4:
        GV.faze = 9
        GV.results = 3
        return
    if GV.aiStrat == 3:
        if GV.playerPot > GV.aiPot:
            draw.call()
            GV.aiPot = GV.playerPot
        else:
            draw.check()

    if GV.aiStrat == 2:
        coin = randint(0, 1)
        if not coin:
            if GV.playerPot > GV.aiPot:
                draw.call()
                GV.aiPot = GV.playerPot
            else:
                draw.check()
        else:
            cash = randint(1, 3) * 5
            if cash > GV.money:
                cash = GV.money
            draw.rase(cash)
            GV.aiPot = GV.playerPot + cash

    if GV.aiStrat == 1:
        coin = randint(0, 2)
        if not coin:
            if GV.playerPot > GV.aiPot:
                draw.call()
                GV.aiPot = GV.playerPot
            else:
                draw.check()
        else:
            cash = randint(2, 4) * 5 * coin
            if cash > GV.money:
                cash = GV.money
            draw.rase(cash)
            GV.aiPot = GV.playerPot + cash

    if GV.aiStrat == 0:
        coin = randint(0, 3)
        if not coin:
            if GV.playerPot > GV.aiPot:
                draw.call()
                GV.aiPot = GV.playerPot
            else:
                draw.check()
        else:
            cash = randint(3, 5) * 5 * coin
            if cash > GV.money:
                cash = GV.money
            draw.rase(cash)
            GV.aiPot = GV.playerPot + cash

    draw.money()
    if GV.firstTurn == False and GV.playerPot == GV.aiPot:
        flipCards()
        return
    GV.firstTurn = False
    GV.faze = 5
    GV.start = True

def playerTurn(move):
    if move == 'raise':
        GV.money -= float(GV.raiseNum)
        GV.playerPot = GV.aiPot + float(GV.raiseNum)
        draw.money()

    elif move == 'fold':
        GV.faze = 9
        GV.results = 4
        return
    elif move == 'check':
        draw.money()

    elif move == 'call':
        GV.money -= GV.aiPot - GV.playerPot
        GV.playerPot = GV.aiPot
        draw.money()

    GV.faze = 3
    GV.start = True
    if GV.firstTurn == False and GV.aiPot == GV.playerPot:
        flipCards()
        return

    GV.firstTurn = False

def reset():
    GV.screen.fill(GV.felt)
    if GV.ante == 1:
        GV.ante = 0
    else:
        GV.ante = 1
    GV.faze = 1
    GV.start = True
    GV.playerPot = 0
    GV.aiPot = 0
    GV.flippedCards = 0
    GV.firstTurn = True

def sleeping(time):
    while time > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GV.running = False
                return
        sleep(0.1)
        time -= 0.1