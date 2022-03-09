import pygame
from config import BLUETANK


class Blue_tank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(BLUETANK)
        self.rect = self.image.get_rect(center=(700, 300))

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.image = pygame.transform.rotate(self.image, -1)
            self.rect = self.image.get_rect(center=self.rect.center)
        if keys[pygame.K_LEFT]:
            self.image = pygame.transform.rotate(self.image, 1)
            self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.player_input()
