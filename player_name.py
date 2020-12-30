import pygame,sys

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500

BLACK = (0, 0, 0)


def menu():
    pygame.init()
    text_color = BLACK
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    background = pygame.image.load("sprites/menu/background.png")
    background = pygame.transform.smoothscale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    base_font = pygame.font.Font(None,32)
    user_text = ''

    input_rect = pygame.Rect(350, 170, 0, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('gray15')

    pygame.font.init()
    font = pygame.font.SysFont("Comic Sans MS", 30, True, False)

    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

                if event.key == pygame.K_END:
                    return user_text

        if active == True:
            color = color_active
        else:
            color = color_passive

        pygame.draw.rect(background, color, input_rect, 2)

        text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(100,text_surface.get_width() + 10)

        text = font.render("Digite o nome do jogador e ao finalizar aperte a tecla END", True, text_color)

        pygame.display.flip()
        screen.blit(background, (0, 0))
        screen.blit(text, (5, 70))
        clock.tick(60)
