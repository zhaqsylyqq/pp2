#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load(r"AnimatedStreet.png")
pygame.mixer.music.load(r"background.wav")
pygame.mixer.music.play(-1) 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed() 
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
class Monetka(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"png-clipart-pixel-art-mario-coin-text-rectangle (1) (1).png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    def move(self):
        global COIN
        self.rect.move_ip(0, 10)
        if pygame.sprite.spritecollideany(P1, COINS):
            COIN += 1
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        if (self.rect.top > 600):
            
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
class bonus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"photo_2024-04-07_22-59-18.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, 370), 0)
    def move(self):
        self.rect.move_ip(0, 10)
           

    
                   
#Setting up Sprites
C1 = Monetka()        
P1 = Player()
E1 = Enemy()
B1 = bonus()
#Creating Sprites Groups
bonuses = pygame.sprite.Group()
bonuses.add(B1)
COINS = pygame.sprite.Group()
COINS.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

object_list = []
time_interval = 3000 # 200 milliseconds == 0.2 seconds
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, time_interval)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
            
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == timer_event:
            object_list.append(bonus())
        elif event.type == INC_SPEED:
              SPEED += 0.5
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coins = font_small.render(str(COIN), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coins, (50,10))
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    for object in object_list[:]:
        object.move()
        DISPLAYSURF.blit(object.image, object.rect)
        if pygame.sprite.spritecollideany(P1, bonuses):
            COIN += 5
            object_list.remove(object)
        if (object.rect.top > 600):
            object_list.remove(object) 

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound(r"crash.wav").play()
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
           
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)