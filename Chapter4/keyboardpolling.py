import sys, random, time, pygame
from pygame.locals import *

def print_text(font, x, y, text, color=((255,255,255))):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

#main
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Keyboard Demo")
#"Global Variables"
font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 200)
white = 255,255,255
yellow = 255,255,0

keyflag = False
correctanswer = 97 #char value of 'a'
seconds = 11
score = 0
clockstart = 0
gameover = True

#gameloop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            keyflag = True
        elif event.type == KEYUP:
            keyflag = False

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    if keys[K_RETURN]:
        if gameover:
            gameover = False
            score = 0
            seconds = 11
            clockstart = time.clock()

    current = time.clock() - clockstart
    speed = score * 6
    if seconds-current < 0:
        gameover = True
    elif current <= 10:
        if keys[correctanswer]:
            correctanswer = random.randint(97,122)
            score += 1

    #clear screen
    screen.fill((0,100,0))

    print_text(font1, 0, 0, "Let's see how fast you can type!")
    print_text(font1, 0, 20, "Try to keep up for 10 seconds...")

    if keyflag:
        print_text(font1,500,0,"<key>")

    if not gameover:
        print_text(font1, 0, 80, "Time: " + str(int(seconds-current)))

    print_text(font1, 0, 100, "Speed: " + str(speed) + " letters/min")

    if gameover:
        print_text(font1, 0, 160, "Press Enter to Start")

    print_text(font2, 0, 240, chr(correctanswer-32), yellow)

    #update
    pygame.display.update()
