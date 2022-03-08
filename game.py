import pygame
import config
import layouts

screen = config.initialize_screen()

background = None

walls = pygame.sprite.Group()

def check_events():
    for event in pygame.event.get():
        # Check if the user wants to exit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def get_layout():
    global background, walls

    layout = layouts.Layouts()

    background = layout.get_bg_color()
    walls = layout.get_group()

def draw_sprites():
    global walls, background

    screen.fill(background)

    walls.draw(screen)