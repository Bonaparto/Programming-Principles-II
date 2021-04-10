import pygame

pygame.init()

White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)

Win_Height = 600
Win_Width = 600

screen = pygame.display.set_mode((Win_Width, Win_Height))
clock = pygame.time.Clock()

block = 20
body = [[150, 150], [0, 0]]

dx, dy = block, 0
radius = 10

game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx = block
                dy = 0  
            if event.key == pygame.K_LEFT:
                dx = -block
                dy = 0
            if event.key == pygame.K_UP:
                dx = 0
                dy = -block
            if event.key == pygame.K_DOWN:
                dx = 0
                dy = block
            if event.key == pygame.K_SPACE:
                body.append([[body[len(body) - 1][0], body[len(body) - 1][1]]])

    for i in range(len(body) - 2, 0, -1):
        body[i][0] = body[i - 1][0]
        body[i][1] = body[i - 1][1]

    body[0][0] += dx
    body[0][1] += dy

    screen.fill(White)

    for i, (x, y) in enumerate(body):    
        color = Red if i == 0 else Green
        pygame.draw.circle(screen, Green, (x, y), radius)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()