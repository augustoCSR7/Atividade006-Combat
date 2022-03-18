import config
import pygame
import layouts
import tank
import bullet


class Game:
    def __init__(self):

        self.level_select = True

        self.game_stop = False

        self.pause = False

        self.level_number = 1

        self.layouts = layouts.Layouts(self.level_number)

        self.tank1 = tank.Tank(1)
        self.tank2 = tank.Tank(2)

        self.player1 = pygame.sprite.GroupSingle(self.tank1)
        self.player2 = pygame.sprite.GroupSingle(self.tank2)

        self.p1_bullet = pygame.sprite.GroupSingle()
        self.p2_bullet = pygame.sprite.GroupSingle()

        self.score1 = 0
        self.score2 = 0

        self.start_time = 0

        self.end_time = 0

        self.remaining_time = 0

    def draw_elements(self, screen: pygame.Surface):
        screen.fill(self.layouts.bg_color)

        if self.pause is not True:
            if self.level_select is not True:
                self.player1.draw(screen)
                self.player2.draw(screen)

                self.p1_bullet.draw(screen)
                self.p2_bullet.draw(screen)

                self.show_score(screen)
                if self.game_stop is not True:
                    self.player1.update()
                    self.player2.update()

                    self.p1_bullet.update()
                    self.p2_bullet.update()

            else:
                self.show_layout_number(screen)

            self.layouts.group.draw(screen)

        else:
            self.show_pause_texts(screen)

    def check_collisions(self):
        self.tank_wall_collision()
        self.bullet_tank_collision()
        self.bullet_wall_collision()
        self.tanks_collision()

    def check_events(self):

        if self.end_time < pygame.time.get_ticks():
            self.game_stop = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if self.pause is not True:
                    if self.level_select is True:
                        if event.key == pygame.K_LEFT:
                            self.change_layout(-1)

                        if event.key == pygame.K_RIGHT:
                            self.change_layout(1)

                        if event.key == pygame.K_SPACE:
                            self.level_select = False
                            self.game_stop = False

                            self.start_time = pygame.time.get_ticks()
                            self.end_time = self.start_time + config.game_time

                    else:
                        if event.key == pygame.K_ESCAPE:
                            self.pause = True
                            self.remaining_time = self.end_time - pygame.time.get_ticks()

                        if event.key == pygame.K_RCTRL:
                            self.shot_bullet(1)

                        if event.key == pygame.K_LSHIFT:
                            self.shot_bullet(2)

                        if event.key == pygame.K_r:
                            self.reset()

                else:
                    if event.key == pygame.K_ESCAPE:
                        self.pause = False
                        self.start_time = pygame.time.get_ticks()
                        self.end_time = self.start_time + self.remaining_time

                    if event.key == pygame.K_SPACE:
                        self.pause = False
                        self.level_select = True
                        self.reset()

    def change_layout(self, direction: int):
        self.level_number += direction

        if self.level_number < 1:
            self.level_number = config.number_of_layouts
        elif self.level_number > config.number_of_layouts:
            self.level_number = 1

        self.layouts.set_layout(self.level_number)

    def show_score(self, screen: pygame.Surface):

        text = config.font1.render(str(self.score1), False, "#9D4844")
        screen.blit(text, (250, -15))

        text = config.font1.render(str(self.score2), False, config.BLUE)
        screen.blit(text, (550, -15))

    def show_layout_number(self, screen: pygame.Surface):
        text = config.font1.render(str(self.level_number), False, config.GREEN)
        screen.blit(text, (250, -15))

    @staticmethod
    def show_pause_texts(screen: pygame.Surface):
        text = config.font1.render("Paused", True, "White")
        text_rect = text.get_rect(center=(config.screen_width / 2, 150))
        screen.blit(text, text_rect)

        text = config.font2.render("Press 'esc' to resume game", True, "White")
        text_rect = text.get_rect(center=(config.screen_width / 2, 350))
        screen.blit(text, text_rect)

        text = config.font2.render("Press 'space' to select another level", True, "White")
        text_rect = text.get_rect(center=(config.screen_width / 2, 400))
        screen.blit(text, text_rect)

    def reset(self):
        self.tank1 = tank.Tank(1)
        self.tank2 = tank.Tank(2)

        self.player1.add(self.tank1)
        self.player2.add(self.tank2)

        self.score1 = 0
        self.score2 = 0

        self.game_stop = False

        self.start_time = pygame.time.get_ticks()
        self.end_time = self.start_time + config.game_time

    def shot_bullet(self, player: int):
        if player == 1 and len(self.p1_bullet.sprites()) == 0:
            model = self.player1.sprite.sprite_model
            coordinates = self.player1.sprite.rect.center

            self.p1_bullet.add(bullet.Bullet(model, coordinates, "#537AD7"))
            config.tank_shot.play()
        elif player == 2 and len(self.p2_bullet.sprites()) == 0:
            model = self.player2.sprite.sprite_model
            coordinates = self.player2.sprite.rect.center

            self.p2_bullet.add(bullet.Bullet(model, coordinates, "#9D4844"))
            config.tank_shot.play()

    def tank_wall_collision(self):
        tanks = [self.tank1, self.tank2]

        for player in tanks:
            collision = pygame.sprite.spritecollide(player, self.layouts.group, False, config.collide_hit_rect)

            if collision:

                for wall in collision:
                    # Check the coordinates which collided with the ball
                    bottom_collision = player.hit_rect.bottom - wall.rect.top
                    top_collision = wall.rect.bottom - player.hit_rect.top
                    right_collision = wall.rect.right - player.hit_rect.left
                    left_collision = player.hit_rect.right - wall.rect.left

                    # Changes the ball direction by the position where it collided
                    if bottom_collision <= 6:
                        player.hit_rect.bottom = wall.rect.top - 3

                    if top_collision <= 6:
                        player.hit_rect.top = wall.rect.bottom + 3

                    if left_collision <= 6:
                        player.hit_rect.right = wall.rect.left - 3

                    if right_collision <= 6:
                        player.hit_rect.left = wall.rect.right + 3

                    player.rect.center = player.hit_rect.center

    def bullet_tank_collision(self):
        tanks = [self.tank1, self.tank2]
        bullets = [self.p2_bullet, self.p1_bullet]
        scores = [self.score2, self.score1]

        for i in range(2):
            if tanks[i].dead is True:
                # Checks if the tank has collided with a wall or the other, to change coordinates
                if pygame.sprite.spritecollide(tanks[i], self.layouts.group, False, config.collide_hit_rect):
                    tanks[i].death()

            else:
                collision = pygame.sprite.spritecollide(tanks[i], bullets[i], True, pygame.sprite.collide_mask)

                if collision:
                    tanks[i].death()
                    config.tank_death.play()
                    scores[i] += 1

        self.score1 = scores[1]
        self.score2 = scores[0]

    def bullet_wall_collision(self):
        if len(self.p1_bullet.sprites()) != 0:
            self.p1_bullet.sprite.check_collision(self.layouts.group)

        if len(self.p2_bullet.sprites()) != 0:
            self.p2_bullet.sprite.check_collision(self.layouts.group)

    def tanks_collision(self):

        if pygame.sprite.collide_rect(self.tank1, self.tank2):
            self.tank1.go_to_previous_coordinates()
            self.tank2.go_to_previous_coordinates()
