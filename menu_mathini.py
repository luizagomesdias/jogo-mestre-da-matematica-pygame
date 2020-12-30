import pygame
import info
import menu_speed
import arq_math

from pygame.locals import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500

ORANGE = 255, 148, 0
BLACK = 0, 0, 0


def menu():
    title_text = ORANGE
    img_width = 170
    img_height = 50

    infx = 375
    infy = 300
    jx = 375
    jy = 250
    rx = 375
    ry = 350
    sx = 375
    sy = 400

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    background = pygame.image.load("sprites/menu/background.png")
    background = pygame.transform.smoothscale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    ninja = pygame.image.load("sprites/ninja/ninja_menu.png")
    ninja = pygame.transform.scale(ninja, (150, 150))

    play1 = pygame.image.load("sprites/menu/play.png")
    play1 = pygame.transform.smoothscale(play1, (img_width, img_height))
    play2 = pygame.image.load("sprites/menu/play.png")
    play2 = pygame.transform.smoothscale(play2, (img_width + 5, img_height + 5))
    play = play1

    infoicon1 = pygame.image.load("sprites/menu/infoicon.png")
    infoicon1 = pygame.transform.smoothscale(infoicon1, (img_width, img_height))
    infoicon2 = pygame.image.load("sprites/menu/infoicon.png")
    infoicon2 = pygame.transform.smoothscale(infoicon2, (img_width + 5, img_height + 5))
    infoicon = infoicon1

    exit1 = pygame.image.load("sprites/menu/exit.png")
    exit1 = pygame.transform.smoothscale(exit1, (img_width, img_height))
    exit2 = pygame.image.load("sprites/menu/exit.png")
    exit2 = pygame.transform.smoothscale(exit2, (img_width + 5, img_height + 5))
    exit0 = exit1

    rank1 = pygame.image.load("sprites/menu/ranking.png")
    rank1 = pygame.transform.smoothscale(rank1, (img_width, img_height))
    rank2 = pygame.image.load("sprites/menu/ranking.png")
    rank2 = pygame.transform.smoothscale(rank2, (img_width + 5, img_height + 5))
    rank = rank1

    pygame.font.init()
    font = pygame.font.SysFont("Comic Sans MS", 60, True, False)

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if (infx <= pygame.mouse.get_pos()[0] <= (infx + img_width)) \
                    and (infy <= pygame.mouse.get_pos()[1] <= (infy + img_height)):
                infoicon = infoicon2
                if pygame.mouse.get_pressed()[0]:
                    info.info()
            else:
                infoicon = infoicon1

            if (jx <= pygame.mouse.get_pos()[0] <= (jx + img_width)) \
                    and (jy <= pygame.mouse.get_pos()[1] <= (jy + img_height)):
                play = play2
                if pygame.mouse.get_pressed()[0]:
                    menu_speed.menu()
            else:
                play = play1

            if (sx <= pygame.mouse.get_pos()[0] <= (sx + img_width)) \
                    and (sy <= pygame.mouse.get_pos()[1] <= (sy + img_height)):
                exit0 = exit2
                if pygame.mouse.get_pressed()[0]:
                    pygame.QUIT()
            else:
                exit0 = exit1

            if (rx <= pygame.mouse.get_pos()[0] <= (rx + img_width)) \
                    and (ry <= pygame.mouse.get_pos()[1] <= (ry + img_height)):
                rank = rank2
                if pygame.mouse.get_pressed()[0]:
                    arq_math.score()
            else:
                rank = rank1

            pygame.display.update()

        text = font.render("Mestre da Matemática", True, title_text)

        screen.blit(background, (0, 0))
        screen.blit(infoicon, (infx, infy))
        screen.blit(play, (jx, jy))
        screen.blit(exit0, (sx, sy))
        screen.blit(text, (118, 80))
        screen.blit(ninja, (SCREEN_WIDTH - 750, SCREEN_HEIGHT - 150))
        screen.blit(rank, (rx, ry))

        pygame.display.update()
