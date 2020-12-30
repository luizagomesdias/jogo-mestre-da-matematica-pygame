import pygame
import menu_mathini
import arq_math

from pygame.locals import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500

ORANGE = (255, 148, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


def end():
    pygame.mixer.music.stop()

    img_width = 100
    img_height = 40
    img_width2 = 105
    img_height2 = 45

    return_x = 800
    return_y = 455

    score_x = 400
    score_y = 230

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    text_color_won = GREEN

    background = pygame.image.load("sprites/menu/background.png")
    background = pygame.transform.smoothscale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    return1 = pygame.image.load("sprites/menu/return.png")
    return1 = pygame.transform.smoothscale(return1, (img_width, img_height))
    return2 = pygame.image.load("sprites/menu/return.png")
    return2 = pygame.transform.smoothscale(return2, (img_width2, img_height2))
    return0 = return1

    score1 = pygame.image.load("sprites/menu/ranking.png")
    score1 = pygame.transform.smoothscale(score1, (img_width, img_height))
    score2 = pygame.image.load("sprites/menu/ranking.png")
    score2 = pygame.transform.smoothscale(score2, (img_width2, img_height2))
    score0 = score1

    pygame.font.init()
    font = pygame.font.SysFont("Comic Sans MS", 25, True, False)
    font3 = pygame.font.SysFont("Comic Sans MS", 55, True, False)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if (return_x <= pygame.mouse.get_pos()[0] <= (return_x + img_width)) \
                    and (return_y <= pygame.mouse.get_pos()[1] <= (return_y + img_height)):
                return0 = return2
                if pygame.mouse.get_pressed()[0]:
                    menu_mathini.menu()
            else:
                return0 = return1

            if (score_x <= pygame.mouse.get_pos()[0] <= (score_x + img_width)) \
                    and (score_y <= pygame.mouse.get_pos()[1] <= (score_y + img_height)):
                score0 = score2
                if pygame.mouse.get_pressed()[0]:
                    arq_math.score()
            else:
                score0 = score1

        congratulations_text = font3.render("Parabéns!!!", True, ORANGE)
        text = font.render("Você se tornou um mestre da matemática!!!", True, text_color_won)

        screen.blit(background, (0, 0))
        screen.blit(text, (190, 180))
        screen.blit(congratulations_text, (315, 110))
        screen.blit(return0, (return_x, return_y))
        screen.blit(score0, (score_x, score_y))

        pygame.display.update()
