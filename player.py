from sprites import *
from movemap import move_map
import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = player_down_pic
        self.rect = self.image.get_rect()
        self.rect.x = 240
        self.rect.y = 220
        self.speed = 3
        self.health = 100
        self.dir = 's'

    def move(self, dir):

        if self.rect.x + move_map[dir][0] * self.speed > 480 or self.rect.x + move_map[dir][0] * self.speed < 0:
            pass
        else:
            self.rect.x += move_map[dir][0] * self.speed
        if self.rect.y + move_map[dir][1] * self.speed < 0 or self.rect.y + move_map[dir][1] * self.speed > 480:
            pass
        else:
            self.rect.y += move_map[dir][1] * self.speed

    def draw_health(self,screen):
        r = min(255, 255 - (255 * ((self.health - (100 - self.health)) / 100)))
        g = min(255, 255 * (self.health / (100 / 2)))
        color = (r, g, 0)
        width = int(500 * self.health / 100)
        self.health_bar = (0, 490, width, 10)
        if self.health <= 100 and self.health >= 5:
            pygame.draw.rect(screen,color, self.health_bar)

    def get_hit(self):
        self.health -= 5

    def get_health(self):
        return self.health