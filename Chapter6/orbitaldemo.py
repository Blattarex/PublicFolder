import random, sys, math, pygame 
from pygame.locals import *

#PointClass Declaration
class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    #X Property
    def getx(self):
        return self.__x
    def setx(self, x):
        self.__x = x
    x = property(getx, setx)

    #Y property
    def gety(self):
        return self.__y 
    def sety(self, y):
        self.__y = y
    y = property(gety, sety)

    def __str__(self):
        return "{X:" + "{:.0f}".format(self.__x) + \
                ",Y:" + "{:.0f}".format(self.__y) + "}"

#Helper Functions
def wrap_angle(angle):
    return angle % 360

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText,(x,y))

#Window Initializations
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Orbit Demo")

#Loading Bitmaps
space = pygame.image.load("space.png").convert()
planet = pygame.image.load("planet2.png").convert_alpha()
ship = pygame.image.load("freelance.png").convert_alpha()

    #Planet Dimensions Get
pw,ph = planet.get_size()
    #Screen Dimensions Get and Center Get
sw,sh = screen.get_size()
centw = sw/2
centh = sh/2
    #Ship Dimensions Get
shipw,shiph = ship.get_size()

    #Transform Ship Dimensions
#ship = pygame.transform.scale(ship, (shipw//2, shiph//2))
ship = pygame.transform.smoothscale(ship, (shipw//2, shiph//2))

#Point Class Initializations
pos = Point(0,0)
old_pos = Point(0,0)

#Other initializations
angle = 0.0
radius = 250
speed = 0.1
font = pygame.font.Font(None, 15)

#Main Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    if keys[K_UP]:
        speed += .1
    if keys[K_DOWN]:
        speed -= .1

    #Variable Declarations
    pos.x = math.sin( math.radians(angle) ) * radius
    pos.y = math.cos( math.radians(angle) ) * radius
    dx = (pos.x - old_pos.x)
    dy = (pos.y - old_pos.y)
    rangle = math.atan2(dy, dx)
    rangled = wrap_angle( -math.degrees(rangle) )
    scratch_ship = pygame.transform.rotate(ship, rangled)

    #calculations
    angle = wrap_angle(angle - speed)
    wid,hei = scratch_ship.get_size()
    x = centw + pos.x - wid//2
    y = centh + pos.y - hei//2

    #Drawing Objects
    screen.blit(space,(0,0))
    screen.blit(planet,(centw-(pw/2), centh-(ph/2)))
    screen.blit(scratch_ship, (x,y))
    print_text(font, 0, 0, str(pos))

    #Post calculation memory writes
    old_pos.x = pos.x
    old_pos.y = pos.y

    pygame.display.update()
