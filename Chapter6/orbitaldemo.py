import random, sys, math, pygame
from pygame.locals import *

#Variable Initializations


#Helper Functions
#def ptxt(font, x, y, color=(255,255,255)):
#   imageText =
#   pygame.draw.text()

#Window Initializations
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Orbit Demo")

#Loading Bitmaps
space = pygame.image.load("space.png").convert()

#Main Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit
    
    screen.blit(space,(0,0))

    pygame.display.update()
