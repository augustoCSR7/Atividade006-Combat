import pygame
from config import REDTANK


class Red_tank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(REDTANK)
        self.rect = self.image.get_rect(center=(100, 300))

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.image = pygame.transform.rotate(self.image, 1)
            self.rect = self.image.get_rect(center=self.rect.center)
        if keys[pygame.K_d]:
            self.image = pygame.transform.rotate(self.image, -1)
            self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.player_input()
