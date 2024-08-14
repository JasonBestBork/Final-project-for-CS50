import pygame as pg
import sys, time
from Character import Player
from walls import Wall
pg.init()

class Game:
    def __init__(self):
        #window config
        self.scale_factor = 1.5
        self.width = 600
        self.height = 768
        self.win = pg.display.set_mode((self.width, self.height))
        #load pictures 
        self.bg_img = pg.image.load("Background.png").convert()
        self.ground_img = pg.image.load("Floor.png").convert()
        self.ground_img2 = pg.image.load("Floor.png").convert()
        #set ground position
        self.ground_rect = self.ground_img.get_rect()
        self.ground_rect.x = 0
        self.ground_rect.y = 600

        self.ground_rect2 = self.ground_img.get_rect()
        self.ground_rect2.x = self.ground_rect.right #we connect ground 2 to the right of ground 1 for looping 
        self.ground_rect2.y = 600
        #set up speed
        self.move_speed = 300
        #initialize player
        self.player = Player()
        self.enter_hit = False
        #initialize walls
        self.walls = []
        self.Wall_counter = 71

        self.score = 0
        self.font = pg.font.Font("Starjedi.ttf", 24)
        self.text = self.font.render("Score: 0", True, (255,0,0))
        self.score_text = self.text.get_rect(center=(70,30))
        self.checking = False
        self.FPS = 60
        

        self.gameLoop()
        
        
        

    def update(self, delta_time):
            if self.enter_hit:
                self.ground_rect.x -= int(self.move_speed*delta_time)
                self.ground_rect2.x -= int(self.move_speed*delta_time)

                if self.ground_rect.right<0:
                    self.ground_rect.x = self.ground_rect2.right
                if self.ground_rect2.right<0:
                    self.ground_rect2.x = self.ground_rect.right

                if self.Wall_counter > 70:
                    self.walls.append(Wall(self.scale_factor, self.move_speed))
                    self.Wall_counter = 0
                self.Wall_counter += 1


                for wall in self.walls:
                 wall.update(delta_time)

                if len(self.walls) != 0:
                    if self.walls[0].rect_1.right<0:
                        self.walls.pop(0)


            self.player.update(delta_time)



    def gameLoop(self):
        clock = pg.time.Clock()
        last_time = time.time()
        while True:
           clock.tick(self.FPS)
           #delta time calculation
           new_time = time.time()
           delta_time = new_time - last_time
           last_time = new_time

           for event in pg.event.get():
               if event.type == pg.QUIT:
                   pg.quit()
                   sys.exit()
               if event.type == pg.KEYDOWN:
                   if event.key == pg.K_RETURN:
                       self.enter_hit = True
                       self.player.update_on = True
                   if event.key == pg.K_SPACE:
                       self.player.fly(delta_time)
           self.CollisionCheck()
           self.drawWorld()
           self.update(delta_time)
           self.Score()
           pg.display.update()


    def CollisionCheck(self):
        if len(self.walls):
            if self.player.rect.bottom>600:
                self.player.update_on = False
                self.enter_hit = False
            if ( self.player.rect.colliderect(self.walls[0].rect_1) or self.player.rect.colliderect(self.walls[0].rect_2)):
                self.enter_hit = False
               

    def Score(self):
        if len(self.walls) > 0:
            if (self.player.rect.left > self.walls[0].rect_2.left and self.player.rect.right < self.walls[0].rect_2.right and not self.checking):
                self.checking = True
            if self.player.rect.left > self.walls[0].rect_2.right and self.checking:
                self.checking = False
                self.score += 1
                self.text = self.font.render(f"Score: {self.score}", True, (255,0,0))






    def drawWorld(self):
        self.win.blit(self.bg_img,(0,0))
        for wall in self.walls:
         wall.draw_wall(self.win)
        self.win.blit(self.ground_img,self.ground_rect)
        self.win.blit(self.ground_img2,self.ground_rect2)
        self.win.blit(self.player.img_list, self.player.rect)
        self.win.blit(self.text, self.score_text)
      

game = Game()
