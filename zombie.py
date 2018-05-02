import pygame
from sprites import *
import math


class Zombie(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = zombie_up_pic
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.speed = 1

    def update(self):
        self.rect = self.rect.move(1,1)

    def move_towards_player(self, player):
        # Movement along x direction
        if self.rect.x > player.rect.x:
            self.rect.x -= self.speed
        elif self.rect.x < player.rect.x:
            self.rect.x += self.speed
        # Movement along y direction
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed