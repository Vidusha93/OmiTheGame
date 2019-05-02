import pygame
import sys
import os
from random import shuffle
from object import *

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
bitter = pygame.font.Font('OmiGameData/Bitter-Regular.ttf', 20)


def do_shuffle(players):
    shuffle(deck_of_index)
    shuffle(deck_of_index)
    shuffle(deck_of_index)
    print(deck_of_index)
    card = 0
    for i in range(4):
        for j in range(8):
            players[i].hand.append(deck_of_index[card])
            card += 1
    for player in players:
        player.sort()

def set_shuffle():
    currentShuffle = 0
    players[currentShuffle].needShuffle = True
    currentShuffle += 1
    if currentShuffle > 3:
        currentShuffle = 0

def redraw_game_window():
    gameBg.draw(win)
    playButton.draw(win)
    shuffleButton.draw(win)
    for card in player_one.hand:
        deck_of_cards[card].draw(win)
    for tup in table:
        deck_of_cards[tup[0]].draw(win)
    pygame.display.update()


gameBg = background(0, 0)
playButton = Button(480, 370, 190, 49, 'PLAY')
shuffleButton = Button(480, 270, 190, 49, 'Shuffle')
ranks = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
deck_of_cards = []
deck_of_index = []
deck_of_index.extend(range(0, 32))
imageListIndex = 0
for suit in suits:
    cardV = 1
    for rank in ranks:
        deck_of_cards.append(playing_card(rank, suit, cardV, imageListIndex))
        imageListIndex += 1
        cardV += 1
players = []
for i in range(4):
    players.append(player(i))
player_one = players[0]
player_two = players[1]
player_three = players[2]
player_four = players[3]
table = []

def game_window():
    run = True
    pOnePos = 183
    print("In Game Window")
    set_shuffle()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for card in deck_of_cards:
                card.eventHandler(event)
        if player_one.hand:
            pOnePos = 183
            tablePos = 183
            tablePos += (75 * (8 - len(table))) // 2
            pOnePos += (75 * (8 - len(player_one.hand))) // 2
            for card in player_one.hand:
                deck_of_cards[card].drawCard = True
                deck_of_cards[card].x = pOnePos
                pOnePos += 75
            for card in player_one.hand:
                if deck_of_cards[card].clickCard:
                    table.append((card, player_one.id))
                    player_one.hand.pop(player_one.hand.index(card))
            for tup in table:
                deck_of_cards[tup[0]].y = 170
                deck_of_cards[tup[0]].x = tablePos
                tablePos += 75
        redraw_game_window()

def shuffle_window():
    run = True
    pOnePos = 183
    print("In shuffle_window")
    shuffleButton.drawButton = True
    set_shuffle()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for card in deck_of_cards:
                card.eventHandler(event)
            shuffleButton.eventHandler(event)
        for p in players:
            if p.needShuffle:
                if shuffleButton.clickButton:
                    shuffleButton.clickButton = False
                    shuffleButton.drawButton = False
                    do_shuffle(players)
                    game_window()
        redraw_game_window()

def main_window():
    run = True
    playButton.drawButton = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            playButton.eventHandler(event)
        if playButton.clickButton:
            playButton.drawButton = False
            shuffle_window()
        redraw_game_window()


main_window()
