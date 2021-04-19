import pygame, os, sys

pygame.init()

Win_Width = 1100
Win_Height = 1000
screen = pygame.display.set_mode((Win_Width, Win_Height))
pygame.display.set_caption('Paint 2.0')

White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Yellow_Green = (96, 255, 128)
Pink = (255, 192, 203)
Orange = (255, 165, 0)
Green = (0, 192, 0)
Blue = (0, 32, 255)
Purple = (160, 32, 255)
Yellow = (255, 224, 32)
Gray = (128, 128, 128)
Brown = (160, 128, 96)
Pale_Pink = (255, 208, 160)

font = pygame.font.SysFont('verdana', 45)
eraser = font.render('Eraser', True, Black)
size_text = font.render('Size', True, Black)
screen.fill(White)

colors = [Black, Pale_Pink, Brown, Orange, Yellow, Green, Blue, Purple, Pink, Red, Yellow_Green, Gray]
choosen_color = Black
choosen_color_circle = Black
choosen_color_rect = Black
size = 100
choosen_figure = True

run = True

def save_image():
    subsurface = screen.subsurface((0, 0, Win_Width - 300, Win_Height))
    pygame.image.save(subsurface, 'image.png')

def options_check(event, coos):
    global choosen_color
    global choosen_color_circle
    global choosen_color_rect
    x, y = coos[0], coos[1]
    X, Y = 880, 200
    for i in range(12):
        Y += 100 
        if X <= x <= X + 50 and Y <= y <= Y + 50:
            choosen_color = colors[i]
            if choosen_figure:
                choosen_color_rect = colors[i]
            else:
                choosen_color_circle = colors[i]
        if i == 5:
            X += 120
            Y = 200
    if 880 <= x <= 1050 and 900 <= y <= 960:
        choosen_color = White
        choosen_color_circle = Black
        choosen_color_rect = Black

def size_check(event, coos):
    global size
    size = 100 - (1060 - coos[0]) // 2

def figure_check(event, coos):
    global choosen_figure
    global choosen_color_circle
    global choosen_color_rect
    if 850 <= coos[0] <= 950 and 30 <= coos[1] <= 130:
        choosen_figure = True
        choosen_color_circle = Black
        choosen_color_rect = choosen_color
    elif 980 <= coos[0] <= 1080 and 30 <= coos[1] <= 130:
        choosen_figure = False
        choosen_color_circle = choosen_color
        choosen_color_rect = Black


while run:  
    pressed = pygame.mouse.get_pressed()
    left_button = pressed[0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_image()
                    run = False
        coos = pygame.mouse.get_pos()
        if left_button and coos[0] < 800:
            if choosen_figure:
                pygame.draw.rect(screen, choosen_color, (coos[0] - size // 2, coos[1] - size // 2, size, size))
            if not choosen_figure:
                pygame.draw.circle(screen, choosen_color, (coos[0], coos[1]), size // 2)
        if left_button:
            if coos[0] > 800 and coos[1] > 300:
                options_check(event, coos)
            elif 1060 >= coos[0] >= 860 and 240 >= coos[1] >= 200:
                size_check(event, coos)
            elif 850 <= coos[0] <= 1080 and 130 >= coos[1] >= 30:
                figure_check(event, coos)

    pygame.draw.rect(screen, White, (800, 0, 400, 1000))
    screen.blit(size_text, (920, 220))
    screen.blit(eraser, (895, 900))
    pygame.draw.rect(screen, choosen_color if not choosen_color == White else Black, (880, 900, 170, 60), 4)
    pygame.draw.line(screen, Black, (800, 0), (800, 1000), 30)
    pygame.draw.rect(screen, choosen_color_rect, (850, 30, size, size))
    pygame.draw.circle(screen, choosen_color_circle, (1030, 80), size // 2)
    pygame.draw.aalines(screen, Black, True, ((860, 200), (1060, 180), (1060, 220)))
    pygame.draw.lines(screen, choosen_color if not choosen_color == White else Black, True, ((860, 200), (860 + size * 2 , 200 + int(0.2 * size)), (860 + size * 2 , 200 - int(0.2 * size))), 5)

    X, Y = 880, 200
    for i in range(12):
        Y += 100 
        pygame.draw.rect(screen, colors[i], (X, Y, 50, 50))
        if i == 5:
            X += 120
            Y = 200

    pygame.display.flip()