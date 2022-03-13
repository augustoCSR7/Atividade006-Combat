import pygame
import bullet
import config
import layouts
import blue_tank
import red_tank

# Initializinh screen
screen = config.initialize_screen()

# Defining the background color variable
background = None

level_select = True

game_stop = False

level_number = 1

start_time = 0
end_time = 0
remaining_time = 0

# Wall group
walls = pygame.sprite.Group()

# Players groups
player1 = pygame.sprite.GroupSingle(blue_tank.Blue_tank())
player2 = pygame.sprite.GroupSingle(red_tank.Red_tank())

p1_bullet = pygame.sprite.GroupSingle()
p2_bullet = pygame.sprite.GroupSingle()

# Players Scores
pontos1 = 0
pontos2 = 0
font = pygame.font.Font('./font/Gamer.ttf',80)
font2 = pygame.font.Font('./font/Gamer.ttf',50)
Mens_pontos1 = f'{pontos1}'
Mens_pontos1format = font.render(Mens_pontos1, False, "#9D4844")
Mens_pontos2 = f'{pontos2}'
Mens_pontos2format = font.render(Mens_pontos2, False, config.BLUE)

pygame.sprite.collide_rect_ratio(0.3)

pause = False

def update_score(player):

    if player == 1:
        global pontos1, Mens_pontos1, Mens_pontos1format
        pontos1 += 1

        Mens_pontos1 = f'{pontos1}'
        Mens_pontos1format = font.render(Mens_pontos1, False, "#9D4844")

    if player == 2:
        global pontos2, Mens_pontos2, Mens_pontos2format
        pontos2 += 1

        Mens_pontos2 = f'{pontos2}'
        Mens_pontos2format = font.render(Mens_pontos2, False, config.BLUE)


# Check if an event happens
def check_events():
    global pause, level_select, level_number
    global start_time, end_time, remaining_time, game_stop

    if end_time - pygame.time.get_ticks() < 0:
        game_stop = True

    for event in pygame.event.get():
        # Check if the user wants to exit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            
            if level_select is True:
                if event.key == pygame.K_SPACE:
                    level_select = False
                    game_stop = False

                    start_time = pygame.time.get_ticks()
                    end_time = start_time + config.game_time

                if event.key == pygame.K_LEFT:
                    level_number -= 1
                    if level_number < 1: 
                        level_number = config.number_of_layouts
                    get_layout(level_number)

                if event.key == pygame.K_RIGHT:
                    level_number += 1
                    if level_number > config.number_of_layouts:
                        level_number = 1
                    get_layout(level_number)
            else:
                if event.key == pygame.K_ESCAPE:
                        pause = True
                        remaining_time = end_time - pygame.time.get_ticks()

                if event.key == pygame.K_RCTRL:
                    shot_bullet(1)
                if event.key == pygame.K_LSHIFT:
                    shot_bullet(2)

                if event.key == pygame.K_r:
                    reset_game()


def reset_game():
    global player1,player2,pontos1,pontos2
    global Mens_pontos1, Mens_pontos1format
    global Mens_pontos2, Mens_pontos2format

    player1.add(blue_tank.Blue_tank())
    player2.add(red_tank.Red_tank())

    pontos1 = 0
    pontos2 = 0
    Mens_pontos1 = f'{pontos1}'
    Mens_pontos1format = font.render(Mens_pontos1, False, "#9D4844")
    Mens_pontos2 = f'{pontos2}'
    Mens_pontos2format = font.render(Mens_pontos2, False, config.BLUE)

def pause_game():
    global pause, level_select, start_time
    global remaining_time, end_time
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False
                    start_time = pygame.time.get_ticks()
                    end_time = start_time + remaining_time

                if event.key == pygame.K_SPACE:
                    pause = False
                    level_select = True
                    reset_game()

        screen.fill(background)

        text = font.render("Paused", True, "White")
        text_rect = text.get_rect(center=(config.screen_width / 2, 150))
        screen.blit(text, (text_rect))

        text = font2.render("Press 'esc' to resume game", True, "White")
        text_rect = text.get_rect(center=(config.screen_width / 2, 350))
        screen.blit(text, (text_rect))

        text = font2.render("Press 'space' to select another level", True, "White")
        text_rect = text.get_rect(center=(config.screen_width / 2, 400))
        screen.blit(text, (text_rect))

        pygame.display.update()


# Gets the chosen layout
def get_layout(layout_type):
    global background, walls

    # the parameter defines which layout is displayed
    layout = layouts.Layouts(layout_type)

    # Defines the background color
    background = layout.get_bg_color()

    # Gets the group with all the walls
    walls = layout.get_group()


# Draws all the screen elements
def draw_sprites():
    global walls, background, level_number,game_stop

    # Fills the background
    screen.fill(background)

    if level_select is not True:
        # Shows Score
        screen.blit(Mens_pontos1format,(250,-15))
        screen.blit(Mens_pontos2format,(550,-15))

        # Shows the bullets
        p1_bullet.draw(screen)
        p2_bullet.draw(screen)

        # Show players sprites
        player1.draw(screen)

        player2.draw(screen)
        
        if game_stop is not True:
            p1_bullet.update()
            p2_bullet.update()
            player1.update()
            player2.update()
            

    else:
        level_text = f'{level_number}'
        level_text_on_screen = font.render(level_text, False, config.BLUE)
        screen.blit(level_text_on_screen,(250,-15))

    # Draw the walls
    walls.draw(screen)

def check_collisions():
    bullet_wall_collision()

    bullet_tank_collision()

    tank_wall_collision()


