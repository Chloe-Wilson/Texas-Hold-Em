from Utils import *
import pygame
import GlobalVariables as GV
import draw
from time import sleep

pygame.init()

restoreMoney()

GV.faze = 0
GV.start = True
GV.running = True
while GV.running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GV.running = False
        if GV.faze == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 425 < mouse[0] < 575 and 450 < mouse[1] < 525:
                    GV.faze = 1
                    GV.start = True
                elif 425 < mouse[0] < 575 and 575 < mouse[1] < 650:
                    GV.running = False
        elif GV.faze == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 870 < mouse[0] < 950 and 700 < mouse[1] < 750:
                    GV.faze = 2
                    if GV.ante == 1:
                        GV.money -= 10
                        GV.playerPot = 10
                        GV.aiPot = 5
                        GV.turn = 0
                    elif GV.ante == 0:
                        GV.money -= 5
                        GV.playerPot = 5
                        GV.aiPot = 10
                        GV.turn = 1
        elif GV.faze == 5:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0 and len(GV.raiseNum) < 10:
                    if len(GV.raiseNum) == 0:
                        pass
                    else:
                        GV.raiseNum = GV.raiseNum + '0'
                elif event.key == pygame.K_1 and len(GV.raiseNum) < 10:
                    if len(GV.raiseNum) == 0:
                        GV.raiseNum = '1'
                    else:
                        GV.raiseNum = GV.raiseNum + '1'
                elif event.key == pygame.K_2 and len(GV.raiseNum) < 10:
                    if len(GV.raiseNum) == 0:
                        GV.raiseNum = '2'
                    else:
                        GV.raiseNum = GV.raiseNum + '2'
                elif event.key == pygame.K_3 and len(GV.raiseNum) < 10:
                    if len(GV.raiseNum) == 0:
                        GV.raiseNum = '3'
                    else:
                        GV.raiseNum = GV.raiseNum + '3'
                elif event.key == pygame.K_4 and len(GV.raiseNum) < 10:
                    if len(GV.raiseNum) == 0:
                        GV.raiseNum = '4'
                    else:
                        GV.raiseNum = GV.raiseNum + '4'
                elif event.key == pygame.K_5 and len(GV.raiseNum) < 10:
                    if len(GV.raiseNum) == 0:
                        GV.raiseNum = '5'
                    else:
                        GV.raiseNum = GV.raiseNum + '5'
                elif event.key == pygame.K_6 and len(GV.raiseNum) < 10:
                    if len(GV.raiseNum) == 0:
                        GV.raiseNum = '6'
                    else:
                        GV.raiseNum = GV.raiseNum + '6'
                elif event.key == pygame.K_7 and len(GV.raiseNum) < 10:
                    if len(GV.raiseNum) == 0:
                        GV.raiseNum = '7'
                    else:
                        GV.raiseNum = GV.raiseNum + '7'
                elif event.key == pygame.K_8 and len(GV.raiseNum) < 10:
                    if len(GV.raiseNum) == 0:
                        GV.raiseNum = '8'
                    else:
                        GV.raiseNum = GV.raiseNum + '8'
                elif event.key == pygame.K_9 and len(GV.raiseNum) < 10:
                    if len(GV.raiseNum) == 0:
                        GV.raiseNum = '9'
                    else:
                        GV.raiseNum = GV.raiseNum + '9'
                elif event.key == pygame.K_BACKSPACE:
                    if len(GV.raiseNum) == 0:
                        pass
                    else:
                        GV.raiseNum = GV.raiseNum[:-1]
                elif event.key == pygame.K_PERIOD and len(GV.raiseNum) < 10:
                    if len(GV.raiseNum) == 0:
                        pass
                    else:
                        GV.raiseNum = GV.raiseNum + '.'
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 10 < mouse[0] < 110 and 650 < mouse[1] < 700:
                    playerTurn('fold')
                elif 10 < mouse[0] < 110 and 575 < mouse[1] < 625:
                    if GV.playerPot == GV.aiPot:
                        playerTurn('check')
                elif 890 < mouse[0] < 990 and 650 < mouse[1] < 700 and GV.raiseNum != '':
                    if GV.money >= float(GV.raiseNum) > GV.aiPot - GV.playerPot:
                        playerTurn('raise')
                elif 890 < mouse[0] < 990 and 725 < mouse[1] < 775:
                    if GV.playerPot < GV.aiPot:
                        playerTurn('call')



    if GV.start == True:
        if GV.faze == 0:
            draw.menu()
            GV.start = False
        elif GV.faze == 1:
            draw.ante()
            GV.start = False
        elif GV.faze == 3:
            aiTurn()
            GV.start = False
        elif GV.faze == 5:
            draw.money()
            draw.buttons()
            GV.raiseNum = ''
            GV.start = False

    if GV.faze == 2:
        deal()
        draw.deal()
        aiStrat()
        GV.start = True
        if GV.ante == 1:
            GV.faze = 3
        elif GV.ante == 0:
            GV.faze = 5

    if GV.faze == 3:
        GV.faze = 5
        aiTurn()

    if GV.faze == 5:
        draw.raseNum()

    if GV.faze == 9:
        if GV.results == 0:
            # Lose
            draw.lose()
            pygame.display.update()
            sleeping(10)
            reset()
        elif GV.results == 1:
            # Win
            draw.win()
            pygame.display.update()
            GV.money += GV.playerPot + GV.aiPot
            sleeping(10)
            reset()
        elif GV.results == 2:
            # Tie
            draw.tie()
            pygame.display.update()
            GV.money += GV.playerPot
            sleeping(10)
            reset()
        elif GV.results == 3:
            # Ai Fold
            draw.aiFold()
            pygame.display.update()
            GV.money += GV.playerPot + GV.aiPot
            sleeping(5)
            reset()
        elif GV.results == 4:
            # You Fold
            draw.fold()
            pygame.display.update()
            sleeping(5)
            reset()

saveMoney()
pygame.quit()
