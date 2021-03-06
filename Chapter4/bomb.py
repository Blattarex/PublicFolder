#THE BOMB CATCHER GAME

import sys, random, time, pygame
from pygame.locals import *

def ptext(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

#main program begins
pygame.init()
screen = pygame.display.set_mode((600,500))

font1 = pygame.font.Font(None, 24)
pygame.mouse.set_visible(False)
white = 255,255,255
red = 220, 50, 50
yellow = 230, 230, 50
black = 0,0,0

lives = 9
score = 0
gameover = True
mousex = mousey = 0
posx = 300
posy = 460
bombx = random.randint(0,500)
bomby = -50
vely = 0.7
velx = random.uniform(-1,1)

#explosion and timestop variables
bombex = False
expos = 0,0
radius = 22
width = 20
clockstart = 0
current = 0
seconds = 3

#gameloop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex,mousey = event.pos
            movex,movey = event.rel
        elif event.type == MOUSEBUTTONUP:
            if gameover:
                gameover = False
                lives = 9
                score = 0

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
  
    screen.fill((0,0,100))

    if gameover:
        ptext(font1,100,200, "<CLICK TO PLAY>")
    else:
        if bombex:
            if width > 1:
                pygame.draw.circle(screen, white, expos, radius, width)
                radius += 10
                width -= 1
                pygame.display.update()
            else:
                bombex = False
                width = 20
                radius = 22

        #move bomb
        bomby += vely
        bombx += velx
        if bombx > 600 or bombx < 0:
            velx = -velx

        #check if bomb moves past the player
        if bomby > 500:
            bombex = True
            expos = int(bombx),500
            bombx = random.randint(0,500)
            bomby = -50
            velx = random.uniform(-1,1)
            lives -=1
            if lives == 0:
                gameover = True


        #Check if player caught bomb
        elif bomby > posy:
            if bombx > posx and bombx < posx + 120:
                score += 10
                bombx = random.randint(0,500)
                bomby = -50
                velx = random.uniform(-1,1)

        #draw bomb
        pygame.draw.circle(screen, black, (int(bombx)-4,int(bomby)-4), 30, 0)
        pygame.draw.circle(screen, yellow, (int(bombx),int(bomby)), 30, 0)

        #set basket position
        posx = mousex
        if posx < 0:
            posx = 0
        elif posx > 500:
            posx = 500
        #draw basket
        pygame.draw.rect(screen, black, (posx-4, posy-4, 120, 40), 0)
        pygame.draw.rect(screen, red, (posx, posy, 120, 40), 0)

    #print # of lives
    ptext(font1, 0, 0, "LIVES: " + str(lives))

    #print score
    ptext(font1, 500, 0, "SCORE: " + str(score))

    pygame.display.update()
