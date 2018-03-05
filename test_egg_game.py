import pygame
import random
import pygame.gfxdraw
import glob

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

yolk = pygame.image.load(glob.glob("images/yolk.png")[0])
yolk = pygame.transform.scale(yolk, (50,30))

egg = pygame.image.load(glob.glob("images/egg.png")[0])
egg = pygame.transform.scale(egg, (50,30))

spatula = pygame.image.load(glob.glob("images/spatula.png")[0])
spatula = pygame.transform.scale(spatula, (50,30))
spatula = pygame.transform.flip(spatula, False, True)

list_egg = []

class Block(pygame.sprite.Sprite):


    def __init__(self,color, width, height):

        super().__init__()

        if color == RED:
            self.image = spatula
        else:
            self.image = pygame.Surface([width, height])


        self.rect = self.image.get_rect()
        self.blink = True

    def change_color(self):
        if self.blink:
            self.image.fill(BLACK)
            self.blink = False
        else:
            self.image.fill(RED)
            self.blink = True

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def set_image(self, img):
        self.image = img






class Missle(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = egg
        self.rect = self.image.get_rect(center=(150, 200))

    def update(self):
        self.rect.x += 1

    def set_image(self, img):
        self.image = img

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)



pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])


block_list = pygame.sprite.Group()


all_sprites_list = pygame.sprite.Group()

purple_sprites_list = pygame.sprite.Group()

missile_sprites_list = pygame.sprite.Group()


for i in range(50):
    block = Block(BLACK, 20, 15)

    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)


    block_list.add(block)
    all_sprites_list.add(block)
    purple_sprites_list.add(block)

player = Block(RED, 20, 15)
all_sprites_list.add(player)

done = False

clock = pygame.time.Clock()

score = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            missile = Missle()
            missile.rect.x = player.rect.x
            missile.rect.y = player.rect.y
            missile_sprites_list.add(missile)




    screen.fill(WHITE)


    pos = pygame.mouse.get_pos()


    player.rect.x = pos[0]
    player.rect.y = pos[1]

    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)


    missles_hit_list = pygame.sprite.groupcollide(missile_sprites_list, block_list, True, True, None)


    for block in blocks_hit_list:
        score += 1
        print(score)

    for blockx in missile_sprites_list:
        blockx.update()





    all_sprites_list.draw(screen)
    purple_sprites_list.draw(screen)
    missile_sprites_list.draw(screen)

    for hits in missles_hit_list:
        list_egg.append((hits.rect.x, hits.rect.y))

    for all in list_egg:
        screen.blit(yolk, all)

    pygame.display.flip()


    clock.tick(60)

pygame.quit()