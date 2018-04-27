import pygame
import os
import random
import blood
from sprites import *
from pygame import gfxdraw

from message import blit_text


os.environ['SDL_VIDEO_CENTERED'] = '1'

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)
RED = (250, 20 , 0)


pygame.init()
my_font = pygame.font.SysFont("kalinga", 16)

def start_screen():
    global blood
    global my_font
    fade = False
    start = True
    alph = 0
    alphaSurface = pygame.Surface((500, 500))  # The custom-surface of the size of the screen.
    alphaSurface.fill((255, 255, 255))  # Fill it with whole white before the main-loop.
    alphaSurface.set_alpha(0)
    blood_sprites = pygame.sprite.Group()

    for i in range(3):
        bld = blood.Blood()
        bld.rect.x = random.randrange(screen_width)
        random.randrange(screen_height)
        blood_sprites.add(bld)
        pygame.display.flip()

    #my intro

    while not fade:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if pygame.time.get_ticks() > 1000 and not fade:
            fade = True
            print('go')
        else:
            screen.fill((0, 0, 0))  # At each main-loop fill the whole screen with black.
            alph += 1  # Increment alpha by a really small value (To make it slower, try 0.01)
            alphaSurface.set_alpha(alph)  # Set the incremented alpha-value to the custom surface.
            screen.blit(alphaSurface, (0, 0))  # Blit it to the screen-surface (Make them separate)

        pygame.display.flip()


    #stuff to put on start screen

    name = my_font.render("Created by Raymond Zhao", True, (0, 0, 0))
    start_text = my_font.render("Start", True, RED)

    while start:
        screen.fill(WHITE)
        screen.blit(name, (0,480))
        screen.blit(start_text, (230,240))
        screen.blit(boxpic, (100,50))
        button = pygame.gfxdraw.aaellipse(screen, 250, 250, 50, 20, RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] >= 200 and pos[0] <= 300:
                    if pos[1] >= 230 and pos[1] <= 270:
                        start = False

        for blood in blood_sprites:
            screen.blit(blood.image, (blood.rect.x, blood.rect.y))
            blood.update()
            pygame.display.flip()

        pygame.display.flip()


def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(PURPLE)
        pygame.display.flip()

start_screen()
game_loop()