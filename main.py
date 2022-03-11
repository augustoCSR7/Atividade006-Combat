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

    game.pause_game()

    # Draws the elements on the screen
    game.draw_sprites()

    # Check collision between the ball and a wall
    game.check_collision()

    game.check_bullet_tank_collision()

    pygame.display.update()

    clock.tick(config.fps)