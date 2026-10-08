#Code technically written by me
#Is an example
#I will probably not use this

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))
my_image = pygame.image.load("code_jam/images/basketball.png").convert_alpha()
image_rect = my_image.get_rect(center=(320, 240))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    image_rect.x += 1

    if image_rect.x > screen.get_width():
        image_rect.x = -image_rect.width
    screen.blit(my_image, image_rect)
    pygame.display.flip()
    clock.tick(15)