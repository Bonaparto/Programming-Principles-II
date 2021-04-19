import pygame, sys, os, json, random

pygame.init()

White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Yellow = (255, 0, 255)
Black = (0, 0, 0)

Win_Height = 600
Win_Width = 600

screen = pygame.display.set_mode((Win_Width, Win_Height))
pygame.display.set_caption('КВАДРАТНЫЙ СНЭЙК')
fps = pygame.time.Clock()

menu_font = pygame.font.SysFont('arial', 100)
menu_font1 = pygame.font.SysFont('arial', 50)
levels_font = pygame.font.SysFont('garamondполужирный', 50)
instructions_font = pygame.font.SysFont('verdana', 20)
ret = instructions_font.render('Return to the menu', True, White)

highscores_url = os.path.join(os.getcwd(), 'Snake', 'scores.py')
saved_url = os.path.join(os.getcwd(), 'Snake', 'saved.py')

food_images = [pygame.image.load(os.path.join(os.getcwd(), 'Snake', 'food', str(i)+'.png')) for i in range(1, 5)]
level = 1
score = 0
speed = 24

with open(highscores_url) as f:
    highscores_list = json.load(f)

with open(saved_url) as f:
    saved_data = json.load(f)

def game_end():
    text = menu_font.render('You Lost', True, White)
    text1 = menu_font1.render(f'Your score: {score}', True, White)
    run = True
    highscores_list['scores'].append(score)
    with open(highscores_url, 'w', encoding='utf-8') as f:
        json.dump(highscores_list, f)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    coos = pygame.mouse.get_pos()
                    x, y = coos[0], coos[1]
                    
        screen.fill(Black)
        screen.blit(text, (150, 50))
        screen.blit(text1, (180, 250))

        pygame.display.flip()


def level_choose():
    levels = [levels_font.render(i, True, White) for i in ['EASY', 'MEDIUM', 'HARD']]
    global level
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    coos = pygame.mouse.get_pos()
                    x, y = coos[0], coos[1]
                    if 150 <= y <= 220 and 165 <= x <= 425:
                        level = 2
                    if 245 <= y <= 315 and 165 <= x <= 425:
                        level = 3
                    if 340 <= y <= 410 and 165 <= x <= 425:
                        level = 4
                    if level != 1:
                        run = False

        screen.fill(Black)
        for i in range(150, 341, 95):
            pygame.draw.rect(screen, White, (165, i, 260, 70), 3)
            
        screen.blit(levels[0], (230, 155))
        screen.blit(levels[1], (182, 250))
        screen.blit(levels[2], (225, 345))
        pygame.display.flip()

def instructions():
    text = [instructions_font.render(i, True, White) for i in['Green player moves with arrows;', 'Red player moves with W, A, S, D;', 'If you crush into the wall, you lose;', 'If you crush into yourself, you lose;', 'If you crush into other player, you lose;', 'Collect food which is spawning on the map','and raise your snake;']]
    run, Y, X = True, 50, 75
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    coos = pygame.mouse.get_pos()
                    x, y = coos[0], coos[1]
                    if 200 <= x <= 430 and 490 <= y <= 540:
                        run = False

        screen.fill(Black)
        screen.blit(ret, (205, 500))
        pygame.draw.rect(screen, White, (190, 490, 230, 50), 3)
        for i in range(len(text)):
            screen.blit(text[i], (X, Y))
            Y += 70
            if i == len(text) - 3:
                Y -= 40
        Y, X = 50, 75
        pygame.display.flip()

def highscores():
    text = menu_font.render('Best Scores', True, White)
    order = [menu_font1.render(i, True, White) for i in ['1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.']]
    scs = [menu_font1.render(str(i), True, White) for i in sorted(highscores_list['scores'])[::-1]]
    run, Y, X = True, 130, 150
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    coos = pygame.mouse.get_pos()
                    x, y = coos[0], coos[1]
                    if 200 <= x <= 430 and 490 <= y <= 540:
                        run = False
        
        screen.fill(Black)
        screen.blit(text, (100, 10))
        screen.blit(ret, (200, 500))
        pygame.draw.rect(screen, White, (190, 490, 230, 50), 3)

        for i in range(len(highscores_list['scores']) % 10):
            if i > 4:
                X = 350
                Y = 130
            screen.blit(order[i], (X, Y))
            screen.blit(scs[i], (X + 45, Y))
            Y += 70

        X = 150
        Y = 130
        pygame.display.flip()

