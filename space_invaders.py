import pygame
from pygame.locals import*              
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Space Invaders")
clock=pygame.time.Clock()
class Character:
    def __init__(self,x,y,image,length,width):
        self.x=x
        self.y=y
        self.image=image
        self.length=length
        self.width=width

    def draw(self):
        screen.blit(self.image,(self.x,self.y))

class Alien (Character):
    def __init__(self,x,y,image,length,width,dir):
        super().__init__(x,y,image,length,width)
        self.dir=dir
    def alien_move(self):
        if self.x >= 600:
            self.dir = False
            self.y+=20
        if self.x <= 0:
            self.dir=True
            self.y+=20
        if self.dir == True:
            self.x += 1
        else:
            self.x -= 1
ltemp=[]
l=[]
x=1
y=0
for j in range(0,5,1):
    for i in range(0,10,1):
        image_var=pygame.image.load("C:\\Users\\ameyg\\Space_Invaders\\enemy_1.png")
        image_var=pygame.transform.scale(image_var,(20,20))
        ltemp.append(Alien(x,y,image_var,5,5,True))
        x+=35
    y += 35
    x=1
    l.append(ltemp)

while True:
    clock.tick(60)
    screen.fill((0,0,0))
    for i in l:
        for j in i:
            pygame.draw.rect(screen,(255,0,0),(j.x,j.y,20,20))
            j.draw()
            j.alien_move()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
    pygame.display.update()