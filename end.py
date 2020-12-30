import pygame
import menu_mathini
import arq_math

from pygame.locals import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500

BLACK = (0, 0, 0)


def end(cont_right):
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
    text_color = BLACK

    background = pygame.image.load("sprites/menu/background.png")
    background = pygame.transform.smoothscale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    number_correct_op = cont_right

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
    font2 = pygame.font.SysFont("Comic Sans MS", 35, True, False)

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

        if number_correct_op == 0:
            text = font.render("Que pena, você não acertou nenhuma operação.", True, text_color)
        elif number_correct_op == 1:
            text = font.render("Que pena, você acertou apenas 1 operação.", True, text_color)
        elif number_correct_op == 2:
            text = font.render("Que pena, você acertou apenas 2 operações.", True, text_color)
        elif number_correct_op == 3:
            text = font.render("Que pena, você acertou apenas 3 operações.", True, text_color)
        elif number_correct_op == 4:
            text = font.render("Que pena, você acertou apenas 4 operações.", True, text_color)
        elif number_correct_op == 5:
            text = font.render("Que pena, você acertou apenas 5 operações.", True, text_color)
        elif number_correct_op == 6:
            text = font.render("Que pena, você acertou apenas 6 operações.", True, text_color)
        elif number_correct_op == 7:
            text = font.render("Que pena, você acertou apenas 7 operações.", True, text_color)
        elif number_correct_op == 8:
            text = font.render("Que pena, você acertou apenas 8 operações.", True, text_color)
        elif number_correct_op == 9:
            text = font.render("Que pena, você acertou apenas 9 operações.", True, text_color)

        game_over = font2.render("Fim de jogo!", True, text_color)

        screen.blit(background, (0, 0))
        screen.blit(text, (170, 180))
        screen.blit(game_over, (330, 110))
        screen.blit(return0, (return_x, return_y))
        screen.blit(score0, (score_x, score_y))

        pygame.display.update()
