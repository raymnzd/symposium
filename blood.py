import pygame
import random
from sprites import *


class Blood(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = bloodpic
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = random.randrange(500)
        self.rect.y = random.randrange(500)
        pygame.display.update()