import sys, pygame
from pygame.locals import *

def ptxt(font,x,y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText,(x,y))

#main
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Mouse Demo")
font1 = pygame.font.Font(None, 24)
white = 255,255,255

mousex = mousey = 0
movex = movey = 0
mousedown = mouseup = 0
mousedownx = mousedowny = 0
mouseupx = mouseupy = 0

#gameloop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex,mousey = event.pos
            movex,movey = event.rel
        elif event.type == MOUSEBUTTONDOWN:
            mousedown = event.button
            mousedownx,mousedowny = event.pos
        elif event.type == MOUSEBUTTONUP:
            mouseup = event.button
            mouseupx,mouseupy = event.pos

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((0,100,0))

    ptxt(font1, 0, 0, "Mouse Events")
    ptxt(font1, 0, 20, "Mouse position: " + str(mousex) + "," + str(mousey))
    ptxt(font1, 0, 40, "Mouse relative: " + str(movex) + "," + str(movex))

    ptxt(font1, 0, 60, "Mouse button down: " + str(mousedown) + "," + str(mousedownx) + "," + str(mousedowny))
    ptxt(font1, 0, 80, "Mouse button up: " + str(mouseup) + "," + str(mouseupx) + ","+  str(mouseupy))

    ptxt(font1, 0, 160, "Mouse Polling")

    x,y = pygame.mouse.get_pos()

    ptxt(font1, 0, 180, "Mouse position: " + str(x) + "," + str(y))

    b1, b2, b3 = pygame.mouse.get_pressed()
    ptxt(font1, 0, 200, "Mouse buttons: " + str(b1) + "," + str(b2) + "," + str(b3))

    pygame.display.update()
