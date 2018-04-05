import pygame, sys, time, math, random
from pygame.locals import *

WINDOWHEIGHT = 400
WINDOWWIDTH = 400

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 128, 0)

pygame.init()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

box = pygame.Rect(5, 200, 30, 30)
box2 = pygame.Rect(250, 100, 30, 30)

mainClock = pygame.time.Clock()

def checkEvents():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE and not fired:
                fired = True

def draw():
    windowSurface.fill(BLACK)
    pygame.draw.rect(windowSurface, RED, box)
    pygame.draw.rect(windowSurface, GREEN, box2)
    pygame.display.update()
    mainClock.tick(30)

def runGame():
        box.x += 5
        box.y -= 5

while True:
    checkEvents()
    runGame()
    draw()
            

