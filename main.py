import pygame,sys,random,time
from pygame.locals import *
pygame.init()
blk=pygame.image.load('block.bmp')    #load blocks image
img=pygame.image.load('back.bmp')     #load background image
thung=pygame.image.load('thung.bmp')  #load player image
gameover=pygame.image.load('go.bmp')
mas=pygame.image.load('masthead.bmp')
soundObj = pygame.mixer.Sound('wall.wav')
back=pygame.mixer.music.load('background.mid')
global windowSurface


windowSurface = pygame.display.set_mode((600, 462), 0, 32)
pygame.display.set_caption('Simple breakout game by piyush')

class pool():
    x=1
    y=1
    dirx=''
    diry=''
    trig=0
    block=[]
    pigger=0
    
    
    def trigger(self):
        self.trig=1
        
    def _init_(self):
        self.x=250
        self.y=250
        dirx='left'
        diry=''
        block=[]
    def movex(self):
        if self.trig==1:
            if self.dirx=='left':
                self.x-=1
            if self.dirx=='right':
                self.x+=1
            if self.x<=0:
                self.dirx='right'
                soundObj.play()
            if self.x==600:
                self.dirx='left'
                soundObj.play()
    def movey(self):
        if self.trig==1:
            if self.diry=='up':
                self.y-=1
            if self.diry=='down':
                self.y+=1
            if self.y==0:
                soundObj.play()
                self.diry='down'
            if self.y>=410:
                self.diry='up'
                self.x=250
                self.y=250
                
               
                                
                
                
    def drawball(self,surface):
        pygame.draw.circle(surface,(200,100,230),(self.x,self.y),13,0)

    def rev(self):
        if self.diry=='down':
            self.diry='up'
    def drawblock(self,surface):
        
        for blocks in self.block:
                              surface.blit(blk,blocks)

        
        
        
        
        














def play():
    pygame.mixer.music.play(-1, 0.0)    
    
    ball1=pool() 
    pygame.init()
    for i in range(10):
            size=i*75
            ball1.block.append(pygame.Rect(size,20,40,40))
    for i in range(10):
            size=i*75
            ball1.block.append(pygame.Rect(size,60,40,40))
    for i in range(10):
            size=i*75
            ball1.block.append(pygame.Rect(size,100,40,40))
            




   
    
    
   
  
    ball1.x=400
    ball1.y=200
    ball1.dirx='left'
    ball1.diry='up'
    ball1.pigger=1

    a=300
    b=349
    
    
 
    
    
   


    
   
    





    
   
    while True:
        windowSurface.fill((25,25,25))
        
   
        pos = pygame.mouse.get_pos()

        a=pos[0]
        for event in pygame.event.get():
             if event.type==QUIT:
                pygame.quit()
                sys.exit()
                
                
             if event.type==KEYUP:
                 if event.key==K_LEFT:
                     a-=30
                 if event.key==K_RIGHT:
                     a+=30
                 if event.key==ord('a'):
                     pigger=0
            
        
        thunge=pygame.Rect(a, b, 120, 10)
        ball=pygame.Rect(ball1.x, ball1.y, 10, 10)  
        windowSurface.blit(img,(0,0))
        windowSurface.blit(thung,thunge)
        ball1.drawball(windowSurface)
        ball1.movex()
        ball1.movey()
        ball1.trig=1
        ball1.drawblock(windowSurface)
        windowSurface.blit(mas,(-1,410))
        if thunge.colliderect(ball):
            print("collision detecte")
            ball1.rev()
            soundObj.play()
            
        for blok in ball1.block:
            if ball.colliderect(blok):
                ball1.block.remove(blok)
        
        

      
        pygame.display.update()
        
    
    
   

play()
