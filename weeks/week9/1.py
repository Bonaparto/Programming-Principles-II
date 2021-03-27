from turtle import heading
import pygame

pygame.init()
win = pygame.display.set_mode((900, 600))

pygame.display.set_caption('Fingering Game')

x = 415
y = 250
width = 70
height = 100
speed = 0.35

isJump = False
jumpCount = 10
run = True

while run:
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0,0,0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x >= 0:
        x -= speed 
    if keys[pygame.K_RIGHT] and x <= 900 - width:
        x += speed
    if not isJump:
        if keys[pygame.K_UP] and y >= 0:
            y -= speed
        if keys[pygame.K_DOWN] and y <= 600 - height:
            y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10: 
            if jumpCount > 0:
                y -= (jumpCount ** 2) / 2    
            else:   
                y += (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    pygame.display.update()

pygame.quit()