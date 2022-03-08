import game
import pygame
import config

clock = pygame.time.Clock()

game.get_layout()

while True:
    game.check_events()

    game.draw_sprites()

    game.check_collision()

    pygame.display.update()

    clock.tick(config.fps)