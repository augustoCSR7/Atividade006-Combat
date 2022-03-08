from pickletools import read_unicodestring1
import pygame

screen_width = 800
screen_height = 550

# Center -> 400, 303 

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

fps = 60

def initialize_screen():

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Combat")

    return screen