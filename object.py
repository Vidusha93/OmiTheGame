import pygame
import os
import sys

pygame.init()
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)
W, H = 960, 540
WINDOW_SIZE = (W, H)
FPS = 30

win = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('OMI GAME BY ISHANGA')
clock = pygame.time.Clock()
bubblegum = pygame.font.Font('OmiGameData/Bubblegum.ttf', 30)
bubblegumStrok = pygame.font.Font('OmiGameData/Bubblegum.ttf', 32)
bitter = pygame.font.Font('OmiGameData/Bitter-Regular.ttf', 20)
malithi = pygame.font.Font('OmiGameData/FM_MALIT.TTF', 20)
bg = pygame.image.load('OmiGameData/BG.png')
cardDown = pygame.image.load('OmiGameData/CardBack.png')
buttonImage = [pygame.image.load('OmiGameData/blue_button00.png'), pygame.image.load('OmiGameData/green_button00.png')]
card_image_list = [pygame.image.load(os.path.join('DeckofCards', 'Card_ (' + str(x) + ').png')) for x in range(1, 33)]


class background(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        win.blit(bg, (self.x, self.y))


class Button(object):
    def __init__(self, x, y, width, height, text=''):
        self.width = width
        self.height = height
        self.x = (W / 2 - self.width / 2)
        self.y = y
        self.text = text
        self.drawButton = False
        self.clickButton = False
        self.hoverButton = False

    def eventHandler(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.mouseCollision(mouse_x, mouse_y):
            self.hoverButton = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clickButton = True
            else:
                self.clickButton = False
        else:
            self.hoverButton = False

    def draw(self, win):
        if self.drawButton:
            if self.hoverButton:
                win.blit(buttonImage[0], (self.x, self.y))
            else:
                win.blit(buttonImage[1], (self.x, self.y))
            if self.text != '':
                strok_surface = bubblegumStrok.render(self.text, 1, COLOR_WHITE)
                text_surface = bubblegum.render(self.text, 1, COLOR_BLACK)
                win.blit(strok_surface, (self.x + (self.width / 2 - text_surface.get_width() / 2) - 1,
                                         self.y + (self.height / 2 - text_surface.get_height() / 2)))
                win.blit(text_surface, (self.x + (self.width / 2 - text_surface.get_width() / 2),
                                        self.y + (self.height / 2 - text_surface.get_height() / 2)))

    def mouseCollision(self, mouse_x, mouse_y):
        if self.x < mouse_x < self.x + self.width:
            if self.y < mouse_y < self.y + self.height:
                return True
        else:
            return False


class playing_card(object):
    def __init__(self, rank, suit, vel, imageIndex):
        self.rank = rank
        self.suit = suit
        self.suitSi = ''
        self.rankSi = ''
        self.vel = vel
        self.imageIndex = imageIndex
        self.imageDown = cardDown
        self.x = 20
        self.y = 420
        self.width = 70
        self.height = 104
        self.drawCard = False
        self.cardUp = True
        self.drawButton = True
        self.clickCard = False
        self.hoverCard = False

    def eventHandler(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.mouseCollision(mouse_x, mouse_y):
            self.hoverCard = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clickCard = True
            else:
                self.clickCard = False
        else:
            self.hoverCard = False

    def draw(self, win):
        if self.drawCard:
            if self.cardUp:
                win.blit(card_image_list[self.imageIndex], (self.x, self.y))
            else:
                win.blit(self.imageDown, (self.x, self.y))
            if self.hoverCard:
                if self.cardUp:
                    text_surface = bitter.render(self.suit + ' ' + self.rank, 1, COLOR_BLACK)
                    win.blit(text_surface, (self.x - 10, self.y - 40))

    def mouseCollision(self, mouse_x, mouse_y):
        if self.x < mouse_x < self.x + self.width:
            if self.y < mouse_y < self.y + self.height:
                return True
        else:
            return False

class player(object):
    def __init__(self, id):
        self.id = id
        self.hand = []
        self.needShuffle = False

    def sort(self):
        self.hand.sort()
        self.hand.sort()
