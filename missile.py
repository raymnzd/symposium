import pygame
from movemap import move_map

class Missile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((1,2))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 4
        self.rect.y = player.rect.y + 4
        self.dir = player.dir

    def update(self):
        self.rect.x += move_map[self.dir][0] * 5
        self.rect.y += move_map[self.dir][1] * 5




