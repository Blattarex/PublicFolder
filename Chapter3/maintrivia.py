import trivia

#main program begins
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("The Trivia Game")


def print_text(font, x, y, text, color =(255,255,255), shadow=True):
    if shadow:
        imgText = font.rrender(text, True, (0,0,0))
        screen.blit(imgText, (x-2, y-2))
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))


font1 = pygame.font.Font(None,40)
font2 = pygame.font.Font(None,24)
white = 255,255,255
cyan = 0,255,255
yellow = 255,255,0
purple = 255,0,255
green = 0,255,0
red = 255,0,0

#Loading Trivia
trivia = Trivia("questionsfile.txt")

#Repeating Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                trivia.handle_input(1)
            elif event.key == pygame.K_2:
                trivia.handle_input(2)
            elif event.key == pygame.K_3:
                trivia.handle_input(3)
            elif event.key == pygame.K_4:
                trivia.handle_input(4)

    #clear
    screen.fill((0,0,200))

    #display data
    trivia.show_question()

    #update
    pygame.display.update()
