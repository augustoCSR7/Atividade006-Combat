import pygame
import config
import game


# import bullet

class Main:
    def __init__(self) -> None:
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = config.initialize_screen()

        self.game = game.Game()

        self.game_loop()

    def game_loop(self):
        while True:
            self.game.check_events()

            self.game.draw_elements(self.screen)

            self.game.check_collisions()

            pygame.display.update()

            self.clock.tick(config.fps)


Main()
