import sys
import time
import pygame
from constants import *
from button import Text_button
import random

pygame.init()
font = pygame.font.Font('fonts\Wainscoted.ttf', 34)
small_font = pygame.font.Font('fonts\Patrick Tonight.otf', 30)

window_x = 800
window_y = 600

fps = pygame.time.Clock()

snake_position = []
snake_body = []
snake_speed = 0
fruit_spawn = True
direction = ''
movement = direction
is_defeate = False
score = 0
is_pause = False


def reset_game():

    global snake_position, snake_body, snake_speed, fruit_spawn, direction, movement, is_defeate, score
    snake_position = [100, 50]
    snake_body = [[100, 50],
                  [90, 50],
                  [80, 50],
                  [70, 50]]
    snake_speed = 15
    fruit_spawn = True
    direction = 'RIGHT'
    movement = direction
    is_defeate = False
    score = 0


reset_game()

fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]


screen = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('SNAKE GAME')

history_game_button = Text_button(x=80, y=200, width=200, heigth=100,
                                  text="Historial de\npartidas", font=font, bg_color=PURPLE,
                                  text_color=WHITE, border_width=3)

game_button = Text_button(x=300, y=200, width=200,
                          heigth=100, text="Jugar", font=font, bg_color=BLACK_PURPLE,
                          text_color=WHITE, border_width=3)

exit_button = Text_button(x=520, y=200, width=200,
                          heigth=100, text="Salir", font=font, text_color=WHITE,
                          border_width=3, bg_color=PURPLE)

return_button = Text_button(x=10, y=500, width=200,
                            heigth=60, text="Regresar", font=font, text_color=WHITE,
                            bg_color=BLACK_PURPLE, border_width=3)

current_screen = MAIN_SCREEN


fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]


def check_defeate(snake_position, snake_body):
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        return True
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        return True
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            return True
    return False


def pause_screen():
    game_over_surface = font.render(
        'El juego se pauso', True, WHITE)
    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (window_x/2, window_y/2)

    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    text = 'Presiona una tecla para continuar\no escape para salir'
    lines = text.split('\n')
    for i, line in enumerate(lines):

        text_surface = font.render(line, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (window_x/2, window_y/2 + (i + 1)*40)
        screen.blit(text_surface, text_rect)


def dead_screen():
    game_over_surface = font.render(
        'Tu puntuación es: ' + str(score), True, WHITE)
    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (window_x/2, window_y/2)

    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(1)
    game_over_surface = font.render(
        'Presiona una tecla para continuar', True, WHITE)
    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = (window_x/2, window_y/2 + 40)

    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()


def main_screen():
    screen.fill(LILAC)

    history_game_button.draw_button(screen)
    game_button.draw_button(screen)
    exit_button.draw_button(screen)

    text_surface = small_font.render("VaneLiss", True, BLACK_PURPLE)
    text_rect = text_surface.get_rect(topleft=(660, 550))
    screen.blit(text_surface, text_rect)


def game_screen(snake_body, fruit_position, screen):
    screen.fill(LILAC)

    score_text = font.render(f'Puntuación: {score}', True, WHITE)
    score_rect = score_text.get_rect()

    screen.blit(score_text, score_rect)

    for pos in snake_body:
        pygame.draw.rect(screen, BLACK_PURPLE,
                         pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, RED, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))


def game_history_screen():
    screen.fill(LILAC)

    return_button.draw_button(screen)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if (current_screen == MAIN_SCREEN):
                if history_game_button.rect.collidepoint(mouse_pos):
                    current_screen = GAME_HISTORY_SCREEN
                elif game_button.rect.collidepoint(mouse_pos):
                    current_screen = GAME_SCREEN
                elif exit_button.rect.collidepoint(mouse_pos):
                    running = False
                    pygame.quit()
                    sys.exit()
            if current_screen == GAME_HISTORY_SCREEN:
                if return_button.rect.collidepoint(mouse_pos):
                    current_screen = MAIN_SCREEN
            if current_screen == GAME_SCREEN:
                if return_button.rect.collidepoint(mouse_pos):
                    current_screen = MAIN_SCREEN
        elif event.type == pygame.KEYDOWN and current_screen == GAME_SCREEN:
            if is_defeate:
                current_screen = MAIN_SCREEN
                reset_game()
            if is_pause:
                if event.key == pygame.K_ESCAPE:
                    current_screen = MAIN_SCREEN
                    reset_game()
                is_pause = False

            if event.key == pygame.K_UP:
                movement = 'UP'
            if event.key == pygame.K_DOWN:
                movement = 'DOWN'
            if event.key == pygame.K_LEFT:
                movement = 'LEFT'
            if event.key == pygame.K_RIGHT:
                movement = 'RIGHT'
            if event.key == pygame.K_SPACE:
                is_pause = True

    if current_screen == MAIN_SCREEN:

        main_screen()

    elif current_screen == GAME_SCREEN:

        if movement == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if movement == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if movement == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if movement == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        is_defeate = check_defeate(snake_position, snake_body)

        if not is_defeate and not is_pause:

            if direction == 'UP':
                snake_position[1] -= 10
            if direction == 'DOWN':
                snake_position[1] += 10
            if direction == 'LEFT':
                snake_position[0] -= 10
            if direction == 'RIGHT':
                snake_position[0] += 10

            if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
                score += 10
                snake_speed += 2
                fruit_spawn = False
            else:
                snake_body.pop()

            snake_body.insert(0, list(snake_position))
            if not fruit_spawn:
                fruit_position = [random.randrange(1, (window_x//10)) * 10,
                                  random.randrange(1, (window_y//10)) * 10]
            fruit_spawn = True

            game_screen(snake_body, fruit_position, screen)
        elif is_defeate:
            dead_screen()
        elif is_pause:
            pause_screen()

    elif current_screen == GAME_HISTORY_SCREEN:
        game_history_screen()

    pygame.display.flip()

    fps.tick(snake_speed)
