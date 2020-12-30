import pygame
import master_math18
import menu_speed

from pygame.locals import *


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500

BLACK = (0, 0, 0)


def menu(speed):
    text_color = BLACK

    op_width = 75
    op_height = 75

    v_width = 100
    v_height = 40
    v_width2 = 105
    v_height2 = 45

    sumx = 110
    subx = 310
    multx = 510
    divx = 710
    opy = 190
    vx = 800
    vy = 455

    op_width2 = 80
    op_height2 = 80

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    background = pygame.image.load("sprites/menu/background.png")
    background = pygame.transform.smoothscale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    mult1 = pygame.image.load("sprites/menu/mult.png")
    mult1 = pygame.transform.smoothscale(mult1, (op_width, op_height))
    mult2 = pygame.image.load("sprites/menu/mult.png")
    mult2 = pygame.transform.smoothscale(mult2, (op_width + 5, op_height + 5))
    mult = mult1

    div1 = pygame.image.load("sprites/menu/div.png")
    div1 = pygame.transform.smoothscale(div1, (op_width, op_height))
    div2 = pygame.image.load("sprites/menu/div.png")
    div2 = pygame.transform.smoothscale(div2, (op_width2, op_height2))
    div = div1

    sum1 = pygame.image.load("sprites/menu/sum.png")
    sum1 = pygame.transform.smoothscale(sum1, (op_width, op_height))
    sum2 = pygame.image.load("sprites/menu/sum.png")
    sum2 = pygame.transform.smoothscale(sum2, (op_width2, op_height2))
    sum0 = sum1

    sub1 = pygame.image.load("sprites/menu/sub.png")
    sub1 = pygame.transform.smoothscale(sub1, (op_width, op_height))
    sub2 = pygame.image.load("sprites/menu/sub.png")
    sub2 = pygame.transform.smoothscale(sub2, (op_width2, op_height2))
    sub = sub1
    
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

            if (sumx <= pygame.mouse.get_pos()[0] <= (sumx + op_width)) \
                    and (opy <= pygame.mouse.get_pos()[1] <= (opy + op_height)):
                sum0 = sum2
                if pygame.mouse.get_pressed()[0]:
                    op = "+"
                    master_math18.game(op, speed)
            else:
                sum0 = sum1

            if (subx <= pygame.mouse.get_pos()[0] <= (subx + op_width)) \
                    and (opy <= pygame.mouse.get_pos()[1] <= (opy + op_height)):
                sub = sub2
                if pygame.mouse.get_pressed()[0]:
                    op = "-"
                    master_math18.game(op, speed)
            else:
                sub = sub1

            if (multx <= pygame.mouse.get_pos()[0] <= (multx + op_width)) \
                    and (opy <= pygame.mouse.get_pos()[1] <= (opy + op_height)):
                mult = mult2
                if pygame.mouse.get_pressed()[0]:
                    op = "x"
                    master_math18.game(op, speed)
            else:
                mult = mult1
 
            if (divx <= pygame.mouse.get_pos()[0] <= (divx + op_width)) \
                    and (opy <= pygame.mouse.get_pos()[1] <= (opy + op_height)):
                div = div2
                if pygame.mouse.get_pressed()[0]:
                    op = "/"
                    master_math18.game(op, speed)
            else:
                div = div1

            if (vx <= pygame.mouse.get_pos()[0] <= (vx + v_width)) \
                    and (vy <= pygame.mouse.get_pos()[1] <= (vy + v_height)):
                return0 = return2
                if pygame.mouse.get_pressed()[0]:
                    menu_speed.menu()
            else:
                return0 = return1
            pygame.display.update()

        text = font.render("Escolha a Operação", True, text_color)

        screen.blit(background, (0, 0))
        screen.blit(sum0, (sumx, opy))
        screen.blit(sub, (subx, opy))
        screen.blit(mult, (multx, opy))
        screen.blit(div, (divx, opy))
        screen.blit(return0, (vx, vy))
        screen.blit(text, (310, 70))

        pygame.display.update()
