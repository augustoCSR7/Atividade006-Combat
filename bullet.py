import pygame
import config


class Bullet(pygame.sprite.Sprite):
    def __init__(self, sprite_model, coordinates, color):
        super().__init__()

        self.image = pygame.Surface((5, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=coordinates)

        self.mask = pygame.mask.from_surface(self.image)

        self.sprite_model = sprite_model

        self.dx = 0
        self.dy = 0

        self.set_direction()

        self.death_time = pygame.time.get_ticks() + config.bullet_on_screen

    def movements(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def update(self):
        self.movements()
        self.check_death()
        self.mask = pygame.mask.from_surface(self.image)

    def check_death(self):
        if pygame.time.get_ticks() >= self.death_time:
            self.kill()

    def set_direction(self):
        if self.sprite_model == 0:
            self.dy = -3 * 2
            self.dx = 0 * 2
        elif self.sprite_model == 1:
            self.dy = -3 * 2
            self.dx = -1 * 2
        elif self.sprite_model == 2:
            self.dy = -3 * 2
            self.dx = -2 * 2
        elif self.sprite_model == 3:
            self.dy = -3 * 2
            self.dx = -3 * 2
        elif self.sprite_model == 4:
            self.dy = -2 * 2
            self.dx = -3 * 2
        elif self.sprite_model == 5:
            self.dy = -1 * 2
            self.dx = -3 * 2
        elif self.sprite_model == 6:
            self.dy = 0 * 2
            self.dx = -3 * 2
        elif self.sprite_model == 7:
            self.dy = 1 * 2
            self.dx = -3 * 2
        elif self.sprite_model == 8:
            self.dy = 2 * 2
            self.dx = -3 * 2
        elif self.sprite_model == 9:
            self.dy = 3 * 2
            self.dx = -3 * 2
        elif self.sprite_model == 10:
            self.dy = 3 * 2
            self.dx = -2 * 2
        elif self.sprite_model == 11:
            self.dy = 3 * 2
            self.dx = -1 * 2
        elif self.sprite_model == 12:
            self.dy = 3 * 2
            self.dx = 0 * 2
        elif self.sprite_model == 13:
            self.dy = 3 * 2
            self.dx = 1 * 2
        elif self.sprite_model == 14:
            self.dy = 3 * 2
            self.dx = 2 * 2
        elif self.sprite_model == 15:
            self.dy = 3 * 2
            self.dx = 3 * 2
        elif self.sprite_model == 16:
            self.dy = 2 * 2
            self.dx = 3 * 2
        elif self.sprite_model == 17:
            self.dy = 1 * 2
            self.dx = 3 * 2
        elif self.sprite_model == 18:
            self.dy = 0 * 2
            self.dx = 3 * 2
        elif self.sprite_model == 19:
            self.dy = -1 * 2
            self.dx = 3 * 2
        elif self.sprite_model == 20:
            self.dy = -2 * 2
            self.dx = 3 * 2
        elif self.sprite_model == 21:
            self.dy = -3 * 2
            self.dx = 3 * 2
        elif self.sprite_model == 22:
            self.dy = -3 * 2
            self.dx = 2 * 2
        elif self.sprite_model == 23:
            self.dy = -3 * 2
            self.dx = 1 * 2

    def check_collision(self, walls: pygame.sprite.Group):
        # Get a list with all the collisions that happened
        collision = pygame.sprite.spritecollide(self, walls, False)

        # If a collision happened, then
        if collision:
            config.bullet_collision.play()

            # For wall that was collided
            for wall in collision:
                # Check the coordinates which collided with the ball
                bottom_collision = self.rect.bottom - wall.rect.top
                top_collision = wall.rect.bottom - self.rect.top
                right_collision = wall.rect.right - self.rect.left
                left_collision = self.rect.right - wall.rect.left

                player_x = self.dx if self.dx >= 0 else -1 * self.dx
                player_y = self.dy if self.dy >= 0 else -1 * self.dy

                # Changes the ball direction by the position where it collided
                if bottom_collision <= player_y or top_collision <= player_y:
                    self.dy *= -1

                if left_collision <= player_x or right_collision <= player_x:
                    self.dx *= -1
