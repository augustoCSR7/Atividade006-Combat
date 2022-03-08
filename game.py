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

# Wall group
walls = pygame.sprite.Group()

# Ball group (to test collision)
bullet = pygame.sprite.GroupSingle(bullet.Bullet())

# Players groups
player1 = pygame.sprite.GroupSingle(blue_tank.Blue_tank())
player2 = pygame.sprite.GroupSingle(red_tank.Red_tank())

# Players Scores
pontos1 = 0
pontos2 = 0
font = pygame.font.Font('./font/Gamer.ttf',80)
Mens_pontos1 = f'{pontos1}'
Mens_pontos1format = font.render(Mens_pontos1, False, config.GREEN)
Mens_pontos2 = f'{pontos2}'
Mens_pontos2format = font.render(Mens_pontos2, False, config.BLUE)


# Check if an event happens
def check_events():
    for event in pygame.event.get():
        # Check if the user wants to exit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


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
    global walls, background, bullet

    # Fills the background
    screen.fill(background)

    # Shows Score
    screen.blit(Mens_pontos1format,(250,-15))
    screen.blit(Mens_pontos2format,(550,-15))

    # Show players sprites
    player1.draw(screen)
    player2.draw(screen)

    # Shows the ball
    bullet.draw(screen)
    bullet.update()

    # Draw the walls
    walls.draw(screen)


# Check collision between the ball and a wall
def check_collision():
    global bullet, walls
    # Get a list with all the collisions that happened
    collision = pygame.sprite.spritecollide(bullet.sprite,walls,False)

    # If a collision happened, then
    if collision:
        # For wall that was colided
        for wall in collision:
            # Check the coordinates which colidded with the ball
            bottom_collision = bullet.sprite.rect.bottom - wall.rect.top
            top_collision = wall.rect.bottom - bullet.sprite.rect.top
            right_collision = wall.rect.right - bullet.sprite.rect.left
            left_collision = bullet.sprite.rect.right - wall.rect.left

            # Changes the ball direction by the position where it collided
            if bottom_collision <= 2 or top_collision <= 2:
                bullet.sprite.dy *= -1
            
            if left_collision <= 2 or right_collision <= 2:
                bullet.sprite.dx *= -1
            
