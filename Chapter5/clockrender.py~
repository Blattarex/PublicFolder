import sys, datetime, pygame, math
from datetime import datetime, date, time
from pygame.locals import *

px = 300
py = 250
radius = 250
angle = 360
pink = 255, 100, 255
orange = 220, 180, 0
white = 255,255,255
yellow = 255,255, 0

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))
    
def wrap_angle(angle):
    return abs(angle % 360)

#main program
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Analog clock demo")
font = pygame.font.Font(None,36)
font1 = pygame.font.Font(None,20)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.quit
    key = pygame.key.get_pressed()
    if key[K_ESCAPE]:
        sys.exit()

    screen.fill((0,0,100))

    #Draw Clock boundary
    pygame.draw.circle(screen, white, (px,py), radius, 6)

    #Drawing in hours
    for n in range (1,13):
        angle = math.radians( n* (360/12) -90)
        x = math.cos(angle) * (radius - 20) - 10
        y = math.sin(angle) * (radius - 20) - 10
        if n % 3 == 0:
            print_text(font, px+x, py+y, str(n))
        else:
            print_text(font1, px+x, py+y, str(n))

    today = datetime.today()
    hours = today.hour
    mins = today.minute
    seconds = today.second

    #Drawing Hour Hand
    hour_angle = wrap_angle( hours * (360/12) + mins* (3/6.0) - 90)
    hour_angle = math.radians( hour_angle )
    hour_x = math.cos( hour_angle ) * (radius - 80)
    hour_y = math.sin( hour_angle ) * (radius - 80)
    target = (px + hour_x, py + hour_y)
    pygame.draw.line(screen, pink, (px,py), target, 25)

    #Drawing Minute hand
    min_angle = wrap_angle( mins * (360/60) - 90)
    min_angle = math.radians( min_angle )
    min_x = math.cos( min_angle ) * (radius - 60)
    min_y = math.sin( min_angle ) * (radius - 60)
    target = (px + min_x, py + min_y)
    pygame.draw.line(screen, orange, (px,py), target, 16)

    #Drawing Second hand
    second_angle = wrap_angle( seconds * (360/60) - 90)
    second_angle = math.radians( second_angle )
    second_x = math.cos( second_angle ) * (radius - 40)
    second_y = math.sin( second_angle ) * (radius - 40)
    target = (px + second_x, py + second_y)
    pygame.draw.line(screen, white, (px,py), target, 6)

    pygame.draw.circle(screen, white, (px,py,), 20)

    print_text(font, 0, 0, str(hours) + ":" + str(mins) + ":" + str(seconds))
    pygame.display.update()
