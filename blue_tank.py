import pygame
import game
from config import BLUETANK
from random import randint


class Blue_tank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(BLUETANK[6]).convert_alpha()

        width = self.image.get_width() // 1.2
        height = self.image.get_height() // 1.2
        self.image = pygame.transform.scale(self.image,(width,height)).convert_alpha()

        self.rect = self.image.get_rect(center=(700, 300))
        self.hit_rect = pygame.Rect(0,0,35,35)
        self.hit_rect.center = self.rect.center

        self.sprite_model = 6
        
    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:

            self.sprite_model -= 1

            if self.sprite_model < 0:
                self.sprite_model = 23

            self.image = pygame.image.load(BLUETANK[self.sprite_model]).convert_alpha()
            width = self.image.get_width() // 1.2
            height = self.image.get_height() // 1.2
            self.image = pygame.transform.scale(self.image,(width,height)).convert_alpha()
            self.rect = self.image.get_rect(center=self.rect.center)

        if keys[pygame.K_LEFT]:

            self.sprite_model += 1

            if self.sprite_model > 23:
                self.sprite_model = 0

            self.image = pygame.image.load(BLUETANK[self.sprite_model]).convert_alpha()
            width = self.image.get_width() // 1.2
            height = self.image.get_height() // 1.2
            self.image = pygame.transform.scale(self.image,(width,height)).convert_alpha()
            self.rect = self.image.get_rect(center=self.rect.center)

        if keys[pygame.K_UP]:
            previous_x = self.rect.x
            previous_y = self.rect.y

            if self.sprite_model == 0:
                self.rect.y -= 3
            elif self.sprite_model == 1:
                self.rect.y -= 3
                self.rect.x -= 1
            elif self.sprite_model == 2:
                self.rect.y -= 3
                self.rect.x -= 2
            elif self.sprite_model == 3:
                self.rect.y -= 3
                self.rect.x -= 3
            elif self.sprite_model == 4:
                self.rect.y -= 2
                self.rect.x -= 3
            elif self.sprite_model == 5:
                self.rect.y -= 1
                self.rect.x -= 3
            elif self.sprite_model == 6:
                self.rect.x -= 3
            elif self.sprite_model == 7:
                self.rect.y += 1
                self.rect.x -= 3
            elif self.sprite_model == 8:
                self.rect.y += 2
                self.rect.x -= 3
            elif self.sprite_model == 9:
                self.rect.y += 3
                self.rect.x -= 3
            elif self.sprite_model == 10:
                self.rect.y += 3
                self.rect.x -= 2
            elif self.sprite_model == 11:
                self.rect.y += 3
                self.rect.x -= 1
            elif self.sprite_model == 12:
                self.rect.y += 3
            elif self.sprite_model == 13:
                self.rect.y += 3
                self.rect.x += 1
            elif self.sprite_model == 14:
                self.rect.y += 3
                self.rect.x += 2
            elif self.sprite_model == 15:
                self.rect.y += 3
                self.rect.x += 3
            elif self.sprite_model == 16:
                self.rect.y += 2
                self.rect.x += 3
            elif self.sprite_model == 17:
                self.rect.y += 1
                self.rect.x += 3
            elif self.sprite_model == 18:
                self.rect.x += 3
            elif self.sprite_model == 19:
                self.rect.x += 3
                self.rect.y -= 1
            elif self.sprite_model == 20:
                self.rect.x += 3
                self.rect.y -= 2
            elif self.sprite_model == 21:
                self.rect.x += 3
                self.rect.y -= 3
            elif self.sprite_model == 22:
                self.rect.x += 2
                self.rect.y -= 3
            elif self.sprite_model == 23:
                self.rect.x += 1
                self.rect.y -= 3
            
            if pygame.sprite.collide_rect(self,game.player2.sprite):
                self.rect.x = previous_x
                self.rect.y = previous_y

        if keys[pygame.K_DOWN]:
            previous_x = self.rect.x
            previous_y = self.rect.y

            if self.sprite_model == 0:
                self.rect.y += 3
            elif self.sprite_model == 1:
                self.rect.y += 3
                self.rect.x += 1
            elif self.sprite_model == 2:
                self.rect.y += 3
                self.rect.x += 2
            elif self.sprite_model == 3:
                self.rect.y += 3
                self.rect.x += 3
            elif self.sprite_model == 4:
                self.rect.y += 2
                self.rect.x += 3
            elif self.sprite_model == 5:
                self.rect.y += 1
                self.rect.x += 3
            elif self.sprite_model == 6:
                self.rect.x += 3
            elif self.sprite_model == 7:
                self.rect.y -= 1
                self.rect.x += 3
            elif self.sprite_model == 8:
                self.rect.y -= 2
                self.rect.x += 3
            elif self.sprite_model == 9:
                self.rect.y -= 3
                self.rect.x += 3
            elif self.sprite_model == 10:
                self.rect.y -= 3
                self.rect.x += 2
            elif self.sprite_model == 11:
                self.rect.y -= 3
                self.rect.x += 1
            elif self.sprite_model == 12:
                self.rect.y -= 3
            elif self.sprite_model == 13:
                self.rect.y -= 3
                self.rect.x -= 1
            elif self.sprite_model == 14:
                self.rect.y -= 3
                self.rect.x -= 2
            elif self.sprite_model == 15:
                self.rect.y -= 3
                self.rect.x -= 3
            elif self.sprite_model == 16:
                self.rect.y -= 2
                self.rect.x -= 3
            elif self.sprite_model == 17:
                self.rect.y -= 1
                self.rect.x -= 3
            elif self.sprite_model == 18:
                self.rect.x -= 3
            elif self.sprite_model == 19:
                self.rect.x -= 3
                self.rect.y += 1
            elif self.sprite_model == 20:
                self.rect.x -= 3
                self.rect.y += 2
            elif self.sprite_model == 21:
                self.rect.x -= 3
                self.rect.y += 3
            elif self.sprite_model == 22:
                self.rect.x -= 2
                self.rect.y += 3
            elif self.sprite_model == 23:
                self.rect.x -= 1
                self.rect.y += 3
            
            if pygame.sprite.collide_rect(self,game.player2.sprite):
                self.rect.x = previous_x
                self.rect.y = previous_y

    def update(self):
        self.player_input()
        self.mask = pygame.mask.from_surface(self.image)
        self.hit_rect.center = self.rect.center

    def death(self):
        new_coordinates = (randint(41,759), randint(100,509))
        self.rect.center = new_coordinates

