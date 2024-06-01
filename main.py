import sys
import pygame
from constants import *
from button import Text_button

pygame.init()
font = pygame.font.Font('fonts\Wainscoted.ttf', 34)
small_font = pygame.font.Font('fonts\Patrick Tonight.otf', 30)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('SNAKE GAME')

current_screen = MAIN_SCREEN

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



def main_screen():
    screen.fill(LILAC)

    history_game_button.draw_button(screen)
    game_button.draw_button(screen)
    exit_button.draw_button(screen)

    text_surface = small_font.render("VaneLiss", True, BLACK_PURPLE)
    text_rect = text_surface.get_rect(topleft=(660, 550))
    screen.blit(text_surface, text_rect)


def game_screen():
    screen.fill(LILAC)

    return_button.draw_button(screen)


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
            if current_screen == MAIN_SCREEN:
                if history_game_button.rect.collidepoint(mouse_pos):
                    current_screen = GAME_HISTORY_SCREEN
                elif game_button.rect.collidepoint(mouse_pos):
                    current_screen = GAME_SCREEN
                elif exit_button.rect.collidepoint(mouse_pos):
                    running = False
                    pygame.quit()
                    sys.exit()
            elif current_screen == GAME_HISTORY_SCREEN:
                if return_button.rect.collidepoint(mouse_pos):
                    current_screen = MAIN_SCREEN
            elif current_screen == GAME_SCREEN:
                if return_button.rect.collidepoint(mouse_pos):
                    current_screen = MAIN_SCREEN

    if current_screen == MAIN_SCREEN:
        main_screen()
    elif current_screen == GAME_SCREEN:
        game_screen()
    elif current_screen == GAME_HISTORY_SCREEN:
        game_history_screen()

    pygame.display.flip()