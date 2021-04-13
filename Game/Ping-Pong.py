from pygame import *
from random import randint
from time import time as timer

win_height = 500
win_width = 700
window = display.set_mode((700,500))
display.set_caption("Pong")
clock = time.Clock()
FPS=60

background = (200, 255, 255)
mixer.init()
#mixer.music.load(pass)
#mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,size_x,size_y, player_speed):
        super().__init__()
        self.image= transform.scale(image.load(player_image),(size_x, size_y))
        self.speed =player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if self.rect.y > 0 and (keys[K_w])  :
            self.rect.y -=self.speed
        if self.rect.y < 400 and (keys[K_s])  :
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if self.rect.y > 0 and (keys[K_UP])  :
            self.rect.y -=self.speed
        if self.rect.y < 400 and (keys[K_DOWN])  :
            self.rect.y += self.speed

player1 = Player("player.png",40,250,15,100,5)
player2 = Player("player.png",660,250,15,100,5)

run = True
finish = False
while run == True:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    if not finish:
        window.fill(background)

        player1.update_l()
        player1.reset()
        player2.update_r()
        player2.reset()
        clock.tick(FPS)
        display.update()
        
    