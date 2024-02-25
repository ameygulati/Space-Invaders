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
    def get_x(self):
        return (x)
    def get_y(self):
        return (y)

class Player_ship(Character):
    def __init__(self,x,y,image,length,width):
        super().__init__(x,y,image,length,width)
    

class Bullet(Character):
    def __init__(self, x, y, image, length, width, fire):
        super().__init__(x, y, image, length, width)
        self.fire=fire
        #self.rect=pygame.draw.rect(screen,(0,250,0),(self.x,self.y,5,10))
    def shoot(self):
        if self.fire == True:
            pygame.draw.rect(screen,(0,250,0),(self.x,self.y,7,10))
            screen.blit(self.image,(self.x,self.y))
            self.y-=5


ltemp=[]
l=[] 
x=1
y=0
move_r = False
move_l = False
for j in range(0,5,1):
    for i in range(0,10,1):
        image_var=pygame.image.load("C:\\Users\\Amey\\Downloads\\Pygames\\Space-Invaders\\enemy_1.png")
        image_var=pygame.transform.scale(image_var,(20,20))
        ltemp.append(Alien(x,y,image_var,5,5,True))
        x+=35
    y += 35
    x=1
    l.append(ltemp)

bul = pygame.image.load("C:\\Users\\Amey\\Downloads\\Pygames\\Space-Invaders\\bullet.png")
bul=pygame.transform.scale(bul, (10,10))

main = pygame.image.load("C:\\Users\\Amey\\Downloads\\Pygames\\Space-Invaders\\ship.png")
main=pygame.transform.scale(main,(50,50))
x=250
ship=Player_ship(x,500,main,50,50)
fire = False
b_l=[]
bx=0
by=0
r_l = []
z = pygame.draw.rect(screen, (0,0,0),(-100,-100,1,1))
b_rect = []
while True:
    clock.tick(60)
    screen.fill((0,0,0))
    ship.draw()
    for i in b_l:
        i.shoot()
    if move_l == True:
        ship.x -= 5
    if move_r == True:
        ship.x += 5

    if fire == True:
        bx=ship.x+20
        by=ship.y
        Bullet_object = Bullet(bx,by,bul,10,10,fire)
        b_l.append(Bullet_object)
        z=pygame.draw.rect(screen,(0,250,0),(b_l[len(b_l)-1].x,b_l[len(b_l)-1].y,5,10))
        b_rect.append(z)
        r_l.append((b_l[len(b_l)-1].x,b_l[len(b_l)-1].y))
        fire = False

    for i in l:
        for j in i:
            a_rect = pygame.draw.rect(screen,(250,0,0),(j.x,j.y,20,20))
            j.draw()
            j.alien_move()

            for k in b_rect:
                if k.colliderect(a_rect):
                    print(1)

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()

        if event.type  == pygame.KEYDOWN:
            if event.key == K_a:
                move_l = True
            elif event.key == K_d:
                move_r = True
            if event.key == K_SPACE:
                fire = True

        if event.type == pygame.KEYUP:
            if event.key == K_a:
                move_l=False
            elif event.key == K_d:
                move_r=False
            if event.key == K_SPACE:
                fire = False
        


    pygame.display.update()