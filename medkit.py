import pygame
from sprites import *
import math
import random


class MedKit(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = medpic
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20,450)
        self.rect.y = random.randint(20,450)
