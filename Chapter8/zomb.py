import itertools, sys, time, random, math, pygame
from pygame.locals import *
from mylib import *

#Helper Functions
def calc_velocity(direction, vel=1.0):
    velocity = Point(0,0)
    if direction == 0: #N
        velocity.y = -vel
    elif direction == 2: #E
        velocity.x = vel
    elif direction == 4: #S
        velocity.y = vel
    elif direction == 6: #W
        velocity.x = -vel
    return velocity

def reverse_direction(sprite):
    if sprite.direction == 0:
        sprite.direction = 4
    elif sprite.direction == 2:
        sprite.direction = 6
    elif sprite.direction == 4:
        sprite.direction = 0
    elif sprite.direction == 6:
        sprite.direction = 2

def zombie_create():
    zombie = mySprite()
    zombie.load("zombie walk.png", 96,96, 8)
    zombie.position = random.randint(0,700), random.randint(0,500)
    zombie.direction = random.randint(0,3) * 2
    zombie_group.add(zombie)

def health_create():
    health = mySprite()
    health.load("health.png", 32,32, 1)
    health.position = 400, 300
    health_group.add(health)

#Initializations
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Collision Demo")
font = pygame.font.Font(None, 36)
timer = pygame.time.Clock()
zomcycle = 0

#Sprite Groups
player_group = pygame.sprite.Group()
zombie_group = pygame.sprite.Group()
health_group = pygame.sprite.Group()

#Player Sprite Init
player = mySprite()
player.load("farmer walk.png", 96,96, 8)
player.position = 80,80
player. direction = 4
player_group.add(player)

#Zombie Sprite Init
zombie_image = pygame.image.load("zombie walk.png").convert_alpha()
for n in range(0,10):
    zombie_create()

#Health Sprite Init
for n in range(0,2):
    health_create()

game_over = False
player_moving = False
player_health = 100

#Main Game Loop
while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]: sys.exit()
        elif keys[K_UP]:
            player.direction = 0
            player_moving = True
        elif keys[K_RIGHT]:
            player.direction = 2
            player_moving = True 
        elif keys[K_DOWN]:
            player.direction = 4
            player_moving = True           
        elif keys[K_LEFT]:
            player.direction = 6
            player_moving = True
        else:
            player_moving = False

    #Game-Over dependent events
    if not game_over:
        #set animation frames based on player's direction
        player.first_frame = player.direction * player.columns
        player.last_frame = player.first_frame + player.columns - 1
        if player.frame < player.first_frame:
            player.frame = player.first_frame

        if not player_moving:
            #Stop Animation
            player.frame = player.first_frame = player.last_frame
        else:
            #Move player in given direction
            player.velocity = calc_velocity(player.direction, 1.5)
            player.velocity.x *= 1.5
            player.velocity.y *= 1.5

        #update sprite
        player_group.update(ticks,50)

        #Manually move player
        if player_moving:
            player.X += player.velocity.x
            player.Y += player.velocity.y
            if player.X < 0: player.X = 0
            elif player.X > 700: player.X = 700
            if player.Y < 0: player.Y = 0
            elif player.Y > 500: player.Y = 500
        
        #add zombieevery #ms/ticks
        zomcycle += timer.get_time()
        if zomcycle >= 10000:
            zombie_create()
            zomcycle = 0

        #update zombsprite
        zombie_group.update(ticks,50)

        #iterate through zombies
        for z in zombie_group:
            #set range
            z.first_frame = z.direction * z.columns
            z.last_frame = z.first_frame + z.columns - 1
            if z.frame < z.first_frame:
                z.frame = z.first_frame
            z.velocity = calc_velocity(z.direction)

            #Keep Zombies on screen
            z.X += z.velocity.x
            z.Y += z.velocity.y
            if z.X < 0 or z.X > 700 or z.Y < 0 or z.Y > 500:
                reverse_direction(z)
            
        #check for collisions with zombies
        attacker = None
        attacker = pygame.sprite.spritecollideany(player, zombie_group)
        if attacker != None:
            #Hit? Better Check
            if pygame.sprite.collide_rect_ratio(0.5)(player,attacker):
                player_health -= 10
                if attacker.X < player.X:
                    attacker.X -= 10
                elif attacker.X > player.X:
                    attacker.X += 10
            else:
                attacker = None

        #update health location
        health_group.update(ticks,50)

        #check health collision
        pickup = None
        pickup = pygame.sprite.spritecollideany(player, health_group)
        if pickup != None:
            player_health += 30
            if player_health > 100: player_health = 100
            pickup.X = random.randint(0,700)
            pickup.Y = random.randint(0,500)

    #Death Check
    if player_health <= 0:
        game_over = True

    #clear screen
    screen.fill((50,50,100))

    #draw
    health_group.draw(screen)
    zombie_group.draw(screen)
    player_group.draw(screen)

    #draw energy  bar
    pygame.draw.rect(screen,(50,150,50,180),Rect(300,570,player_health*2,25))
    pygame.draw.rect(screen,(100,200,100,180),Rect(300,570,200,25), 2)

    if game_over:
        print_text(font, 300, 100, "GAME OVER")

    pygame.display.update()
