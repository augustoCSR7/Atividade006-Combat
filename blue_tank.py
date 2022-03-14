import pygame
import game
import config
from config import BLUE_TANK
from random import randint


class BlueTank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Sets the first image and resizes it to 0.8 its size
        self.image = pygame.image.load(BLUE_TANK[6]).convert_alpha()
        width = self.image.get_width() // 1.2
        height = self.image.get_height() // 1.2
        self.image = pygame.transform.scale(self.image, (width, height)).convert_alpha()

        # Sets the sprite rect based on the image size
        self.rect = self.image.get_rect(center=(700, 300))

        # Creates a "hit rect" to deal with wall collision
        # and set its center as the rect center
        self.hit_rect = pygame.Rect(0, 0, 35, 35)
        self.hit_rect.center = self.rect.center

        # Defines a mask from the actual image on screen
        self.mask = pygame.mask.from_surface(self.image)

        # Checks if the tank is dead
        self.dead = False
        self.cont = 0

        # Controls the tank rotation
        self.sprite_model = 6

    def player_input(self):
        # Get the pressed keys
        keys = pygame.key.get_pressed()

        # rotates the tank if the key is for left or right
        if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:

            game.tank_walk.play()

            if keys[pygame.K_RIGHT]:
                self.sprite_model -= 1
            else:
                self.sprite_model += 1

            if keys[pygame.K_RIGHT]:
                if self.sprite_model < 0:
                    self.sprite_model = 23
            else:
                if self.sprite_model > 23:
                    self.sprite_model = 0

            self.image = pygame.image.load(BLUE_TANK[self.sprite_model]).convert_alpha()
            width = self.image.get_width() // 1.2
            height = self.image.get_height() // 1.2
            self.image = pygame.transform.scale(self.image, (width, height)).convert_alpha()
            self.rect = self.image.get_rect(center=self.rect.center)

        # Moves the tank if the key is up
        if keys[pygame.K_UP]:
            game.tank_walk.play()

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

            # Check if a tank collides with another
            if pygame.sprite.collide_rect(self, game.player2.sprite):
                self.rect.x = previous_x
                self.rect.y = previous_y

        # Moves the tank if the key is down
        if keys[pygame.K_DOWN]:
            game.tank_walk.play()

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

            # Check if a tank collides with another
            if pygame.sprite.collide_rect(self, game.player2.sprite):
                self.rect.x = previous_x
                self.rect.y = previous_y

    def update(self):
        # Updates the mask with the actual image on screen
        self.mask = pygame.mask.from_surface(self.image)

        # Updates the hit_rect center to follow the rect center
        self.hit_rect.center = self.rect.center

        if self.dead is True:
            # Checks if the tank has collided with a wall or the other, to change coordinates
            if pygame.sprite.spritecollide(self,
                                           game.walls, False,
                                           config.collide_hit_rect) or pygame.sprite.collide_rect(self,
                                                                                                  game.player2.sprite):
                new_coordinates = (randint(41, 759), randint(100, 509))
                self.hit_rect.center = new_coordinates
                self.rect.center = self.hit_rect.center

            # Spin the tank
            self.spin()
            self.cont += 1

            # Stop spinning the tank
            if self.cont == 100:
                self.cont = 0
                self.dead = False

        # Checks if the other player is dead, so
        # it won't move while the other is spinning
        elif game.player2.sprite.dead is not True:
            self.player_input()

    # Function for when the tank gets shot
    def death(self):
        # Set a new randon location
        new_coordinates = (randint(41, 759), randint(100, 509))
        self.rect.center = new_coordinates
        self.dead = True

    # Spin the tank
    def spin(self):
        self.sprite_model += 1

        if self.sprite_model > 23:
            self.sprite_model = 0

        self.image = pygame.image.load(BLUE_TANK[self.sprite_model]).convert_alpha()
        width = self.image.get_width() // 1.2
        height = self.image.get_height() // 1.2
        self.image = pygame.transform.scale(self.image, (width, height)).convert_alpha()
        self.rect = self.image.get_rect(center=self.rect.center)
