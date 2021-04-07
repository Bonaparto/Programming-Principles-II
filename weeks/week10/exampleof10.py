import os, pygame, random

image_library = {}

screen_size = (1820, 980)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Igra goy')
clock = pygame.time.Clock()
x, y, speed = 30, 30, 15
run = True

def get_image(path):    
    global image_library
    path = os.path.join(os.getcwd(), 'images', path)
    image = image_library.get(path)
    if image == None:
        image = pygame.image.load(path)
        image_library[path] = image
    return image

class Im:

    def __init__(self, *args, **kwargs):
        self.dx = random.randint(5, 10)
        self.dy = 167
        self.x = 0
        self.y = 0

    def move(self):
        self.x += self.dx
        # self.y += self.dy
        if self.x > screen_size[0] - 224 or self.x < 0:
            self.dx *= -1
            self.y += self.dy
        if self.y > screen_size[1] - 167 or self.y < 0:
            self.dy *= -1

    def draw(self, screen):
        screen.blit(get_image('siski.jpg'), (self.x, self.y))

images = [
    Im()
]

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                images.append(Im())
    
    for im in images:
        im.move()

    screen.fill((0,0,0))

    for im in images:
        im.draw(screen)

    # if pressed[pygame.K_DOWN]:
    #     y += speed
    # if pressed[pygame.K_UP]:
    #     y -= speed
    # if pressed[pygame.K_RIGHT]:
    #     x += speed
    # if pressed[pygame.K_LEFT]:
    #     x -= speed


    clock.tick(60)
    pygame.display.flip()
    pygame.display.update()