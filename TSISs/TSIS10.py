import pygame, random, math, sys, os
from pygame.locals import *

pygame.init()

run = True
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption('ФОРСАЖ 14124')
FPS = pygame.time.Clock()
White = (255, 255, 255)

class Player(pygame.sprite.Sprite):

    def __init__(self): 
        self.image = pygame.image.load(os.path.join(os.getcwd(), 'images', "Player.jpg"))
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect()

    def update(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < 590:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

    def draw(self):
        screen.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pass

P1 = Player()
E1 = Enemy()

while run:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    P1.update()

    screen.fill(White)

    P1.draw()

    FPS.tick(60)