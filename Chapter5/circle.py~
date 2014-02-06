import sys, random, math, pygame
from pygame.locals import *

#main program
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('Incremental Circle')
screen.fill((0,0,100))

posx= 300
posy= 250
radius = 200
angle = 360

#drawloop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    #increment angle
    angle += 1
    if angle >= 360:
        angle = 0
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color = r,g,b

    #calc coord
    x = math.cos( math.radians(angle) ) * radius
    y = math.sin( math.radians(angle) ) * radius

    #draw one step around the circle
    pos = ( int(posx + x), int(posy + y) )
    pygame.draw.circle(screen, color, pos, 10, 0)

    pygame.display.update()
