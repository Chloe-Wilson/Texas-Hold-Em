import GlobalVariables as GV
import pygame
pygame.init()

def txt(txt, color, x, y):
    drawtxt = GV.fontComicSans.render(txt, False, color)
    GV.screen.blit(drawtxt, (x, y))

def money():
    pygame.draw.rect(GV.screen, GV.felt, (10, 750, 300, 50))
    txt('Money = $' + str(GV.money), GV.white, 10, 750)
    pygame.draw.rect(GV.screen, GV.felt, (10, 20, 300, 50))
    txt('Pot = $' + str(GV.playerPot + GV.aiPot), GV.white, 10, 20)

def menu():
    GV.screen.fill(GV.felt)
    GV.screen.blit(pygame.transform.scale(GV.icon, (300, 300)), (350, 100))
    pygame.draw.rect(GV.screen, GV.red, (425, 450, 150, 75))
    txt('Play', GV.white, 473, 463)
    pygame.draw.rect(GV.screen, GV.red, (425, 575, 150, 75))
    txt('Quit', GV.white, 470, 588)

def ante():
    GV.screen.fill(GV.felt)
    money()
    pygame.draw.rect(GV.screen, GV.red, (870, 700, 80, 50))
    txt('Ante', GV.white, 875, 700)
    if GV.ante == 1:
        txt('$10', GV.white, 880, 660)
    elif GV.ante == 0:
        txt('$5', GV.white, 885, 660)

def card(card, x, y):
    pic = pygame.image.load('PlayingCards\\' + str(card) + '.png')
    pic = pygame.transform.scale(pic, (100, 140))
    GV.screen.blit(pic, (x, y))

def deal():
    GV.screen.fill(GV.felt)
    money()

    #Draw player cards
    card(GV.player[0], 438, 600)
    card(GV.player[1], 463, 600)

    #Draw ai cards
    card('cardBack', 438, 60)
    card('cardBack', 463, 60)

    #Draw river cards
    card('cardBack', 200, 330)
    card('cardBack', 325, 330)
    card('cardBack', 450, 330)
    card('cardBack', 575, 330)
    card('cardBack', 700, 330)

def aiFold():
    txt('Ai Folds', GV.red, 350, 260)
    pygame.draw.rect(GV.screen, GV.felt, (438, 60, 125, 140))

def call():
    pygame.draw.rect(GV.screen, GV.felt, (650, 20, 350, 300))
    txt('Call', GV.white, 800, 50)

def check():
    pygame.draw.rect(GV.screen, GV.felt, (650, 20, 350, 300))
    txt('Check', GV.white, 800, 50)

def rase(cash):
    pygame.draw.rect(GV.screen, GV.felt, (650, 20, 350, 300))
    txt('Raise $' + str(cash), GV.white, 800, 50)

def buttons():
    pygame.draw.rect(GV.screen, GV.red, (10, 650, 100, 50))
    txt('Fold', GV.white, 20, 650)
    pygame.draw.rect(GV.screen, GV.red, (10, 575, 100, 50))
    txt('Check', GV.white, 20, 575)
    pygame.draw.rect(GV.screen, GV.red, (890, 650, 100, 50))
    txt('Raise', GV.white, 900, 650)
    pygame.draw.rect(GV.screen, GV.red, (890, 725, 100, 50))
    txt('Call', GV.white, 900, 725)

def fold():
    txt('You Fold', GV.red, 350, 260)
    pygame.draw.rect(GV.screen, GV.felt, (438, 600, 125, 140))

def win():
    txt('You Win', GV.red, 350, 260)
    card(GV.ai[0], 438, 60)
    card(GV.ai[1], 463, 60)

def lose():
    txt('You Lose', GV.red, 350, 260)
    card(GV.ai[0], 438, 60)
    card(GV.ai[1], 463, 60)

def tie():
    txt('You Tie', GV.red, 350, 260)
    card(GV.ai[0], 438, 60)
    card(GV.ai[1], 463, 60)

def clearButtons():
    pygame.draw.rect(GV.screen, GV.felt, (10, 650, 100, 50))
    pygame.draw.rect(GV.screen, GV.felt, (10, 575, 100, 50))
    pygame.draw.rect(GV.screen, GV.felt, (890, 650, 100, 50))
    pygame.draw.rect(GV.screen, GV.felt, (800, 600, 200, 75))
    pygame.draw.rect(GV.screen, GV.felt, (890, 725, 100, 50))

def raseNum():
    pygame.draw.rect(GV.screen, GV.felt, (800, 575, 190, 50))
    txt('$' + GV.raiseNum, GV.white, 970 - len(GV.raiseNum) * 18, 575)