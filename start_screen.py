#might be my start screen

import pygame
import random

pygame.init()
screen_width = 500
screen_height = 500
WHITE = (255, 255, 255)
screen = pygame.display.set_mode([screen_width, screen_height])

my_font = pygame.font.SysFont("kalinga", 16)
the_text = my_font.render("Created by Raymond Zhao", True, (0, 0, 0))
boxpic = pygame.image.load(("images/boxhead.png"))
text_rect = the_text.get_rect()
screen.fill(WHITE)

running = True

all_fonts = pygame.font.get_fonts()

print("done")
while running:
    mx, my = pygame.mouse.get_pos()
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_rect.collidepoint(pygame.mouse.get_pos()):
                print("yes" + str(random.randint(0,100)))
    screen.blit(the_text, (0, 480))
    screen.blit(boxpic, (100,50))
    pygame.display.flip()
