#might be my start screen

import pygame
import random
import numpy as np
import matplotlib.pyplot as plt
import os
import time
from pygame import gfxdraw
from constants import *



pygame.init()

# all_fonts = pygame.font.get_fonts()

class Blood(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = bloodpic
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = random.randrange(screen_width)
        self.rect.y = random.randrange(screen_height)
        pygame.display.update()

blood_sprites = pygame.sprite.Group()

for i in range(3):
    blood = Blood()
    blood.rect.x = random.randrange(screen_width)
    random.randrange(screen_height)
    blood_sprites.add(blood)
    pygame.display.flip()





class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = player_down_pic
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 300

    def move(self, dir):
        if dir == 'a':
            self.rect.x -= 1
        if dir == 'd':
            self.rect.x += 1
        if dir == 's':
            self.rect.y += 1
        if dir == 'w':
            self.rect.y -= 1
        if dir == 'wa':
            self.rect.y -= 1
            self.rect.x -= 1
        if dir == 'wd':
            self.rect.y -= 1
            self.rect.x += 1
        if dir == 'sa':
            self.rect.y += 1
            self.rect.x -= 1
        if dir == 'sd':
            self.rect.y += 1
            self.rect.x += 1


class Start():

    def __init__(self):
        my_font = pygame.font.SysFont("kalinga", 16)
        self.name = my_font.render("Created by Raymond Zhao", True, (0, 0, 0))
        self.name_rect = self.name.get_rect()

        self.start_text = my_font.render("Start", True, RED )
        self.start_rect = self.start_text.get_rect()

        pass

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pos[0] >= 200 and pos[0] <= 300:
                if pos[1] >= 230 and pos[1] <= 270:
                    global scene
                    scene = scenes['Play']



        if event.type == pygame.QUIT:
            running = False
            print('this should stop')


    def draw(self):
        screen.fill(WHITE)
        screen.blit(self.name, (0,480))
        screen.blit(boxpic, (100,50))

        self.button = pygame.gfxdraw.aaellipse(screen, 250, 250, 50, 20, RED)
        screen.blit(self.start_text, (230,240))
        # pygame.draw.filled_ellipse(screen, 250, 250, 50, 20, RED)

        timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_event, 1)
        for blood in blood_sprites:
            screen.blit(blood.image, (blood.rect.x, blood.rect.y))
            blood.update()
            pygame.display.flip()






    def update(self):
        pass



class Play():

    def __init__(self):
        self.x = 0
        self.clicked = False
        if scene == self:
            self.slide()

        self.player = Player()

    def handle_event(self, event):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_a] and not pressed[pygame.K_w] and not pressed[pygame.K_s]:
            self.player.move('a')
            self.player.image = player_left_pic

        if pressed[pygame.K_w]:
            if pressed[pygame.K_a]:
                self.player.move('wa')
                self.player.image = player_upleft_pic
            elif pressed[pygame.K_d]:
                self.player.move('wd')
                self.player.image = player_upright_pic
            else:
                self.player.move('w')
                self.player.image = player_up_pic

        if pressed[pygame.K_s]:
            if pressed[pygame.K_a]:
                self.player.move('sa')
                self.player.image = player_downleft_pic
            elif pressed[pygame.K_d]:
                self.player.move('sd')
                self.player.image = player_downright_pic
            else:
                self.player.move('s')
                self.player.image = player_down_pic

        if pressed[pygame.K_d] and not pressed[pygame.K_w] and not pressed[pygame.K_s]:
            self.player.move('d')
            self.player.image = player_right_pic





    def slide(self):
        self.x += 1
        screen.fill(WHITE)
        surf = pygame.draw.rect(screen, (0, 0, 255), (self.x, 0, 500, 500))

    def draw(self):
        if scene == self:
            self.slide()
        # pygame.draw.rect(screen, (PURPLE), (0, 0, 50, 50))
        x = 0
        # if scene == self:
        #     while surf.x < 510:
        #         pygame.display.update()
        #         screen.fill((255, 255, 255))
        #         surf = pygame.draw.rect(screen, (0, 0, 255), (x, 0, 500, 500))
        #         time.sleep(.03)
        #         x += 1
        screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        screen.fil(WHITE)


    def update(self):
        pass



scene = ""
scenes = {'Start': Start(), 'Play': Play()}


class Boxhead():

    def __init__(self):

        self.screen = screen
        self.alphaSurface = pygame.Surface((500, 500))  # The custom-surface of the size of the screen.
        self.alphaSurface.fill((255, 255, 255))  # Fill it with whole white before the main-loop.
        self.alphaSurface.set_alpha(0)  # Set alpha to 0 before the main-loop.
        self.alph = 0  # The increment-variable.
        self.started = False
        self.start()


    def start(self):
        running = True
        global scene
        global scenes
        while running:

            clock.tick(60)


            if pygame.time.get_ticks() > 2500 and not self.started:
                scene = scenes['Start']
                scene.draw()
                self.started = True
                print('lol')
            else:
                self.screen.fill((0, 0, 0))  # At each main-loop fill the whole screen with black.
                self.alph += 1  # Increment alpha by a really small value (To make it slower, try 0.01)
                self.alphaSurface.set_alpha(self.alph)  # Set the incremented alpha-value to the custom surface.
                self.screen.blit(self.alphaSurface, (0, 0))  # Blit it to the screen-surface (Make them separate)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


                try:
                    scene.handle_event(event)
                    scene.update()
                    scene.draw()
                except:
                    pass
            pygame.display.flip()



if __name__ == "__main__":
    game = Boxhead()