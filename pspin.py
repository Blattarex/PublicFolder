import pygame
import sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Lines")

po1x = 100
po1y = 100
po2x = 500
po2y = 400

vel1 = 1
vel2 = 2
vel3 = 3
vel4 = 4

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    
    screen.fill((0,80,0))

    po1x += vel1
    po2x += vel2
    po1y += vel3
    po2y += vel4

    if po1x > 500 or po1x < 0:
        vel1 = -vel1
    if po2x > 500 or po2x < 0:
        vel2 = -vel2
    if po1y > 500 or po1y < 0:
        vel3 = -vel3
    if po2y > 500 or po2y < 0:
        vel4 = -vel4

    #Drawing the Line
    color = 100, 255, 200
    width = 8
    pygame.draw.line(screen, color, (po1x,po1y), (po2x,po2y), width)

    pygame.display.update()
