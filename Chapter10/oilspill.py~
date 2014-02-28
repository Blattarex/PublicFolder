import sys, random, math, time, pygame
from pygame.locals import *
from mylib import *
tan = (210,210, 130, 255)
darktan = (180,180, 110, 255)

#Oil sprite class
class oilsprite(mySprite):
    def __init__(self):
        mySprite.__init__(self)
        self.radius= random.randint(0,60) + 30 #radius 30 to 90
        play_sound(new_oil)

    def update(self, timing, rate= 30):
        mySprite.update(self, timing, rate)

    def fade(self):
        r2 = self.radius//2
        color = self.image.get_at((r2,r2))
        if color.a > 5:
            color.a -= 5
            pygame.draw.circle(self.image, color, (r2,r2), r2, 0)
        else:
            oil_group.remove(self)
            play_sound(clean_oil)

#Init function
def initialize():
    global screen, backbuffer, font, timer, oil_group, cursor, cursor_group

    pygame.init()
    screen = pygame.display.set_mode((800,550))
    font = pygame.font.Font(None, 36)
    pygame.mouse.set_visible(False)
    timer = pygame.time.Clock()

    #create drawing surface
    backbuffer = pygame.Surface((800,550))
    backbuffer.fill(darktan)

    #create oil list
    oil_group = pygame.sprite.Group()

    #Create cursor sprite (WHAT we're making a sprite for the cursor???)
    cursor = mySprite()
    cursor.radius = 60
    image = pygame.Surface((60,60)).convert_alpha()
    image.fill((255,255,255,0))
    pygame.draw.circle(image, (80,80,220,70), (30,30), 30, 0)
    pygame.draw.circle(image, (80,80,255,255), (30,30), 30, 4)
    cursor.set_image(image)
    cursor_group = pygame.sprite.GroupSingle()
    cursor_group.add(cursor)

#audio init
def audioinit():
    global new_oil, clean_oil

    #initialize the audio mixer
    pygame.mixer.init() #force call when pygame.init does not call
    new_oil = pygame.mixer.Sound("new_oil.wav")
    clean_oil = pygame.mixer.Sound("clean_oil.wav")

def play_sound(sound):
    channel = pygame.mixer.find_channel(True)
    channel.set_volume(0.5)
    channel.play(sound)

def add_oil():
    global oil_group, new_oil

    oil = oilsprite()
    image = pygame.Surface((oil.radius, oil.radius)).convert_alpha()
    image.fill((255,255,255,0))
    oil.fadelevel = random.randint(50,150)
    oil_color = 10,10,20,oil.fadelevel
    r2 = oil.radius//2
    pygame.draw.circle(image, oil_color, (r2,r2), r2, 0)
    oil.set_image(image)
    oil.X = random.randint(0, 760)
    oil.Y = random.randint(0, 510)
    oil_group.add(oil)

#In Game Loop
initialize()
audioinit()
game_over = False
last_time = 0

while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]: sys.exit()

    #get mouse
    b1, b2, b3 = pygame.mouse.get_pressed()
    mx, my = pygame.mouse.get_pos()
    pos = (mx + 30, my + 30)
    if b1 > 0: pygame.draw.circle(backbuffer, tan, pos, 30, 0)

    #collion test
    oil_hit = None
    for oil in oil_group:
        if pygame.sprite.collide_circle_ratio(0.5)(cursor,oil):
            oil_hit = oil
            if b1 > 0: oil_hit.fade()
            break

    #add oil drips
    if ticks > last_time + 1000:
        add_oil()
        last_time = ticks

    #draw backbuff
    screen.blit(backbuffer, (0,0))

    #draw oil
    oil_group.update(ticks)
    oil_group.draw(screen)

    #draw cursor
    cursor.position = (mx, my)
    cursor_group.update(ticks)
    cursor_group.draw(screen)

    if oil_hit: print_text(font, 0,0, "OIL SPLOTCH - CLEAN IT")
    else: print_text(font, 0, 0, "CLEAN")
    pygame.display.update()
