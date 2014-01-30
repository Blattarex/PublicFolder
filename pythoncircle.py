import pygame
import sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drawingcircles")

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill((0,0,200))

    color = 255,255,0
    position = 300,250
    radius = 100
    width = 10
    pygame.draw.circle(screen, color, position, radius, width)

    pygame.display.update()
