import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((10,10))
        self.image.fill("black")
        self.rect = self.image.get_rect(center = (400,303))

        self.dx = -2
        self.dy = 2

    def movements(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def update(self):
        self.movements()