def game_menu():
    t, run = menu_font.render('SNAKE', True, White), True
    t1 = [menu_font1.render(i, True, White) for i in ['Start', 'Instruction', 'Best Scores', 'Saved Games']]
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    coos = pygame.mouse.get_pos()
                    x, y = coos[0], coos[1]
                    if 145 <= x <= 445 and 175 <= y <= 245:
                        level_choose()
                        run = False
                    if 265 <= y <= 335 and 145 <= x <= 445:
                        instructions()
                    if 355 <= y <= 425 and 145 <= x <= 445:
                        highscores()
                    if 445 <= y <= 515 and 145 <= x <= 445:
                        saved_game()
                        run = False

        screen.fill(Black)
        for i in range(175, 446, 90):
            pygame.draw.rect(screen, White, (145, i, 300, 70), 3)
        screen.blit(t1[0], (250, 185))
        screen.blit(t1[1], (200, 275))
        screen.blit(t1[2], (185, 365))
        screen.blit(t1[3], (165, 455))
        screen.blit(t, (160, 20))
        pygame.display.flip()

def saved_game():
    global level
    global score
    with open(saved_url, 'r', encoding='utf-8') as f:
        saved_data = json.load(f)
    level = saved_data['level']
    score = saved_data['score']
    P1.body = saved_data['bodies'][0]
    P2.body = saved_data['bodies'][1]

def save_game():
    text = menu_font1.render('Do you want to save game?', True, White)
    text1 = menu_font1.render('Yes', True, White)
    text2 = menu_font1.render('No', True, White)
    run = True
    while run:
        screen.fill(Black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    coos = pygame.mouse.get_pos()
                    x, y = coos[0], coos[1]
                    if 210 <= x <= 360 and 275 <= y <= 345:
                        saved_data['score'] = score
                        saved_data['bodies'] = [P1.body, P2.body]  
                        saved_data['level'] = level
                        with open(saved_url, 'w', encoding='utf-8') as f:
                            json.dump(saved_data, f)
                        pygame.quit()
                        sys.exit()
                    elif 210 <= x <= 360 and 395 <= y <= 465:
                        pygame.quit()
                        sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        pygame.draw.rect(screen, White, (210, 275, 150, 70), 3)
        pygame.draw.rect(screen, White, (210, 395, 150, 70), 3)
        screen.blit(text, (50, 150))
        screen.blit(text1, (250, 280))
        screen.blit(text2, (255, 400))
        pygame.display.flip()

def check_collision():
    if level == 3:
        if P1.body[0][0] < 8 or P1.body[0][0] > Win_Width - 33 or P1.body[0][1] < 0 or P1.body[0][1] > 488 or P2.body[0][0] < 8 or P2.body[0][0] > Win_Width - 33 or P2.body[0][1] < 0 or P2.body[0][1] > 488:
            game_end()
    if level == 4:
        if P1.body[0][0] < 10 or P1.body[0][0] > Win_Width - 36 or P1.body[0][1] < 10 or P1.body[0][1] > 486 or P2.body[0][0] < 8 or P2.body[0][0] > Win_Width - 33 or P2.body[0][1] < 10 or P2.body[0][1] > 486:
            game_end()
        for i in range(120, 401, 280):
            if P1.body[0][0] < i + 64 and P1.body[0][0] > i - speed and ((P1.body[0][1] > 80 and P1.body[0][1] < 142) or (P1.body[0][1] > 360 and P1.body[0][1] < 416)):
                game_end()
            if P2.body[0][0] < i + 64 and P2.body[0][0] > i - speed and ((P2.body[0][1] > 80 and P2.body[0][1] < 142) or (P2.body[0][1] > 360 and P2.body[0][1] < 416)):
                game_end()
        if ((P1.body[0][0] < 464 and P1.body[0][0] > 420) or (P1.body[0][0] < 152 and P1.body[0][0] > 108)) and ((P1.body[0][1] > 136 and P1.body[0][1] < 168) or (P1.body[0][1] > 340 and P1.body[0][1] < 384)):
            game_end()
        if ((P2.body[0][0] < 464 and P2.body[0][0] > 420) or (P2.body[0][0] < 152 and P2.body[0][0] > 108)) and ((P2.body[0][1] > 136 and P2.body[0][1] < 168) or (P2.body[0][1] > 340 and P2.body[0][1] < 384)):
            game_end()
        if (P1.body[0][0] > 248 and P1.body[0][0] < 308 and P1.body[0][1] > 232 and P1.body[0][1] < 284) or (P2.body[0][0] > 248 and P2.body[0][0] < 308 and P2.body[0][1] > 232 and P2.body[0][1] < 284):
            game_end()
        
class Food():
    def __init__(self):
        self.x = 24
        self.y = 24
        self.surf = pygame.Surface((speed, speed))
        self.image = food_images[random.randint(0, 3)]
        self.rect = self.surf.get_rect(center = (self.x, self.y))

    def show(self):
        screen.blit(self.image, self.rect)

class Player():
    def __init__(self, p):
        self.dx = 0
        self.dy = 0
        self.body = [[160, 200]] if p == 1 else [[400, 200]]
        self.colors = [Green, Red] if p == 1 else [Yellow, Blue]
        self.r = False
        self.l = False
        self.u = False
        self.d = False

    def move(self):
        if level == 2:
            if self.body[0][0] < 0:
                self.body[0][0] = Win_Width
            if self.body[0][0] > Win_Width:
                self.body[0][0] = 0
            if self.body[0][1] < 0:
                self.body[0][1] = 508 - speed
            if self.body[0][1] > 508 - speed:
                self.body[0][1] = -8
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]
        self.body[0][0] += self.dx
        self.body[0][1] += self.dy
        if [self.body[0][0], self.body[0][1]] in self.body[1:]:
            game_end()
            
    def show(self):
        for i in range(len(self.body)):
            pygame.draw.rect(screen, self.colors[i % 2], (self.body[i][0], self.body[i][1], speed, speed))

