import pygame
from math import sin, cos, pi

Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Blue = (0, 0, 255)
nums = ['-1.00', '-0.75', '-0.50', '-0.25', '     0', ' 0.25', ' 0.50', ' 0.75', ' 1.00', '2']
radians = ['3π', '5π', '2π', '3π', ' π', 'π', ' 0']
l, l1, s, c = '__', '_', 'sin x', 'cos x'

pygame.init()

size_of_screen = (1820, 980)
screen = pygame.display.set_mode(size_of_screen)
pygame.display.set_caption('Sin & Cos <3')
screen.fill(Black)
font = pygame.font.SysFont('arial', 30)
font1 = pygame.font.SysFont('arial', 36)
run, Draw = True, True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # upper and lower borders
    pygame.draw.line(screen, White, (100, 100), (1720, 100), 8)
    pygame.draw.line(screen, White, (100, 880), (1720, 880), 8)

    # left and right borders
    pygame.draw.line(screen, White, (100, 100), (100, 880), 8) 
    pygame.draw.line(screen, White, (1720, 100), (1720, 880), 8)

    # the plane
    pygame.draw.line(screen, White, (100, 490), (1720, 490), 6)    # x - axis
    pygame.draw.line(screen, White, (910, 100), (910, 880), 6)    # y - axis

    # marks for the plane
    for y in range(186, 870, 76):
        pygame.draw.line(screen, White, (100, y), (1720, y), 2)
        if 250 < y < 850:
            # small marks
            pygame.draw.line(screen, White, (100, y - 19), (110, y - 19))
            pygame.draw.line(screen, White, (100, y - 57), (110, y - 57)) 
            pygame.draw.line(screen, White, (1720, y - 19), (1710, y - 19)) 
            pygame.draw.line(screen, White, (1720, y - 57), (1710, y - 57)) 

            # big marks
            pygame.draw.line(screen, White, (100, y - 38), (120, y - 38)) 
            pygame.draw.line(screen, White, (1720, y - 38), (1700, y - 38)) 

    for x in range(160, 1720, 250):
        pygame.draw.line(screen, White, (x, 100), (x, 880), 2)
        if 250 < x < 1700:
            # marks for lower line
            pygame.draw.line(screen, White, (x - 220, 880), (x - 220, 870))
            pygame.draw.line(screen, White, (x - 160, 880), (x - 160, 870))
            pygame.draw.line(screen, White, (x - 190, 880), (x - 190, 860)) 
            pygame.draw.line(screen, White, (x - 100, 880), (x - 100, 870))
            pygame.draw.line(screen, White, (x - 40, 880), (x - 40, 870))
            pygame.draw.line(screen, White, (x - 70, 880), (x - 70, 860)) 
            pygame.draw.line(screen, White, (x - 130, 880), (x - 130, 850))

            # marks for upper line
            pygame.draw.line(screen, White, (x - 220, 100), (x - 220, 110))
            pygame.draw.line(screen, White, (x - 160, 100), (x - 160, 110))
            pygame.draw.line(screen, White, (x - 190, 100), (x - 190, 120)) 
            pygame.draw.line(screen, White, (x - 100, 100), (x - 100, 110))
            pygame.draw.line(screen, White, (x - 40, 100), (x - 40, 110))
            pygame.draw.line(screen, White, (x - 70, 100), (x - 70, 120)) 
            pygame.draw.line(screen, White, (x - 130, 100), (x - 130, 130))

    # numbered marks
    cnt = len(nums) - 2
    for i in range(170, 850, 76):                       # y - axis
        text = font.render(nums[cnt], True, White)
        screen.blit(text, (35, i))
        cnt -= 1
    
    cnt = 0
    for i in range(145, 920, 126):
        text = font.render(l1, True, White)
        if cnt % 2 != 0:
            y = 890
            screen.blit(text, (i - 24, 892))
        else:
            y = 900
            if not i + 126 > 920: 
                screen.blit(text, (i - 20, 890))
        text = font.render(radians[cnt], True, White)
        screen.blit(text, (i, y))
        cnt += 1

    cnt -= 1
    for i in range(1024, 1720, 124):
        cnt -= 1        
        if cnt % 2 != 0:
            y = 890
        else:
            y = 890
        text = font.render(radians[cnt], True, White)
        screen.blit(text, (i, y))

    for i in range(284, 1720, 250):
        text = font.render(l, True, White)
        screen.blit(text, (i - 12, 892))
        text = font.render('2', True, White)
        screen.blit(text, (i - 4, 918))

    text = font1.render(s, True, White)
    screen.blit(text, (1170, 200))
    pygame.draw.line(screen, Red, (1250, 213), (1320, 213), 5)
    
    text = font1.render(c, True, White)
    screen.blit(text, (1168, 225))
    for i in range(1250, 1320, 20):
        pygame.draw.line(screen, Blue, (i, 238), (i + 10, 238), 5)

    # drawing graph
    X = 0
    while Draw:
        for i in range(-540, 541):
            pygame.draw.line(screen, Red, (160 + X, 490 - int(sin((i / 180) * pi) * 302)), (161 + X, 490 - int(sin(((i + 1) / 180) * pi) * 302)), 4)
            if i % 5 == 0:
                pygame.draw.line(screen, Blue, (160 + X, 490 - int(cos((i / 180) * pi) * 302)), (161 + X, 490 - int(cos(((i + 1) / 180) * pi) * 302)), 4)
            X += (1500 / 1080)
            pygame.display.update()
            pygame.time.delay(3)
        Draw = False

    pygame.display.flip()

pygame.quit()