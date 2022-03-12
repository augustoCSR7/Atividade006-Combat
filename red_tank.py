from random import randint
import game
import pygame
from config import REDTANK


class Red_tank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(REDTANK[18]).convert_alpha()

        width = self.image.get_width() // 1.2
        height = self.image.get_height() // 1.2
        self.image = pygame.transform.scale(self.image,(width,height)).convert_alpha()

        self.rect = self.image.get_rect(center=(100, 300))
        self.hit_rect = pygame.Rect(0,0,35,35)
        self.hit_rect.center = self.rect.center

        self.sprite_model = 18

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:

            self.sprite_model -= 1

            if self.sprite_model < 0:
                self.sprite_model = 23

            self.image = pygame.image.load(REDTANK[self.sprite_model]).convert_alpha()
            width = self.image.get_width() // 1.2
            height = self.image.get_height() // 1.2
            self.image = pygame.transform.scale(self.image,(width,height)).convert_alpha()
            self.rect = self.image.get_rect(center = self.rect.center)

        if keys[pygame.K_a]:

            self.sprite_model += 1

            if self.sprite_model > 23:
                self.sprite_model = 0

            self.image = pygame.image.load(REDTANK[self.sprite_model]).convert_alpha()
            width = self.image.get_width() // 1.2
            height = self.image.get_height() // 1.2
            self.image = pygame.transform.scale(self.image,(width,height)).convert_alpha()
            self.rect = self.image.get_rect(center=self.rect.center)

        if keys[pygame.K_w]:
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

            if pygame.sprite.collide_rect(self,game.player1.sprite):
                self.rect.x = previous_x
                self.rect.y = previous_y

        if keys[pygame.K_s]:
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

            if pygame.sprite.collide_rect(self,game.player1.sprite):
                self.rect.x = previous_x
                self.rect.y = previous_y

    def update(self):
        self.player_input()
        self.mask = pygame.mask.from_surface(self.image)
        self.hit_rect.center = self.rect.center

    
    def death(self):
        new_coordinates = (randint(41,759), randint(100,509))
        self.rect.center = new_coordinates
