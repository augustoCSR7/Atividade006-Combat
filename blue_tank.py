import pygame
from config import BLUETANK

class Blue_tank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(BLUETANK)
        self.rect = self.image.get_rect(center=(700,300))


