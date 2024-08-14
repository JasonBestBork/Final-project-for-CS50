import pygame as pg
from random import randint
class Wall:
    def __init__(self, scale, move_walls):
        self.wall_1 = pg.transform.scale_by(pg.image.load("Wall.png").convert_alpha(), scale)
        self.wall_2 = pg.transform.scale_by(pg.image.load("Wall.png").convert_alpha(), scale)
        self.rect_1 = self.wall_1.get_rect()
        self.rect_2 = self.wall_2.get_rect()
        self.wall_distance = 170
        self.rect_1.y = randint(230,500)
        self.rect_1.x = 600
        self.rect_2.y = self.rect_1.y - self.wall_distance - self.rect_1.height
        self.rect_2.x = 600
        self.move_walls = move_walls

    def draw_wall(self, win):
        win.blit(self.wall_1, self.rect_1)
        win.blit(self.wall_2, self.rect_2)
        
    def update(self, dt):
        self.rect_1.x -= int(self.move_walls * dt)
        self.rect_2.x -= int(self.move_walls * dt)