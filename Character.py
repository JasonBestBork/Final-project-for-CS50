import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.img_list = pg.transform.scale_by(pg.image.load("Character.png").convert_alpha(), 1)
        self.rect = self.img_list.get_rect(center = (100,100))
        self.velocity_y = 0
        self.gravity = 13
        self.player_speed = 240
        self.update_on = False


    def update(self,dt):
      if self.update_on:
            self.velocity_y += self.gravity * dt
            self.rect.y += self.velocity_y

            if self.rect.y <= 0:
                self.rect.y = 0
                self.player_speed = 0
            elif self.rect.y > 0 and self.player_speed == 0:
                self.player_speed = 260


    def fly(self,dt):
        self.velocity_y = -self.player_speed * dt



