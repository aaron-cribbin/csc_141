#Code technically written by me
#Is an example
#I will probably not use this

import pygame

pygame.init()
#screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1900, 1050))
my_image = pygame.image.load("assignments/code_jam/images/basketball_small.png")
image_rect = my_image.get_rect(center=(320, 240))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((75, 200, 100))
    if image_rect.x > screen.get_width():
        image_rect.x = -image_rect.width
    screen.blit(my_image, image_rect)
    
    pygame.display.flip()
    clock.tick(15)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            image_rect.x += 1
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            image_rect.x -= 1
        elif event.key == pygame.K_UP:
            image_rect.y -= 1
        elif event.key == pygame.K_DOWN:
            image_rect.y += 1
'''
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            move_right = True
        elif event.key == pygame.K_LEFT:
            move_left = True
        elif event.key == pygame.K_UP:
            move_up = True
        elif event.key == pygame.K_DOWN:
            move_down = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            move_right = False
        elif event.key == pygame.K_LEFT:
            move_left = False
        elif event.key == pygame.K_UP:
            move_up = False
        elif event.key == pygame.K_DOWN:
            move_down = False
'''