import pygame
import os


pygame.init()
screen = pygame.display.set_mode((1820, 980))
run = True

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

x, y = 30, 30

color = BLUE

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         if color == RED: color = BLUE
        #         else: color = RED

    # pressed = pygame.key.get_pressed()
    # if pressed[pygame.K_UP]: y -= 3
    # if pressed[pygame.K_DOWN]: y += 3
    # if pressed[pygame.K_LEFT]: x -= 3
    # if pressed[pygame.K_RIGHT]: x += 3

    screen.fill(WHITE)
    
    screen.blit(get_image('ball.png'), (20, 20))
    
    # pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    
    clock.tick(60)

    pygame.display.flip()

pygame.quit()