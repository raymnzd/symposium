#might be my start screen

import pygame
import random
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'
clock = pygame.time.Clock()

pygame.init()
screen_width = 500
screen_height = 500

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode([screen_width, screen_height])
my_font = pygame.font.SysFont("kalinga", 16)
the_text = my_font.render("Created by Raymond Zhao", True, (0, 0, 0))
text_rect = the_text.get_rect()

boxpic = pygame.image.load(("images/boxhead.png"))
bloodpic = pygame.image.load(('images/blood.png'))
bloodpic = pygame.transform.scale(bloodpic, (50,50))


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
for i in range(5):
    blood = Blood()
    blood.rect.x = random.randrange(screen_width)
    random.randrange(screen_height)
    blood_sprites.add(blood)
    pygame.display.flip()


class Start():

    def __init__(self):
        screen.fill(WHITE)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            print("u clicked")

    def draw(self):
        screen.fill(WHITE)
        screen.blit(the_text, (0,480))
        screen.blit(boxpic, (100,50))
        for blood in blood_sprites:
            blood.update()


    def update(self):
        pass




scenes = {'Start': Start()}
scene = scenes['Start']

def Boxhead():
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            scene.handle_event(event)
            scene.update()
            scene.draw()
        pygame.display.flip()


if __name__ == "__main__":
    Boxhead()
