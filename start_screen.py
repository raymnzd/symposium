#might be my start screen

import pygame
import random
import os
from constants import *


pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])


my_font = pygame.font.SysFont("kalinga", 16)
the_text = my_font.render("Created by Raymond Zhao", True, (0, 0, 0))
text_rect = the_text.get_rect()


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


class Start():

    def __init__(self):
        pass

    def handle_event(self, event):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print('this should stop')

    def draw(self):
        screen.fill(WHITE)
        screen.blit(the_text, (0,480))
        screen.blit(boxpic, (100,50))
        timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_event, 1)
        for blood in blood_sprites:
            screen.blit(blood.image, (blood.rect.x, blood.rect.y))
            blood.update()
            pygame.display.flip()


    def update(self):
        pass





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
        while running:

            clock.tick(60)
            self.screen.fill((0, 0, 0))  # At each main-loop fill the whole screen with black.
            self.alph += 1  # Increment alpha by a really small value (To make it slower, try 0.01)
            self.alphaSurface.set_alpha(self.alph)  # Set the incremented alpha-value to the custom surface.
            self.screen.blit(self.alphaSurface, (0, 0))  # Blit it to the screen-surface (Make them separate)

            self.scenes = {'Start': Start()}


            if pygame.time.get_ticks() > 2500 and not self.started:
                scene = self.scenes['Start']
                scene.draw()
                self.started = True
                print('lol')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                try:
                    scene.handle_event(event)
                    scene.update()
                    scene.draw()
                except:
                    print('scene hasn\'t been made or doesn\'t have those methods')

            pygame.display.flip()



if __name__ == "__main__":
    game = Boxhead()