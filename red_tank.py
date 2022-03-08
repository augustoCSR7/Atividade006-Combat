import pygame
from config import REDTANK

class Red_tank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(REDTANK)
        self.rect = self.image.get_rect(center=(100,300))


