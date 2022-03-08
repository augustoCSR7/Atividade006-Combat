import game
import pygame
import config

# Clock instance to limit the updates per second
clock = pygame.time.Clock()

# Get the layout chosen by the user
game.get_layout(1)

while True:
    # Check is an event happens
    game.check_events()

    # Draws the elements on the screen
    game.draw_sprites()

    # Check collision between the ball and a wall
    game.check_collision()

    pygame.display.update()

    clock.tick(config.fps)