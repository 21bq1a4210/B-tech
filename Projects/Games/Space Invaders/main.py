import math
import random

from pygame.locals import *
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
#mixer.music.play(-1)

# Caption and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("Images/ufo.png")
pygame.display.set_icon(icon)

#Score
score_value = 0
font = pygame.font.Font("Font/jd_led3.ttf", 32)
textX, textY = 10, 10

# player
playerImg = pygame.image.load("Images/player.png")
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def show_score(x, y):
    score = font.render(f"Score: {str(score_value)}", True, (255, 255, 0))
    screen.blit(score, (x, y))

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 20

#create enemies
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("Images/enemy.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)

#draw enemy
def show_enemy(x, y, i):
    screen.blit(enemyImg[i], (x,y))

#Bullet
#ready - You cant see the bullet on the screen
#fire - the bullet is currently moving

bulletImg = pygame.image.load("Images/bullet.png")
bulletX, bulletY = 0, 480
bulletX_change, bulletY_change = 0, 20  # Increase bulletY_change for rapid fire
bullet_state = "ready"

def fire_bullet(x, y):
    global  bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))


def is_collision_with_player(playerX, playerY, enemyX, enemyY):
    distance = math.sqrt(math.pow(playerX - enemyX, 2) + (math.pow(playerY - enemyY, 2)))
    return distance < 27

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    return distance < 27

# Clock for controlling frame rate
clock = pygame.time.Clock()
frame_rate = 45 # Adjust this value to control the frame rate

if __name__ == "__main__":
    # game loop
    running = True
    game_over_flag = False
    while running:
        # Limit frame rate
        clock.tick(frame_rate)
        # RGB
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #if keystroke is pressed check whether its close or right or left
            if event.type == pygame.KEYDOWN:
                #close
                if event.key == pygame.K_ESCAPE:
                    running = False
                # left key
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                # right key
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                # shoot
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        bulletSound = mixer.Sound("Sounds/laser.wav")
                        bulletSound.play()
                        # Get the current x cordinate of the spaceship
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)

                #stop movement id=f key is released
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        playerX_change = 0
                #update player positions
                playerX += playerX_change
                if playerX <= 0:
                    playerX = 0
                elif playerX >= 736:
                    playerX = 736

        #Enemy Movement
        for i in range(num_of_enemies):
            # move enemy position
            enemyX[i] += enemyX_change[i]

            # turn around movement if edge is crossed
            if enemyX[i] <= 0:
                enemyX_change[i] = 2
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -2
                enemyY[i] += enemyY_change[i]

            # draw enemy
            show_enemy(enemyX[i], enemyY[i], i)

            #collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosionSound = mixer.Sound("Sounds/explosion.wav")
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

        if bulletY <= 0:
            bulletY = 480
            bullet_state = 'ready'
        if bullet_state is 'fire':
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change
        player(playerX, playerY)
        show_score(textX, textY)
        pygame.display.update()

    # quit pygame
    pygame.quit()
