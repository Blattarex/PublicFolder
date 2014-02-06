#Circle Demo program involving the clock thing

import sys, pygame, datetime, math
from pygame.locals import *
from datetime import datetime, date, time

def ptext(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

#Variables
center = 0,0
radius = 200
white = 255,255,255
red = 255,0,0
T = datetime.today().time()

#Draw Circle
    pygame.draw.circle(screen, white, (pos_x, pos_y), radius, 6)
#Draw Arms

#Draw Hours

#General End stuff -- screen update
