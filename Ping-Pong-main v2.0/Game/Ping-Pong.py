from pygame import *
from random import randint
from time import time as timer



window = display.set_mode((600,400))#700,500
display.set_caption("Pong")
clock = time.Clock()
FPS=60

background = image.load('background.jpg')
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
        if self.rect.y < 305 and (keys[K_s])  :
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if self.rect.y > 0 and (keys[K_UP])  :
            self.rect.y -=self.speed
        if self.rect.y < 305 and (keys[K_DOWN])  :
            self.rect.y += self.speed

speed_x = 3
speed_y = 3
p1w = 0
p2w = 0

font.init()
font = font.Font(None,35)
lose1 = font.render('PLAYER 1 LOSE!',True,(180,0,0))
lose2 = font.render('PLAYER 2 LOSE!',True,(180,0,0))


ball = GameSprite('ball.png',300,200,20,20,4)
player1 = Player("player.png",40,250,15,100,5)
player2 = Player("player.png",540,250,15,100,5)






run = True
finish = False
while run == True:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    if not finish:
        window.blit(background,(0, 0))

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            speed_x *= -1


        if ball.rect.y > 350 or ball.rect.y <0:
            speed_y *= -1

        if ball.rect.x <0 :
            window.blit(lose1,(100,200))
            p2w +=1
            finish = True
        if ball.rect.x >600 :
            window.blit(lose2,(300,200))
            p1w +=1
            finish = True

        window.blit(font.render(str(p1w)+' : '+ str(p2w),True,(180,90,90)),(250,50))
        ball.update()
        ball.reset()
        player1.update_l()
        player1.reset()
        player2.update_r()
        player2.reset()
        clock.tick(FPS)
        display.update()
    else: 
        
        ball.rect.x = 300
        ball.rect.y = 200
        time.delay(3000) 
        finish = False       
    