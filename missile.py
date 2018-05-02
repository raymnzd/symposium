import pygame

class Missile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((1,2))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 4
        self.rect.y = player.rect.y + 4

    def update(self):
        self.rect.x += 5
        self.rect.y += 0
