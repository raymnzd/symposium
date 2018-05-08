import pygame
from sprites import *
import math


class Zombie(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = zombie_down_pic
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.speed = 1
        self.changex = 0
        self.changey = 0

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
        self.change_pic(player)

    def change_pic(self, player):
        if self.changex == 1:
            if self.changey == 1:
                if abs(self.rect.x - player.rect.x) <= 5:
                    self.image = zombie_down_pic
                else:
                    self.image = zombie_downright_pic
            else:
                if self.changey == -1:
                    if abs(player.rect.y - self.rect.y) > 50:
                        self.image = zombie_upright_pic
                    else:
                        self.image = zombie_right_pic
        elif self.changex == -1:
            if self.changey == 1:
                if abs(self.rect.x - player.rect.x) <= 5:
                    self.image = zombie_down_pic
                else:
                    self.image = zombie_downleft_pic
            else:
                if self.changey == -1:
                    if abs(player.rect.x - self.rect.x) <= 5:
                        self.image = zombie_up_pic
                    else:
                        if abs(player.rect.y - self.rect.y) > 50:
                            self.image = zombie_upleft_pic
                        else:
                            self.image = zombie_left_pic