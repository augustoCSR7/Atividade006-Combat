import game
import pygame
import config

# Clock instance to limit the updates per second
clock = pygame.time.Clock()

# Gets the first layout
game.get_layout(1)

while True:
    # Check is an event happens
    game.check_events()

    # Check if the game is paused
    game.pause_game()

    # Draws the elements on the screen
    game.draw_sprites()

    # Check collisions
    game.check_collisions()

    # Update the pygame display
    pygame.display.update()

    # Defines the amount of refreshes per second
    clock.tick(config.fps)
