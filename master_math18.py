import pygame
import random
import menu_mathini
import end
import won
import arq_math
import player_name

from pygame.locals import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500

YELLOW = (255, 255, 0)


def game(op, speed):
    class Health(pygame.sprite.Sprite):

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)

            self.images_hp = [pygame.image.load('sprites/hp/hp0..png').convert_alpha(),
                              pygame.image.load('sprites/hp/hp1.png').convert_alpha(),
                              pygame.image.load('sprites/hp/hp2.png').convert_alpha(),
                              pygame.image.load('sprites/hp/hp3.png').convert_alpha(),
                              pygame.image.load('sprites/hp/hp4.png').convert_alpha(),
                              pygame.image.load('sprites/hp/hp5.png').convert_alpha()]

            self.hp_widht = 360
            self.hp_height = 35
            self.image = pygame.image.load('sprites/hp/hp0..png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.hp_widht, self.hp_height))
            self.rect = self.image.get_rect()
            self.rect[0] = SCREEN_WIDTH - 870
            self.rect[1] = SCREEN_HEIGHT - 490
            self.wrong = 0
            self.right = 0

        def update(self):
            if self.wrong == 1:
                self.image = self.images_hp[1]
                self.image = pygame.transform.scale(self.image, (self.hp_widht, self.hp_height))
            elif self.wrong == 2:
                self.image = self.images_hp[2]
                self.image = pygame.transform.scale(self.image, (self.hp_widht, self.hp_height))
            elif self.wrong == 3:
                self.image = self.images_hp[3]
                self.image = pygame.transform.scale(self.image, (self.hp_widht, self.hp_height))
            elif self.wrong == 4:
                self.image = self.images_hp[5]
                self.image = pygame.transform.scale(self.image, (self.hp_widht, self.hp_height))
            elif self.wrong == 5:
                self.image = self.images_hp[5]
                self.image = pygame.transform.scale(self.image, (self.hp_widht, self.hp_height))
                self.player_name = player_name.menu()
                arq_math.archive(self.player_name, self.right, self.wrong)
                end.end(self.right)

    class Return(pygame.sprite.Sprite):

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)

            self.images = pygame.image.load('sprites/menu/menu.png').convert_alpha()
            self.image = pygame.image.load('sprites/menu/menu.png').convert_alpha()
            self.return_width = 100
            self.return_height = 40
            self.return_width2 = 105
            self.return_height2 = 45
            self.image = pygame.transform.smoothscale(self.image, (self.return_width, self.return_height))
            self.image2 = pygame.transform.smoothscale(self.image, (self.return_width2, self.return_height2))
            self.imagep = pygame.transform.smoothscale(self.image, (self.return_width, self.return_height))
            self.rect = self.image.get_rect()
            self.rect[0] = 800
            self.rect[1] = 455

        def update(self):
            if (self.rect[0] <= pygame.mouse.get_pos()[0] <= (self.rect[0] + self.return_width)) \
                    and (self.rect[1] <= pygame.mouse.get_pos()[1] <= (self.rect[1] + self.return_height)):
                self.image = self.image2
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.music.stop()
                    menu_mathini.menu()
            else:
                self.image = self.imagep

    class Ninja(pygame.sprite.Sprite):

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)

            self.images_idle = [pygame.image.load('sprites/ninja/idle0.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/idle1.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/idle2.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/idle3.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/idle4.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/idle5.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/idle6.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/idle7.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/idle8.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/idle9.png').convert_alpha()]

            self.images_right = [pygame.image.load('sprites/ninja/run0R.png').convert_alpha(),
                                 pygame.image.load('sprites/ninja/run1R.png').convert_alpha(),
                                 pygame.image.load('sprites/ninja/run2R.png').convert_alpha(),
                                 pygame.image.load('sprites/ninja/run3R.png').convert_alpha(),
                                 pygame.image.load('sprites/ninja/run4R.png').convert_alpha(),
                                 pygame.image.load('sprites/ninja/run5R.png').convert_alpha(),
                                 pygame.image.load('sprites/ninja/run6R.png').convert_alpha(),
                                 pygame.image.load('sprites/ninja/run7R.png').convert_alpha(),
                                 pygame.image.load('sprites/ninja/run8R.png').convert_alpha(),
                                 pygame.image.load('sprites/ninja/run9R.png').convert_alpha()]

            self.images_left = [pygame.image.load('sprites/ninja/run0L.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/run1L.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/run2L.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/run3L.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/run4L.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/run5L.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/run6L.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/run7L.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/run8L.png').convert_alpha(),
                                pygame.image.load('sprites/ninja/run9L.png').convert_alpha()]

            self.current_image = 0
            self.ninja_width = 85
            self.ninja_height = 120
            self.image = pygame.image.load('sprites/ninja/idle0.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.ninja_width, self.ninja_height))
            self.position = 'idle'
            self.jump_sound = pygame.mixer.Sound("audio/wing.wav")

            self.rect = self.image.get_rect()
            self.rect[0] = SCREEN_WIDTH - SCREEN_WIDTH
            self.rect[1] = SCREEN_HEIGHT / 1.5

        def update(self):
            if self.position == 'left':
                self.current_image = (self.current_image + 1) % 10
                self.image = self.images_left[self.current_image]
                self.image = pygame.transform.scale(self.image, (self.ninja_width, self.ninja_height))
            if self.position == 'right':
                self.current_image = (self.current_image + 1) % 10
                self.image = self.images_right[self.current_image]
                self.image = pygame.transform.scale(self.image, (self.ninja_width, self.ninja_height))
            if self.position == 'idle':
                self.current_image = (self.current_image + 1) % 10
                self.image = self.images_idle[self.current_image]
                self.image = pygame.transform.scale(self.image, (self.ninja_width, self.ninja_height))

        def down(self):
            self.rect[1] += 150

        def jump(self):
            self.rect[1] -= 150
            self.jump_sound.play()

        def right(self):
            if self.rect[0] <= (SCREEN_WIDTH - 100):
                self.rect[0] += 35
            self.position = 'right'

        def left(self):
            if self.rect[0] >= 35:
                self.rect[0] -= 35
            self.position = 'left'

        def idle(self):
            self.position = 'idle'

    class Number(pygame.sprite.Sprite):

        def __init__(self, column):
            pygame.sprite.Sprite.__init__(self)

            self.number_images = [pygame.image.load('sprites/number/0.png').convert_alpha(),
                                  pygame.image.load('sprites/number/1.png').convert_alpha(),
                                  pygame.image.load('sprites/number/2.png').convert_alpha(),
                                  pygame.image.load('sprites/number/3.png').convert_alpha(),
                                  pygame.image.load('sprites/number/4.png').convert_alpha(),
                                  pygame.image.load('sprites/number/5.png').convert_alpha(),
                                  pygame.image.load('sprites/number/6.png').convert_alpha(),
                                  pygame.image.load('sprites/number/7.png').convert_alpha(),
                                  pygame.image.load('sprites/number/8.png').convert_alpha(),
                                  pygame.image.load('sprites/number/9.png').convert_alpha(),
                                  pygame.image.load('sprites/number/10.png').convert_alpha()]

            self.current_number = generate_random_number()
            self.number_widht = 45
            self.number_height = 45
            self.level = speed
            self.column = column
            self.image = self.number_images[self.current_number]
            self.image = pygame.transform.scale(self.image, (self.number_widht, self.number_height))
            self.collide_sound = pygame.mixer.Sound("audio/point.wav")

            self.rect = self.image.get_rect()
            self.rect[0] = generate_random_width_position(self.column)
            self.rect[1] = generate_random_height_initial_position()

        def update(self):
            height_position1 = self.rect[1]
            if height_position1 > SCREEN_HEIGHT:
                self.current_number = generate_random_number()
                self.image = self.number_images[self.current_number]
                self.image = pygame.transform.scale(self.image, (self.number_widht, self.number_height))
                self.rect[1] = generate_random_height_initial_position()
                self.rect[0] = generate_random_width_position(self.column)
            if self.level == "easy":
                self.rect[1] += 10
            if self.level == "middle":
                self.rect[1] += 15
            if self.level == "hard":
                self.rect[1] += 20

        def collide(self):
            self.collide_sound.play()
            self.rect[1] = SCREEN_HEIGHT + 100

    class Operation(pygame.sprite.Sprite):

        def __init__(self, op):
            pygame.sprite.Sprite.__init__(self)

            self.images_score = [pygame.image.load('sprites/number/n0.png').convert_alpha(),
                                 pygame.image.load('sprites/number/n1.png').convert_alpha(),
                                 pygame.image.load('sprites/number/n2.png').convert_alpha(),
                                 pygame.image.load('sprites/number/n3.png').convert_alpha(),
                                 pygame.image.load('sprites/number/n4.png').convert_alpha(),
                                 pygame.image.load('sprites/number/n5.png').convert_alpha(),
                                 pygame.image.load('sprites/number/n6.png').convert_alpha(),
                                 pygame.image.load('sprites/number/n7.png').convert_alpha(),
                                 pygame.image.load('sprites/number/n8.png').convert_alpha(),
                                 pygame.image.load('sprites/number/n9.png').convert_alpha(),
                                 pygame.image.load('sprites/number/n10.png').convert_alpha()]

            self.current_number = 0
            self.operand_1 = "?"
            self.operand_2 = "?"
            self.math_operator = op
            self.equal = "="
            self.cont_right = 0
            self.cont_wrong = 0
            self.operand_width = 40
            self.operand_height = 40
            self.text_color = YELLOW
            self.image = self.images_score[self.current_number]
            self.image = pygame.transform.scale(self.image, (self.operand_width, self.operand_height))
            self.collide_sound = pygame.mixer.Sound("audio/point.wav")
            self.score_sound = pygame.mixer.Sound("audio/score.wav")
            self.error_sound = pygame.mixer.Sound("audio/uhoh.wav")

            self.rect = self.image.get_rect()
            self.rect[0] = SCREEN_WIDTH - 785
            self.rect[1] = SCREEN_HEIGHT - 440

            self.expected_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                    12, 14, 15, 16, 18, 20, 21, 24,
                                    25, 27, 28, 30, 32, 35, 36, 40,
                                    42, 45, 48, 49, 50, 54, 56, 60,
                                    63, 64, 70, 72, 80, 81, 90, 100]

            self.division_matrix = [[],
                                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
                                    [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],
                                    [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],
                                    [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
                                    [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],
                                    [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],
                                    [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],
                                    [9, 18, 27, 36, 45, 54, 63, 72, 81, 90],
                                    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]]

            self.sub_matrix = [[],
                               [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                               [3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                               [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                               [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
                               [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                               [7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                               [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                               [9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
                               [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                               [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]

            self.operation = []

            if self.math_operator == "x":
                self.expected_result = self.expected_number[generate_random_mult_operation()]

            if self.math_operator == "+":
                self.expected_result = generate_random_sum_operation()

            if self.math_operator == "/":
                self.expected_result = "?"
                self.operand_2 = generate_random_op2()
                self.operand_1 = random.choice(self.division_matrix[self.operand_2])

            if self.math_operator == "-":
                self.expected_result = "?"
                self.operand_2 = generate_random_op2()
                self.operand_1 = random.choice(self.sub_matrix[self.operand_2])

        def update(self, screen_text):
            self.current_number = self.cont_right
            self.image = self.images_score[self.current_number]
            self.image = pygame.transform.scale(self.image, (self.operand_width, self.operand_height))
            text_operand_1 = font.render("{}".format(self.operand_1), True, self.text_color)
            screen_text.blit(text_operand_1, (SCREEN_WIDTH - 250, SCREEN_HEIGHT - 480))
            text_math_operator = font.render("{}".format(self.math_operator), True, self.text_color)
            screen_text.blit(text_math_operator, (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 480))
            text_operand_2 = font.render("{}".format(self.operand_2), True, self.text_color)
            screen_text.blit(text_operand_2, (SCREEN_WIDTH - 150, SCREEN_HEIGHT - 480))
            text_equal = font.render("{}".format(self.equal), True, self.text_color)
            screen_text.blit(text_equal, (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 480))
            text_cont_right = font_2.render("Acertos:{}".format(self.cont_right), True, self.text_color)
            screen_text.blit(text_cont_right, (SCREEN_WIDTH - 870, SCREEN_HEIGHT - 440))
            text_expected_result = font.render("{}".format(self.expected_result), True, self.text_color)
            screen_text.blit(text_expected_result, (SCREEN_WIDTH - 50, SCREEN_HEIGHT - 480))

        def set_number(self, number):
            if self.math_operator == "x" or self.math_operator == "+":
                if len(self.operation) < 2:
                    self.operation.append(number)
                    if len(self.operation) == 1:
                        self.operand_1 = self.operation[0]
                    if len(self.operation) == 2:
                        self.operand_2 = self.operation[1]

                if len(self.operation) == 2:
                    if self.math_operator == "x":
                        operation_result = self.operation[0] * self.operation[1]
                        if operation_result == self.expected_result:
                            self.score_sound.play()
                            self.cont_right += 1
                            health.right += 1
                            self.change()
                            if self.cont_right == 10:
                                self.player_name = player_name.menu()
                                arq_math.archive(self.player_name, self.cont_right, self.cont_wrong)
                                won.end()
                        else:
                            self.error_sound.play()
                            self.cont_wrong += 1
                            health.wrong += 1
                            self.change()

                    if self.math_operator == "+":
                        operation_result = self.operation[0] + self.operation[1]
                        if operation_result == self.expected_result:
                            self.score_sound.play()
                            self.cont_right += 1
                            health.right += 1
                            self.change()
                            if self.cont_right == 10:
                                self.player_name = player_name.menu()
                                arq_math.archive(self.player_name, self.cont_right, self.cont_wrong)
                                won.end()
                        else:
                            self.error_sound.play()
                            self.cont_wrong += 1
                            health.wrong += 1
                            self.change()

                    self.operation.clear()

            if self.math_operator == "/" or self.math_operator == "-":
                if len(self.operation) < 1:
                    self.operation.append(number)
                    self.expected_result = self.operation[0]

                    if self.math_operator == "/":
                        operation_result = self.operand_1 / self.operand_2
                        if operation_result == self.expected_result:
                            self.score_sound.play()
                            self.cont_right += 1
                            health.right += 1
                            self.change()
                            if self.cont_right == 10:
                                self.player_name = player_name.menu()
                                arq_math.archive(self.player_name, self.cont_right, self.cont_wrong)
                                won.end()
                        else:
                            self.error_sound.play()
                            self.cont_wrong += 1
                            health.wrong += 1
                            self.change()

                    if self.math_operator == "-":
                        operation_result = self.operand_1 - self.operand_2
                        if operation_result == self.expected_result:
                            self.score_sound.play()
                            self.cont_right += 1
                            health.right += 1
                            self.change()
                            if self.cont_right == 10:
                                self.player_name = player_name.menu()
                                arq_math.archive(self.player_name, self.cont_right, self.cont_wrong)
                                won.end()
                        else:
                            self.error_sound.play()
                            self.cont_wrong += 1
                            health.wrong += 1
                            self.change()

                    self.operation.clear()

        def change(self):
            if self.math_operator == "x":
                self.operand_1 = "?"
                self.operand_2 = "?"
                self.expected_result = self.expected_number[generate_random_mult_operation()]

            if self.math_operator == "+":
                self.operand_1 = "?"
                self.operand_2 = "?"
                self.expected_result = generate_random_sum_operation()

            if self.math_operator == "/":
                self.operand_2 = generate_random_op2()
                self.operand_1 = random.choice(self.division_matrix[self.operand_2])
                self.expected_result = "?"

            if self.math_operator == "-":
                self.expected_result = "?"
                self.operand_2 = generate_random_op2()
                self.operand_1 = random.choice(self.sub_matrix[self.operand_2])

    def generate_random_number():
        return random.randint(0, 10)

    def generate_random_mult_operation():
        return random.randint(0, 41)

    def generate_random_sum_operation():
        return random.randint(0, 20)

    def generate_random_op2():
        return random.randint(1, 10)

    def generate_random_height_initial_position():
        return random.randint(-400, 0)

    def generate_random_width_position(column):
        init_value = SCREEN_WIDTH / 4 * (column - 1)
        end_value = (SCREEN_WIDTH / 4 * column) - 50
        return random.randint(init_value, end_value)


    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.SysFont("Comic Sans MS", 30, True, False)
    font_2 = pygame.font.SysFont("Comic Sans MS", 20, True, False)

    background = pygame.image.load("sprites/city_ninja.png")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.mixer.music.load("audio/music.mpeg")
    pygame.mixer.music.play(-1)

    ninja_group = pygame.sprite.Group()
    ninja = Ninja()
    ninja_group.add(ninja)

    return_group = pygame.sprite.Group()
    return_class = Return()
    return_group.add(return_class)

    number_group = pygame.sprite.Group()
    number1 = Number(column=1)
    number2 = Number(column=2)
    number3 = Number(column=3)
    number4 = Number(column=4)
    number_group.add(number1)
    number_group.add(number2)
    number_group.add(number3)
    number_group.add(number4)

    operation_group = pygame.sprite.Group()
    operation = Operation(op)
    operation_group.add(operation)

    health_group = pygame.sprite.Group()
    health = Health()
    health_group.add(health)

    clock = pygame.time.Clock()

    while True:
        clock.tick(15)

        key = pygame.key.get_pressed()
        if key[K_LEFT]:
            ninja.left()
        if key[K_RIGHT]:
            ninja.right()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    ninja.jump()
            elif event.type == KEYUP:
                if event.key == K_UP:
                    ninja.down()
                ninja.idle()

        screen.blit(background, (0, 0))
        screen.blit(background, (0, 0))

        number_group.update()
        number_group.draw(screen)

        return_group.update()
        return_group.draw(screen)

        ninja_group.update()
        ninja_group.draw(screen)

        health_group.update()
        health_group.draw(screen)

        operation_group.update(screen)
        operation_group.draw(screen)

        pygame.display.update()

        if pygame.sprite.collide_mask(ninja, number1):
            operation.set_number(number1.current_number)
            number1.collide()

        if pygame.sprite.collide_mask(ninja, number2):
            operation.set_number(number2.current_number)
            number2.collide()

        if pygame.sprite.collide_mask(ninja, number3):
            operation.set_number(number3.current_number)
            number3.collide()

        if pygame.sprite.collide_mask(ninja, number4):
            operation.set_number(number4.current_number)
            number4.collide()
