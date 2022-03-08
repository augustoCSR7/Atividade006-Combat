import pygame
from bola import Bola
import config
import layouts

screen = config.initialize_screen()

background = None

walls = pygame.sprite.Group()

ball = pygame.sprite.GroupSingle(Bola())

def check_events():
    for event in pygame.event.get():
        # Check if the user wants to exit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def get_layout():
    global background, walls

    layout = layouts.Layouts(2)

    background = layout.get_bg_color()
    walls = layout.get_group()

def draw_sprites():
    global walls, background, ball

    screen.fill(background)

    ball.draw(screen)
    ball.update()

    walls.draw(screen)

def check_collision():
    global ball, walls

    collision = pygame.sprite.spritecollide(ball.sprite,walls,False)

    if collision:
        for wall in collision:
            bottom_collision = ball.sprite.rect.bottom - wall.rect.top
            top_collision = wall.rect.bottom - ball.sprite.rect.top
            right_collision = wall.rect.right - ball.sprite.rect.left
            left_collision = ball.sprite.rect.right - wall.rect.left

            if bottom_collision <= 2 or top_collision <= 2:
                ball.sprite.dy *= -1
            
            if left_collision <= 2 or right_collision <= 2:
                ball.sprite.dx *= -1
            
