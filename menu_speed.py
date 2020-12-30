import pygame
import menu_mathini
import menu_mathop

from pygame.locals import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500

BLACK = (0, 0, 0)


def menu():
    text_color = BLACK

    op_width = 50
    op_height = 50

    v_width = 100
    v_height = 40
    v_width2 = 105
    v_height2 = 45

    vel1x = 110
    vel2x = 425
    vel3x = 720
    opy = 200
    vx = 800
    vy = 455

    op_width2 = 55
    op_height2 = 55

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    background = pygame.image.load("sprites/menu/background.png")
    background = pygame.transform.smoothscale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    level1_1 = pygame.image.load("sprites/menu/1.png")
    level1_1 = pygame.transform.smoothscale(level1_1, (op_width, op_height))
    level1_2 = pygame.image.load("sprites/menu/1.png")
    level1_2 = pygame.transform.smoothscale(level1_2, (op_width2, op_height2))
    level1 = level1_1

    level2_1 = pygame.image.load("sprites/menu/2.png")
    level2_1 = pygame.transform.smoothscale(level2_1, (op_width, op_height))
    level2_2 = pygame.image.load("sprites/menu/2.png")
    level2_2 = pygame.transform.smoothscale(level2_2, (op_width2, op_height2))
    level2 = level2_1

    level3_1 = pygame.image.load("sprites/menu/3.png")
    level3_1 = pygame.transform.smoothscale(level3_1, (op_width, op_height))
    level3_2 = pygame.image.load("sprites/menu/3.png")
    level3_2 = pygame.transform.smoothscale(level3_2, (op_width + 5, op_height + 5))
    level3 = level3_1
    
    return1 = pygame.image.load("sprites/menu/return.png")
    return1 = pygame.transform.smoothscale(return1, (v_width, v_height))
    return2 = pygame.image.load("sprites/menu/return.png")
    return2 = pygame.transform.smoothscale(return2, (v_width2, v_height2))
    return0 = return1

    pygame.font.init()
    font = pygame.font.SysFont("Comic Sans MS", 30, True, False)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if (vel1x <= pygame.mouse.get_pos()[0] <= (vel1x + op_width)) \
                    and (opy <= pygame.mouse.get_pos()[1] <= (opy + op_height)):
                level1 = level1_2
                if pygame.mouse.get_pressed()[0]:
                    speed = 'easy'
                    menu_mathop.menu(speed)
            else:
                level1 = level1_1

            if (vel2x <= pygame.mouse.get_pos()[0] <= (vel2x + op_width)) \
                    and (opy <= pygame.mouse.get_pos()[1] <= (opy + op_height)):
                level2 = level2_2
                if pygame.mouse.get_pressed()[0]:
                    speed = 'middle'
                    menu_mathop.menu(speed)
            else:
                level2 = level2_1

            if (vel3x <= pygame.mouse.get_pos()[0] <= (vel3x + op_width)) \
                    and (opy <= pygame.mouse.get_pos()[1] <= (opy + op_height)):
                level3 = level3_2
                if pygame.mouse.get_pressed()[0]:
                    speed = 'hard'
                    menu_mathop.menu(speed)
            else:
                level3 = level3_1

            if (vx <= pygame.mouse.get_pos()[0] <= (vx + v_width)) \
                    and (vy <= pygame.mouse.get_pos()[1] <= (vy + v_height)):
                return0 = return2
                if pygame.mouse.get_pressed()[0]:
                    menu_mathini.menu()
            else:
                return0 = return1
            pygame.display.update()

        text = font.render("Escolha o nível de dificuldade", True, text_color)

        screen.blit(background, (0, 0))
        screen.blit(level1, (vel1x, opy))
        screen.blit(level2, (vel2x, opy))
        screen.blit(level3, (vel3x, opy))
        screen.blit(return0, (vx, vy))
        screen.blit(text, (230, 70))

        pygame.display.update()
