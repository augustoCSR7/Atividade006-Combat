import game
import pygame
import config

clock = pygame.time.Clock()

game.get_layout()

while True:
    game.check_events()

    game.draw_sprites()

    pygame.display.update()

    clock.tick(config.fps)