P1, P2 = Player(1), Player(2)
food = Food()

game_menu()  

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                save_game()
            if event.key == pygame.K_RIGHT and not P1.l:
                P1.dx = speed // 3
                P1.dy = 0  
                P1.r = True
                P1.l = False
                P1.u = False
                P1.d = False
            if event.key == pygame.K_LEFT and not P1.r:
                P1.dx = -speed // 3
                P1.dy = 0
                P1.r = False
                P1.l = True
                P1.u = False
                P1.d = False
            if event.key == pygame.K_UP and not P1.d:
                P1.dx = 0
                P1.dy = -speed // 3
                P1.r = False
                P1.l = False
                P1.u = True
                P1.d = False
            if event.key == pygame.K_DOWN and not P1.u:
                P1.dx = 0
                P1.dy = speed // 3
                P1.r = False
                P1.l = False
                P1.u = False
                P1.d = True
            if event.key == pygame.K_d and not P2.l:
                P2.dx = speed // 3
                P2.dy = 0 
                P2.l = False
                P2.r = True 
                P2.u = False
                P2.d = False
            if event.key == pygame.K_a and not P2.r:
                P2.dx = -speed // 3
                P2.dy = 0
                P2.l = True
                P2.r = False 
                P2.u = False
                P2.d = False
            if event.key == pygame.K_w and not P2.d:
                P2.dx = 0
                P2.dy = -speed // 3
                P2.l = False
                P2.r = False 
                P2.u = True
                P2.d = False
            if event.key == pygame.K_s and not P2.u:
                P2.dx = 0
                P2.dy = speed // 3
                P2.l = False
                P2.r = False 
                P2.u = False
                P2.d = True
    cur_score = menu_font1.render(f'Score: {score}', True, White)

    screen.fill(Black)

    if level == 2:
        pygame.draw.line(screen, White, (0, 520), (600, 520), 16)

    if level == 3:
        pygame.draw.rect(screen, White, (0, 0, 600, 520), 24)

    if level == 4:
        pygame.draw.rect(screen, White, (0, 0, 600, 520), 24)
        for i in range(120, 457, 280):
            pygame.draw.rect(screen, White, (i, 104, 64, 32))
            pygame.draw.rect(screen, White, (i, 384, 64, 32))
        pygame.draw.rect(screen, White, (120, 136, 32, 32))
        pygame.draw.rect(screen, White, (120, 352, 32, 32))
        pygame.draw.rect(screen, White, (432, 136, 32, 32))
        pygame.draw.rect(screen, White, (432, 352, 32, 32))
        pygame.draw.rect(screen, White, (268, 244, 40, 40))

    screen.blit(cur_score, (216, 530))

    if (P1.body[0][0] - speed <= food.x <= P1.body[0][0] + speed * 2 and P1.body[0][1] - speed <= food.y <= P1.body[0][1] + speed * 2) or (P2.body[0][0] - speed <= food.x <= P2.body[0][0] + speed * 2 and P2.body[0][1] - speed <= food.y <= P2.body[0][1] + speed * 2):
        if (P1.body[0][0] - speed <= food.x <= P1.body[0][0] + speed * 2 and P1.body[0][1] - speed <= food.y <= P1.body[0][1] + speed * 2):
            P1.body.append([P1.body[len(P1.body) - 1][0], P1.body[len(P1.body) - 1][1]])
        else:
            P2.body.append([P2.body[len(P2.body) - 1][0], P2.body[len(P2.body) - 1][1]])
        if level == 2:
            coos = (random.randint(12, 588), random.randint(12, 508))
            food.rect.center, food.x, food.y = coos, coos[0], coos[1]
        if level == 3:
            coos = (random.randint(36, 564), random.randint(36, 508))
            food.rect.center, food.x, food.y = coos, coos[0], coos[1]
        if level == 4:
            coos = (random.randint(24, Win_Width - speed * 2), random.randint(24, 472))
            food.rect.center, food.x, food.y = coos, coos[0], coos[1]
        food.image = food_images[random.randint(0, 2)]
        score += 1

    P1.move()
    P2.move()
    P1.show()
    P2.show()
    check_collision()
    if [P1.body[0][0], P1.body[0][0]] in P2.body or [P2.body[0][0], P2.body[0][1]] in P1.body:
        game_end()
    food.show()

    fps.tick(15)
    pygame.display.flip()

pygame.quit()