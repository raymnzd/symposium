import pygame


def blit_text(message, size, color):
    my_font = pygame.font.SysFont("kalinga", 16)
    my_message = my_font.render(message, 0, color)

    return my_message
