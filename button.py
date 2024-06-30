import pygame
from constants import BLACK, WHITE


class Text_button():
    def __init__(self, x, y, width, heigth, text, font, bg_color=WHITE,
                 text_color=BLACK, borde_color=WHITE, border_width=0):
        self.rect = pygame.Rect(x, y, width, heigth)
        self.text = text
        self.bg_color = bg_color
        self.font = font
        self.text_color = text_color
        self.border_color = borde_color
        self.border_width = border_width

    def draw_button(self, screen):
        inner_rect = pygame.Rect(self.rect[0] + self.border_width,  # Define el rectangulo interior
                                 self.rect[1] + self.border_width,
                                 self.rect[2] - 2*self.border_width,
                                 self.rect[3] - 2*self.border_width)

        # Dibujamos rectangulo grande(Borde)
        pygame.draw.rect(screen, self.border_color, self.rect)
        # Dibujamos rectangulo pequeño
        pygame.draw.rect(screen, self.bg_color, inner_rect)

        
        lines = self.text.split('\n')

        for i, line in enumerate(lines):

            text_surface = self.font.render(line, True, self.text_color)
            text_rect = text_surface.get_rect(center=(
                self.rect[0] + self.rect[2] // 2, self.rect[1] + (i + 1) * self.rect[3] // (len(lines) + 1)))
            screen.blit(text_surface, text_rect)
