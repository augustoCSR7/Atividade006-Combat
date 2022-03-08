import pygame
from Config import BLUETANK

class BlueTank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(BLUETANK)
        self.rect = self.image.get_rect(center=(750,300))

all_sprites = pygame.sprite.Group()
tank = BlueTank()
all_sprites.add(tank)
