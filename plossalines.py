#thousand line thingy
import pygame
import sys
import random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawing Lines")


vel1 = 1
vel2 = 2
vel3 = 3
vel4 = 4

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
 

    screen.fill((0,80,0))

    #Drawing the Line
    for x in range (0, 1000): 
        po1x = random.randint(0,600)
        po1y = random.randint(0,500)
        po2x = random.randint(0,600)
        po2y = random.randint(0,500)     
        color = random.randint(0,255),random.randint(0,255),random.randint(0,255)
        width = random.randint(1,10)
        pygame.draw.line(screen, color, (po1x,po1y), (po2x,po2y), width)

    pygame.display.update()