# Check collision between the ball and a wall
def bullet_wall_collision():
    global p1_bullet,p2_bullet, walls

    if len(p1_bullet.sprites()) != 0:
        # Get a list with all the collisions that happened
        collision = pygame.sprite.spritecollide(p1_bullet.sprite,walls,False)

        # If a collision happened, then
        if collision:
            # For wall that was colided
            for wall in collision:
                # Check the coordinates which colidded with the ball
                bottom_collision = p1_bullet.sprite.rect.bottom - wall.rect.top
                top_collision = wall.rect.bottom - p1_bullet.sprite.rect.top
                right_collision = wall.rect.right - p1_bullet.sprite.rect.left
                left_collision = p1_bullet.sprite.rect.right - wall.rect.left

                player_x = p1_bullet.sprite.dx if p1_bullet.sprite.dx >=0 else -1 * p1_bullet.sprite.dx
                player_y = p1_bullet.sprite.dy if p1_bullet.sprite.dy >=0 else -1 * p1_bullet.sprite.dy

                # Changes the ball direction by the position where it collided
                if bottom_collision <= player_y or top_collision <= player_y:
                    p1_bullet.sprite.dy *= -1
                
                if left_collision <= player_x or right_collision <= player_x:
                    p1_bullet.sprite.dx *= -1
        
    if len(p2_bullet.sprites()) != 0:
        # Get a list with all the collisions that happened
        collision = pygame.sprite.spritecollide(p2_bullet.sprite,walls,False)

        # If a collision happened, then
        if collision:
            # For wall that was colided
            for wall in collision:
                # Check the coordinates which colidded with the ball
                bottom_collision = p2_bullet.sprite.rect.bottom - wall.rect.top
                top_collision = wall.rect.bottom - p2_bullet.sprite.rect.top
                right_collision = wall.rect.right - p2_bullet.sprite.rect.left
                left_collision = p2_bullet.sprite.rect.right - wall.rect.left

                player_x = p2_bullet.sprite.dx if p2_bullet.sprite.dx >=0 else -1 * p2_bullet.sprite.dx
                player_y = p2_bullet.sprite.dy if p2_bullet.sprite.dy >=0 else -1 * p2_bullet.sprite.dy

                # Changes the ball direction by the position where it collided
                if bottom_collision <= player_y or top_collision <= player_y:
                    p2_bullet.sprite.dy *= -1
                
                if left_collision <= player_x or right_collision <= player_x:
                    p2_bullet.sprite.dx *= -1


def shot_bullet(player):
    global p1_bullet, p2_bullet

    if player == 1 and len(p1_bullet.sprites()) == 0:
        model = player1.sprite.sprite_model
        coordinates = player1.sprite.rect.center

        p1_bullet.add(bullet.Bullet(model,coordinates,"#537AD7"))

    elif player == 2 and len(p2_bullet.sprites()) == 0:
        model = player2.sprite.sprite_model
        coordinates = player2.sprite.rect.center

        p2_bullet.add(bullet.Bullet(model,coordinates,"#9D4844"))


def bullet_tank_collision():
    collision = pygame.sprite.spritecollide(player1.sprite,p2_bullet,True,pygame.sprite.collide_mask)

    if collision:
        player1.sprite.death()
        update_score(1)

    collision = pygame.sprite.spritecollide(player2.sprite,p1_bullet,True,pygame.sprite.collide_mask)

    if collision:
        player2.sprite.death()
        update_score(2)



def tank_wall_collision():
    collision = pygame.sprite.spritecollide(player1.sprite,walls,False,config.collide_hit_rect)

    if collision:

        for wall in collision:
            # Check the coordinates which colidded with the ball
            bottom_collision = player1.sprite.hit_rect.bottom - wall.rect.top
            top_collision = wall.rect.bottom - player1.sprite.hit_rect.top
            right_collision = wall.rect.right - player1.sprite.hit_rect.left
            left_collision= player1.sprite.hit_rect.right - wall.rect.left

            

            # Changes the ball direction by the position where it collided
            if bottom_collision <= 6:
                player1.sprite.hit_rect.bottom = wall.rect.top - 3
                
            if top_collision <= 6:
                player1.sprite.hit_rect.top = wall.rect.bottom + 3
            
            if left_collision <= 6:
                player1.sprite.hit_rect.right = wall.rect.left - 3
                
            if right_collision <= 6:
                player1.sprite.hit_rect.left = wall.rect.right + 3
            
            player1.sprite.rect.center = player1.sprite.hit_rect.center

    collision = pygame.sprite.spritecollide(player2.sprite,walls,False,config.collide_hit_rect)

    if collision:
        
        for wall in collision:
            # Check the coordinates which colidded with the ball
            bottom_collision = player2.sprite.hit_rect.bottom - wall.rect.top
            top_collision = wall.rect.bottom - player2.sprite.hit_rect.top
            right_collision = wall.rect.right - player2.sprite.hit_rect.left
            left_collision= player2.sprite.hit_rect.right - wall.rect.left

            

            # Changes the ball direction by the position where it collided
            if bottom_collision <= 6:
                player2.sprite.hit_rect.bottom = wall.rect.top - 3
                
            if top_collision <= 6:
                player2.sprite.hit_rect.top = wall.rect.bottom + 3
            
            if left_collision <= 6:
                player2.sprite.hit_rect.right = wall.rect.left - 3
                
            if right_collision <= 6:
                player2.sprite.hit_rect.left = wall.rect.right + 3
            
            player2.sprite.rect.center = player2.sprite.hit_rect.center
