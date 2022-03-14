import pygame


# Wall class for the walls of the game
class Wall(pygame.sprite.Sprite):
    def __init__(self, color, dimensions: tuple, coordinates: tuple):
        super().__init__()
        self.image = pygame.Surface(dimensions)
        self.image.fill(color)
        self.rect = self.image.get_rect(center=coordinates)
