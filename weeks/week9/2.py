import pygame

Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

pygame.init()

size_of_screen = (1820, 980)
screen = pygame.display.set_mode(size_of_screen)
pygame.display.set_caption('ЖЫНДЫ МА')
screen.fill(Green)
run = True

clock = pygame.time.Clock

FPS = 60

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for step in range(10, 100, 10):
        pygame.draw.line(screen, Blue, (10, step), (390, 10), 4)
    # pygame.draw.line(screen, Red, (200, 400), (3000, 7), 150)
    pygame.draw.circle(screen, Black, (900, 500), 60)

    # clock.tick(FPS)

    # Applying changes on the window
    pygame.display.flip()