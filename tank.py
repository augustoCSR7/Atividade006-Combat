import pygame
# import game
import config
from random import randint


class Tank(pygame.sprite.Sprite):
    def __init__(self, tank_type: int):
        super().__init__()

        self.tank_type = tank_type

        if tank_type == 1:
            # Sets the first image and resizes it to 0.8 its size
            self.tank_sprites = config.BLUE_TANK
            self.image = pygame.image.load(self.tank_sprites[6]).convert_alpha()
            self.resize_tank()

            # Sets the sprite rect based on the image size
            self.rect = self.image.get_rect(center=(700, 300))

            # Controls the tank rotation
            self.sprite_model = 6

        elif tank_type == 2:
            # Sets the first image and resizes it to 0.8 its size
            self.tank_sprites = config.RED_TANK
            self.image = pygame.image.load(self.tank_sprites[18]).convert_alpha()
            self.resize_tank()

            # Sets the sprite rect based on the image size
            self.rect = self.image.get_rect(center=(100, 300))

            # Controls the tank rotation
            self.sprite_model = 18

        # sets the keys for movement depending on the tank_type
        self.keys = dict()
        self.set_movement_keys(tank_type)

        # Sets the previous coordinates to 
        # check collision between tanks
        self.previous_x = self.rect.x
        self.previous_y = self.rect.y

        # Creates a "hit rect" to deal with wall collision
        # and set its center as the rect center
        self.hit_rect = pygame.Rect(0, 0, 35, 35)
        self.hit_rect.center = self.rect.center

        # Defines a mask from the actual image on screen
        self.mask = pygame.mask.from_surface(self.image)

        # Checks if the tank is dead
        self.dead = False
        self.cont = 0

    def player_input(self):
        # Get the pressed keys
        pressed_keys = pygame.key.get_pressed()

        # rotates the tank if the key is left or right
        if pressed_keys[self.keys["right"]] or pressed_keys[self.keys["left"]]:

            config.tank_walk.play()

            if pressed_keys[self.keys["right"]]:
                self.sprite_model -= 1
            else:
                self.sprite_model += 1

            if pressed_keys[self.keys["right"]]:
                if self.sprite_model < 0:
                    self.sprite_model = 23
            else:
                if self.sprite_model > 23:
                    self.sprite_model = 0

            self.image = pygame.image.load(self.tank_sprites[self.sprite_model]).convert_alpha()

            self.resize_tank()
            self.rect = self.image.get_rect(center=self.rect.center)

            # Updates the mask with the actual image on screen
            self.update_mask()

        # Moves the tank if the key is up or down
        if pressed_keys[self.keys["up"]] or pressed_keys[self.keys["down"]]:
            config.tank_walk.play()

            self.previous_x = self.rect.x
            self.previous_y = self.rect.y

            add_x = 0
            add_y = 0

            if self.sprite_model == 0:
                add_y = -3
            elif self.sprite_model == 1:
                add_y = -3
                add_x = -1
            elif self.sprite_model == 2:
                add_y = -3
                add_x = -2
            elif self.sprite_model == 3:
                add_y = -3
                add_x = -3
            elif self.sprite_model == 4:
                add_y = -2
                add_x = -3
            elif self.sprite_model == 5:
                add_y = -1
                add_x = -3
            elif self.sprite_model == 6:
                add_x = -3
            elif self.sprite_model == 7:
                add_y = 1
                add_x = -3
            elif self.sprite_model == 8:
                add_y = 2
                add_x = -3
            elif self.sprite_model == 9:
                add_y = 3
                add_x = -3
            elif self.sprite_model == 10:
                add_y = 3
                add_x = -2
            elif self.sprite_model == 11:
                add_y = 3
                add_x = -1
            elif self.sprite_model == 12:
                add_y = 3
            elif self.sprite_model == 13:
                add_y = 3
                add_x = 1
            elif self.sprite_model == 14:
                add_y = 3
                add_x = 2
            elif self.sprite_model == 15:
                add_y = 3
                add_x = 3
            elif self.sprite_model == 16:
                add_y = 2
                add_x = 3
            elif self.sprite_model == 17:
                add_y = 1
                add_x = 3
            elif self.sprite_model == 18:
                add_x = 3
            elif self.sprite_model == 19:
                add_x = 3
                add_y = -1
            elif self.sprite_model == 20:
                add_x = 3
                add_y = -2
            elif self.sprite_model == 21:
                add_x = 3
                add_y = -3
            elif self.sprite_model == 22:
                add_x = 2
                add_y = -3
            elif self.sprite_model == 23:
                add_x = 1
                add_y = -3

            if pressed_keys[self.keys["down"]]:
                add_x *= -1
                add_y *= -1

            self.rect.x += add_x
            self.rect.y += add_y

            '''# Check if a tank collides with another
            if pygame.sprite.collide_rect(self, game.player2.sprite):
                self.rect.x = previous_x
                self.rect.y = previous_y'''

    def update(self):
        # Updates the hit_rect center to follow the rect center
        self.hit_rect.center = self.rect.center

        if self.dead is True:
            # Spin the tank
            self.spin()

        else:
            self.player_input()

    def update_mask(self):
        self.mask = pygame.mask.from_surface(self.image)

    # Function for when the tank gets shot
    def death(self):
        # Set a new randon location
        new_coordinates = (randint(41, 759), randint(100, 509))
        self.rect.center = new_coordinates

        self.hit_rect.center = self.rect.center
        self.dead = True

    # Spin the tank
    def spin(self):

        self.sprite_model += 1

        if self.sprite_model > 23:
            self.sprite_model = 0

        if self.tank_type == 1:
            self.image = pygame.image.load(config.BLUE_TANK[self.sprite_model]).convert_alpha()
        else:
            self.image = pygame.image.load(config.RED_TANK[self.sprite_model]).convert_alpha()

        self.resize_tank()
        self.rect = self.image.get_rect(center=self.rect.center)
        self.update_mask()

        self.cont += 1

        # Stop spinning the tank
        if self.cont == 100:
            self.cont = 0
            self.dead = False

    def resize_tank(self):
        width = self.image.get_width() // 1.2
        height = self.image.get_height() // 1.2
        self.image = pygame.transform.scale(self.image, (width, height)).convert_alpha()

    def set_movement_keys(self, tank_type):
        if tank_type == 1:
            self.keys = {
                "up": pygame.K_UP,
                "down": pygame.K_DOWN,
                "left": pygame.K_LEFT,
                "right": pygame.K_RIGHT
            }
        elif tank_type == 2:
            self.keys = {
                "up": pygame.K_w,
                "down": pygame.K_s,
                "left": pygame.K_a,
                "right": pygame.K_d
            }

    def go_to_previous_coordinates(self):
        self.rect.x = self.previous_x
        self.rect.y = self.previous_y
