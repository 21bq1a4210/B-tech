import math
import random

import pygame
from pygame import mixer

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('Images/background.png')

# sound
mixer.music.load('Sounds/background.wav')
mixer.music.play(-1)

# Caption and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("Images/ufo.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("Images/player.png")
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# game loop
running = True
while running:
    # RGB
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    player(playerX, playerY)
    pygame.display.update()

# quit pygame
pygame.quit()
