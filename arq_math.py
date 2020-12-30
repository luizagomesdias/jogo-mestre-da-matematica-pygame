from os import system
import pickle
import pygame
import menu_mathini

from pygame.locals import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500

BLACK = (0, 0, 0)
ORANGE = (255, 148, 0)
YELLOW = (255, 255, 0)


def archive(player_name, cont_right, cont_wrong):
    system("cls")
    reg = {"player_name":"", "right_op":"", "wrong_op":""}
    reg["player_name"] = player_name
    reg["right_op"] = cont_right
    reg["wrong_op"] = cont_wrong
    arq = open("score.dat", "ab")
    pickle.dump(reg, arq)
    arq.close()


def score():
    text_color = BLACK
    text_color2 = ORANGE
    text_color3 = YELLOW

    img_width = 100
    img_height = 40
    img_width2 = 105
    img_height2 = 45

    return_x = 800
    return_y = 455

    score_x = 15
    score_y = 455

    t1_width = 50
    t1_height = 100

    t2_width = 400
    t2_height = 100

    t3_width = 750
    t3_height = 100

    x = 50
    y = 150

    return1 = pygame.image.load("sprites/menu/return.png")
    return1 = pygame.transform.smoothscale(return1, (img_width, img_height))
    return2 = pygame.image.load("sprites/menu/return.png")
    return2 = pygame.transform.smoothscale(return2, (img_width2, img_height2))
    return0 = return1

    clear_score1 = pygame.image.load("sprites/menu/zerar.png")
    clear_score1 = pygame.transform.smoothscale(clear_score1, (img_width, img_height))
    clear_score2 = pygame.image.load("sprites/menu/zerar.png")
    clear_score2 = pygame.transform.smoothscale(clear_score2, (img_width2, img_height2))
    clear_score0 = clear_score1

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    background = pygame.image.load("sprites/menu/background.png")
    background = pygame.transform.smoothscale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.font.init()
    font = pygame.font.SysFont("Comic Sans MS", 30, True, False)

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
                clear_score0 = clear_score2
                if pygame.mouse.get_pressed()[0]:
                    clear_score()
            else:
                clear_score0 = clear_score1

        text = font.render("Ranking", True, text_color2)
        player = font.render("Jogador", True, text_color3)
        cont_right = font.render("Acertos", True, text_color3)
        cont_wrong = font.render("Erros", True, text_color3)

        screen.blit(background, (0, 0))
        screen.blit(text, (400, 10))
        screen.blit(player, (t1_width, t1_height))
        screen.blit(cont_right, (t2_width, t2_height))
        screen.blit(cont_wrong, (t3_width, t3_height))

        try:
            arq = open("score.dat", "rb")
            i = 0
        except:
            print("\nArquivo score.dat inexistente")
        else:
            while True:
                try:
                    reg = pickle.load(arq)
                except:
                    break
                else:
                    text_player_name = font.render(reg["player_name"], True, text_color)
                    text_cont_right = font.render(str(reg["right_op"]), True, text_color)
                    text_cont_wrong = font.render(str(reg["wrong_op"]), True, text_color)

                    screen.blit(text_player_name, (x, y + i))
                    screen.blit(text_cont_right, (x + 350, y + i))
                    screen.blit(text_cont_wrong, (x + 700, y + i))
                    i += 30
        arq.close()

        screen.blit(return0, (return_x, return_y))
        screen.blit(clear_score0, (score_x, score_y))
        pygame.display.update()


def clear_score():
    system("cls")
    arq = open("score.dat", "wb")
    arq.close()
