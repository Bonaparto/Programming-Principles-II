import pygame, random, os, time, sys
from pygame import font
from pygame.locals import *

pygame.init()

Width, Height = 640, 640
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('ФОРСАЖ 14124')
FPS = pygame.time.Clock()
White = (255, 255, 255)
Red = (0, 255, 255)
Yellow = (255, 0, 255)
p_library_of_images = {}
e_library_of_images = {}
pe_library_of_images = {}
speed = 1
coinFont = pygame.font.SysFont('chiller', 40)
endFont = pygame.font.SysFont('century', 100)
game_over = endFont.render('Game Over', True, Red)

def get_image(name, p):
    if p == 0:
        global e_library_of_images
        path = os.path.join(os.getcwd(), 'images', 'Enemy', name)
        image = e_library_of_images.get(path)
        if image == None:
            image = pygame.image.load(path)
            e_library_of_images[path] = image
        return image
    elif p == 12:
        global pe_library_of_images
        path = os.path.join(os.getcwd(), 'images', 'Pets', name)
        image = pe_library_of_images.get(path)
        if image == None:
            image = pygame.image.load(path)
            pe_library_of_images[path] = image
        return image
    else: 
        global p_library_of_images
        path = os.path.join(os.getcwd(), 'images', 'Player', p, name)
        image = p_library_of_images.get(path)
        if image == None:
            image = pygame.image.load(path)
            p_library_of_images[path] = image
        return image

class Player(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()
        self.P = str(random.randint(1, 3))
        self.image = get_image('2 (1).png', self.P)
        self.speed = 6
        self.surf = pygame.Surface((68, 84))
        self.rect = self.surf.get_rect(center = (320, 598))
        self.c = 1
        self.cnt = 1

    def move(self):
        self.c += 1
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -self.speed)
        if self.rect.bottom < Height:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, self.speed)
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-self.speed, 0)
        if self.rect.right < Width:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(self.speed, 0)
        if not(self.c % 3) and (pressed_keys[K_RIGHT] or pressed_keys[K_LEFT] or pressed_keys[K_DOWN] or pressed_keys[K_UP]):
            self.cnt += 1
            if self.cnt > 11:
                self.cnt = 1
            self.image = get_image(f'2 ({self.cnt}).png', self.P)

    def draw(self):
        screen.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.E = random.randint(1, 9)
        self.image = get_image(f'E ({self.E}).png', 0)
        self.speed = random.randint(5 + speed // 8, 11 + speed // 8)
        self.surf = pygame.Surface((65, 108))
        self.rect = self.surf.get_rect(center = (random.randint(90, 550), random.randint(90, 100)))
        self.cnt = 1

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > Height:
            self.rect.top = 0
            self.rect.center = (random.randint(65, 575), random.randint(50, 60))
            self.speed = random.randint(5 + self.cnt // 4, 11 + self.cnt // 4)
            self.E = random.randint(1, 9)
            self.image = get_image(f'E ({self.E}).png', 0)
            self.cnt += 1
    
    def draw(self):
        screen.blit(self.image, self.rect)

class Pet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pe = random.randint(16, 30)
        self.image = get_image(str(self.pe) + '.png', 12) 
        self.surf = pygame.Surface((40, 40))
        self.rect = self.surf.get_rect(center = (random.randint(40, 600), 40))

    def move(self):
        self.rect.move_ip(0, 7)
        if self.rect.top > Height:
            self.pe = random.randint(16, 30)
            self.rect = self.surf.get_rect(center = (random.randint(40, 600), 40))
            self.rect.top = 0
            self.image = get_image(str(self.pe) + '.png', 12)
            global speed
            speed += 1
        
    def draw(self):
        screen.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()
Pe1 = Pet()

enemies = pygame.sprite.Group()
enemies.add(E1)
pets = pygame.sprite.Group()
pets.add(Pe1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(Pe1)

while True:
    background = pygame.image.load(os.path.join(os.getcwd(), 'images', 'Backgrounds', str(random.randint(1, 4)) + '.png'))
    cnt = 0
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        score = coinFont.render(str(cnt), True, Yellow)
        screen.blit(background, (0, 0))
        screen.blit(score, (600, 0))

        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
            entity.move()

        if pygame.sprite.spritecollideany(P1, enemies):
            # screen.fill(White)
            for entity in all_sprites:
                entity.kill()
                screen.fill(White)
                end = True
                while end:
                    screen.blit(game_over, (70, 240))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
        
        if pygame.sprite.spritecollideany(P1, pets):
            cnt += 1
            Pe1.rect.top = Height

        FPS.tick(60)