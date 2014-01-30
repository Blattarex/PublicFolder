import math
import pygame
import sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,500))

pygame.display.set_caption("Drawing Arcs")

pointrad1 = 0
pointrad2 = 180

pointmov1 = 3
pointmov2 = 3

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
    screen.fill((0,0,200))

    #update positions
    pointrad1 += pointmov1
    pointrad2 += pointmov2

    #there shouldn't be a condition where we need to switch
    #signs, so just ignore that for now.

    #Drawing the Arcs
    color1 = 255,0,255
    position = 200,150,200,200
    start_angle = math.radians(pointrad1)
    end_angle = math.radians(pointrad2)
    width = 8
    pygame.draw.arc(screen, color1, position, start_angle, end_angle, width)

    pygame.display.update()
