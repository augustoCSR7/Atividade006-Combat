import pygame

# COLORS
RED = (255, 0, 0)
GREEN = (0, 127, 33)
BLUE = (0, 97, 148)

# Rect size constants
# used: 1, 2, 4, 5, 7, 8, 9
RECT1 = (20, 20)

RECT2 = (60, 15)
RECT3 = (20, 60)

RECT4 = (30, 30)

RECT5 = (20, 108)
RECT6 = (108, 10)

RECT7 = (60, 30)
RECT8 = (30, 60)

RECT9 = (20, 168)
RECT10 = (168, 10)

# SCREEN CONFIG
screen_width = 800
screen_height = 550

# Game time in ms
game_time = 140000

# Screen refreshes per second
fps = 60

# Bullet Screen time in ms
bullet_on_screen = 4000

# Number of layouts on the game
number_of_layouts = 2

# Defining the fonts
pygame.font.init()
font1 = pygame.font.Font('./font/Gamer.ttf', 80)
font2 = pygame.font.Font('./font/Gamer.ttf', 50)

# SPRITES
BLUE_TANK = []
RED_TANK = []

# Sounds
pygame.mixer.init()

tank_walk = pygame.mixer.Sound("sound/tank_move.mp3")
tank_walk.set_volume(0.1)

tank_shot = pygame.mixer.Sound("sound/tank_shot.mp3")
tank_shot.set_volume(0.3)

tank_death = pygame.mixer.Sound("sound/tank_death.mp3")
tank_death.set_volume(0.5)

bullet_collision = pygame.mixer.Sound("sound/bullet_sound.mp3")
bullet_collision.set_volume(0.3)


# Saves the sprites' location on the lists
def red_tank_sprites_list():
    count = 0

    for i in range(24):
        RED_TANK.append(f'img/tank rotations/tank1/tank1_{count}.png')
        count = count + 15


# Saves the sprites' location on the lists
def blue_tank_sprites_list():
    count = 0

    for i in range(24):
        BLUE_TANK.append(f'img/tank rotations/tank2/tank2_{count}.png')
        count = count + 15


# Initialize the pygame and returns a display object
def initialize_screen():
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Combat: Tank-Pong")

    return screen


# Checks if the "one" hit_rect collides with the rect of the "two"
def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)


red_tank_sprites_list()
blue_tank_sprites_list()
