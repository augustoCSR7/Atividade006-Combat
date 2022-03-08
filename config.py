import pygame

#SCREEN CONFIG
screen_width = 800
screen_height = 550

#COLORS
RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (0, 127, 33)
BLUE = (0, 97, 148)

# Rect size constants
# used: 1, 2, 4, 5, 7, 8, 9
RECT1 = (20, 20)

RECT2 = (60, 20)
RECT3 = (20, 60)

RECT4 = (30, 30)

RECT5 = (20, 108)
RECT6 = (108, 10)

RECT7 = (60, 30)
RECT8 = (30, 60)

RECT9 = (20, 168)
RECT10 = (168, 10)

#SPRITES
BLUETANK = 'Sprites/tank2.png'
REDTANK = 'Sprites/tank1.png'

# Screen refreshs per second
fps = 60

def initialize_screen():
    global font

    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Combat")

    return screen
