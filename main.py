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

    # Check collisions
    game.check_collisions()

    pygame.display.update()

    clock.tick(config.fps)