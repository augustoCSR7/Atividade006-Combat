import pygame
from pygame.locals import *
from sys import exit
from BlueTank import *
from config import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(Red)
pygame.display.set_caption('COMBAT GAME')

pontos1 = 0
pontos2 = 0
while True:
    Mens_pontos1 = f'{pontos1}'
    Mens_pontos1format = font.render(Mens_pontos1, False, Green)
    Mens_pontos2 = f'{pontos2}'
    Mens_pontos2format = font.render(Mens_pontos2, False, Blue)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    screen.blit(Mens_pontos1format,(250,-15))
    screen.blit(Mens_pontos2format,(550,-15))
    all_sprites.draw(screen)
    all_sprites.update()

    pygame.display.update()