import pygame
import config
# import tank
import game2
# import bullet

class main:
    def __init__(self) -> None:
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = config.initialize_screen()

        self.game = game2.Game()

        self.game_loop()

    def game_loop(self):
        while True:
            self.game.draw_elements(self.screen)

            self.game.check_events()

            pygame.display.update()

            self.clock.tick(config.fps)

main()