import pygame, random, math
from pygame.locals import *

pygame.init()

run = True
screen = pygame.display.set_mode((640, 360))
pygame.display.set_caption('ФОРСАЖ 14124')
FPS = pygame.time.Clock()

class Player:
    def __init__(self) -> None:
        pass


class Enemy:
    def __init__(self) -> None:
        pass


while run:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    FPS.tick(60)