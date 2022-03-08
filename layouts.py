import pygame
import wall
import config

class Layouts:
    def __init__(self):
        self.group = pygame.sprite.Group()
        self.wall_color = None
        self.bg_color = None
        self.layout1()
        self.rectangle()

    def get_group(self):
        return self.group

    def get_bg_color(self):
        return self.bg_color

    def rectangle(self):
        for i in range(13,config.screen_width,26):
            self.group.add(wall.Wall(self.wall_color,(26,26),(i,70)))
            self.group.add(wall.Wall(self.wall_color,(26,26),(i,537)))

        for i in range(70,config.screen_height,26):
            self.group.add(wall.Wall(self.wall_color,(26,26),(13,i)))
            self.group.add(wall.Wall(self.wall_color,(26,26),(787,i)))

    def layout1(self):
        self.wall_color = "#EE9A50"
        self.bg_color = "#8A963B"

        self.group.add(wall.Wall(self.wall_color,config.RECT7,(400 + 100, 308)))
        self.group.add(wall.Wall(self.wall_color,config.RECT7,(400 - 100, 308)))

        self.group.add(wall.Wall(self.wall_color,config.RECT8,(400, 203)))
        self.group.add(wall.Wall(self.wall_color,config.RECT8,(400, 403)))

        self.group.add(wall.Wall(self.wall_color,config.RECT5,(650,303)))
        self.group.add(wall.Wall(self.wall_color,config.RECT5,(150,303)))

        self.group.add(wall.Wall(self.wall_color,config.RECT1,(670,259)))
        self.group.add(wall.Wall(self.wall_color,config.RECT1,(670,347)))

        self.group.add(wall.Wall(self.wall_color,config.RECT1,(130,259)))
        self.group.add(wall.Wall(self.wall_color,config.RECT1,(130,347)))

    def layout2(self):
        self.wall_color = "#D8A93F"
        self.bg_color = "#902608"

        self.group.add(wall.Wall(self.wall_color,config.RECT9,(650,303)))
        self.group.add(wall.Wall(self.wall_color,config.RECT9,(150,303)))

        self.group.add(wall.Wall(self.wall_color,config.RECT4,(400, 509)))
        self.group.add(wall.Wall(self.wall_color,config.RECT4,(400, 98)))

        self.group.add(wall.Wall(self.wall_color,config.RECT1,(670,229)))
        self.group.add(wall.Wall(self.wall_color,config.RECT1,(670,377)))

        self.group.add(wall.Wall(self.wall_color,config.RECT1,(130,229)))
        self.group.add(wall.Wall(self.wall_color,config.RECT1,(130,377)))

        self.group.add(wall.Wall(self.wall_color,config.RECT1,(291,407)))
        self.group.add(wall.Wall(self.wall_color,config.RECT2,(311,427)))

        self.group.add(wall.Wall(self.wall_color,config.RECT1,(509,407)))
        self.group.add(wall.Wall(self.wall_color,config.RECT2,(489,427)))

        self.group.add(wall.Wall(self.wall_color,config.RECT1,(291,199)))
        self.group.add(wall.Wall(self.wall_color,config.RECT2,(311,179)))

        self.group.add(wall.Wall(self.wall_color,config.RECT1,(509,199)))
        self.group.add(wall.Wall(self.wall_color,config.RECT2,(489,179)))

        self.group.add(wall.Wall(self.wall_color,config.RECT4,(225,303)))
        self.group.add(wall.Wall(self.wall_color,config.RECT4,(565,303)))

        self.group.add(wall.Wall(self.wall_color,config.RECT2,(180,131)))
        self.group.add(wall.Wall(self.wall_color,config.RECT2,(620,131)))
        self.group.add(wall.Wall(self.wall_color,config.RECT2,(180,466)))
        self.group.add(wall.Wall(self.wall_color,config.RECT2,(620,466)))
