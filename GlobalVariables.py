import pygame
pygame.init()
pygame.font.init()

raiseNum = ''
money = None
running = None
faze = None
start = None
ante = 1
playerPot = 0
aiPot = 0
flippedCards = 0
aiStrat = None
results = None
firstTurn = True

player = []
ai = []
river = []

felt = (0, 100, 0)
red = (255, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Texas Hold\'Em')
screen.fill(felt)


fontComicSans = pygame.font.SysFont('Comic Sans MS', 30)

icon = pygame.image.load('Pictures\TexasLogo.png')
icon = pygame.transform.scale(icon, (200, 200))
pygame.display.set_icon(icon)

fullDeck = ['Ace of Spades', 'Two of Spades', 'Three of Spades', 'Four of Spades', 'Five of Spades',
            'Six of Spades', 'Seven of Spades', 'Eight of Spades', 'Nine of Spades', 'Ten of Spades',
            'Jack of Spades', 'Queen of Spades', 'King of Spades',
            'Ace of Diamonds', 'Two of Diamonds', 'Three of Diamonds', 'Four of Diamonds', 'Five of Diamonds',
            'Six of Diamonds', 'Seven of Diamonds', 'Eight of Diamonds', 'Nine of Diamonds', 'Ten of Diamonds',
            'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds',
            'Ace of Clubs', 'Two of Clubs', 'Three of Clubs', 'Four of Clubs', 'Five of Clubs',
            'Six of Clubs', 'Seven of Clubs', 'Eight of Clubs', 'Nine of Clubs', 'Ten of Clubs',
            'Jack of Clubs', 'Queen of Clubs', 'King of Clubs',
            'Ace of Hearts', 'Two of Hearts', 'Three of Hearts', 'Four of Hearts', 'Five of Hearts',
            'Six of Hearts', 'Seven of Hearts', 'Eight of Hearts', 'Nine of Hearts', 'Ten of Hearts',
            'Jack of Hearts', 'Queen of Hearts', 'King of Hearts']

deck = list(fullDeck)