import pygame
from movemap import move_map
import random

class Missile(pygame.sprite.Sprite):

    def __init__(self, player, user):
        super().__init__()
        self.user = user
        if self.user == "player":
            self.user = "player"
            self.image = pygame.Surface((5,2))
            self.image.fill((0,0,255))
            self.rect = self.image.get_rect()
            self.rect.x = player.rect.x + 8
            self.rect.y = player.rect.y + 8
            self.target = "enemy"
        else:
            self.image = pygame.Surface((3,3))
            self.image.fill((255,0,0))
            self.rect = self.image.get_rect()
            self.rect.x = user.rect.x + 4
            self.rect.y = user.rect.y + 4
            self.targx = player.rect.x
            self.targy = player.rect.y
            self.target = "player"

        self.dir = player.dir
        self.randx = random.randint(0,1)
        self.randy = random.randint(0,1)

    def update(self):

        if self.user == "player":
            self.rect.x += move_map[self.dir][0] * 4
            self.rect.y += move_map[self.dir][1] * 4
        else:
            self.rect.x += move_map[self.dir][self.randx] * 2
            self.rect.y += move_map[self.dir][self.randy] * 2



