import pygame
import menu_mathini

from pygame.locals import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500


def info():
    vx = 800
    vy = 455
    vw = 90
    vh = 40
    vw2 = 95
    vh2 = 45

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    info_img = pygame.image.load("sprites/menu/info_1.png")
    info_img = pygame.transform.scale(info_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

    return1 = pygame.image.load("sprites/menu/return.png")
    return1 = pygame.transform.smoothscale(return1, (vw, vh))
    return2 = pygame.image.load("sprites/menu/return.png")
    return2 = pygame.transform.smoothscale(return2, (vw2, vh2))
    return0 = return1
     
    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if (vx <= pygame.mouse.get_pos()[0] <= (vx + vw)) \
                    and (vy <= pygame.mouse.get_pos()[1] <= (vy + vh)):
                return0 = return2
                if pygame.mouse.get_pressed()[0]:
                    menu_mathini.menu()
            else:
                return0 = return1

        screen.blit(info_img, (0, 0))

        screen.blit(return0, (vx, vy))

        pygame.display.update()
