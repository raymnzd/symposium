import pygame
from sprites import *
import math


class Devil(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = devil_down_pic
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.speed = 1
        self.changex = 0
        self.changey = 0

        self.last_shot = 0


    def update(self):
        self.rect = self.rect.move(1,1)

    def move_towards_player(self, player):
        # Movement along x direction

        if self.rect.x > player.rect.x:
            self.rect.x -= self.speed
            self.changex = -1
        elif self.rect.x < player.rect.x:
            self.rect.x += self.speed
            self.changex = 1
        # Movement along y direction
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
            self.changey = 1
        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed
            self.changey = -1
        self.change_pic()

    def change_pic(self):
        if self.changex == 1:
            if self.changey == 1:
                self.image = devil_downright_pic
            elif self.changey == -1:
                self.image = devil_upright_pic
            else:
                self.image = devil_right_pic
        elif self.changex == -1:
            if self.changey == 1:
                self.image = devil_downleft_pic
            elif self.changey == -1:
                self.image = devil_upleft_pic
            else:
                self.image = devil_left_pic