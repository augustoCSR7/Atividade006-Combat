from random import choice
import pygame
import config


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((3,3))
        self.image.fill("black")
        self.rect = self.image.get_rect(center = (400,303))

        self.dx = -2 
        self.dy = 2

    def movements(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def update(self):
        self.movements()