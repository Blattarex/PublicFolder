import sys, random, math, pygame
from pygame.locals import *

# Mysprite class goes here
class mySprite(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self) #extend the base Sprite Class
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.colums = 1
        self.last_time = 0

    #X Property
    def _getx(self): return self.rect.x
    def _setx(self, value): self.rect.x = value
    X = property(_getx, _setx)

    #Y Property
    def _gety(self): return self.rect.y
    def _sety(self, value): self.rect.y = value
    Y = property(_gety, _sety)

    #Position Property
    def _getpos(self): return self.rect.topleft
    def _setpos(self, pos): self.rect.topleft = pos
    position = property(_getpos, _setpos)

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0,0,width,height)
        self.columns = columns
        #Attempt auto calculation of total frames
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate = 30):
        #Update animation frame number
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        #build current frame only if changed
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

    def __str__(self):
        return str(self.frame) + "," + str(self.frame_width) + \
                "," + str(self.last_frame) + "," + str(self.frame_width) + \
                "," + str(self.frame_height) + "," + str(self.columns) + \
                "," + str(self.rect)


# Helper Functions
def print_text(font, x , y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

def reset_arrow():
    y = random.randint(250,350)
    arrow.position = 800,y

#Main Game Program
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Escape from the Dragon")
font = pygame.font.Font(None, 18)
framerate = pygame.time.Clock()

#Bitmap load
bg = pygame.image.load("background.png"). convert_alpha()

#Create the Sprite Group
group = pygame.sprite.Group()

#create dragon sprite
dragon = mySprite(screen)

dragon.load("dragon.png", 260, 150, 3)
dragon.position = 100, 230
group.add(dragon)

#Player Sprite
player = mySprite(screen)
player.load("caveman.png", 50, 65, 8)
player.first_frame = 1
player.last_frame = 7
player.position = 400, 303
group.add(player)

#Create Arrow Sprite
arrow = mySprite(screen)
arrow.load("flame.png", 40, 16, 1)
arrow.position = 800, 320
group.add(arrow)

#Global Variable Declarations
arrow_vel = 8.0
game_over = False
you_win = False
player_jumping = False
jump_vel = 0.0
player_start_y = player.Y
successful_jumps = 0
double_jump = False
keyflag = False

#Game Loop
while True:
    framerate.tick(30)
    ticks = pygame.time.get_ticks()

    #Keyboard Events so you don't have to hit it for something
    #like a millisecond

    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
        elif event.type == KEYDOWN: keyflag = True
        elif event.type == KEYUP: keyflag = False
    key = pygame.key.get_pressed()
    if key[K_ESCAPE]:
        sys.exit()
    elif key[K_SPACE]:
        if not player_jumping:
            player_jumping = True
            jump_vel = -8.0
        elif keyflag and not double_jump:
            jump_vel = -8.0
            double_jump = True

    #update arrow
    if not game_over:
        arrow.X -= arrow_vel
        if arrow.X < -40: reset_arrow()

    #Check if arrow collides with player
    if pygame.sprite.collide_rect(arrow, player):
        reset_arrow()
        player.X -= 10

    #check if arrow collides with dragon
    if pygame.sprite.collide_rect(arrow, dragon):
        reset_arrow()
        dragon.X -=10
        successful_jumps += 1

    #check if player collides with dragon
    if pygame.sprite.collide_rect(player, dragon):
        game_over = True

    #check if dragon moves offscreen
    if dragon.X < -100:
        you_win = True
        game_over = True

    #Check if player is jumping
    if player_jumping:
        player.Y += jump_vel
        jump_vel += 0.5
        if player.Y > player_start_y:
            player_jumping = False
            player.Y = player_start_y
            jump_vel = 0.0
            double_jump = False

    #draw bg
    screen.blit(bg, (0,0))

    #Update Group
    if not game_over:
        group.update(ticks, 50)

    #draw sprites
    group.draw(screen)

    #messaging
    print_text(font, 0, 0, "Successful Jumps: " + str(successful_jumps))
    print_text(font, 350, 560, "Press Space to Jump!")
    if game_over:
        print_text(font, 360, 100, "G A M E - O V E R")
        if you_win:
            print_text(font, 330, 130, "YOU BEAT THE DRAGON!")
        else:
            print_text(font, 330, 130, "THE DRAGON GOT YOU.")

    pygame.display.update()