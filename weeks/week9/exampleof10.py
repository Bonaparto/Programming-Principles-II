import os, pygame

image_library = {}

def get_image(path):    
    global image_library
    path = os.path.join(os.getcwd(), path)
    image = image_library.get(path)
    if image == None:
        image = pygame.image.load(path)
        image_library[path] = image
    return image

screen_size = (640, 360)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Igra goy')
clock = pygame.time.Clock()
x, y = 30, 30
run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    

    screen.blit(get_image('photo.jpg'), (x, y))

    clock.tick(60)
    pygame.display.flip()
    pygame.display.update()