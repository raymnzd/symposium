import pygame
import random
import pygame.gfxdraw
import glob

# Define some colors
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
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """

    def __init__(self,color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        if color == RED:
            self.image = spatula
        else:
            self.image = pygame.Surface([width, height])

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
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



# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()

# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

purple_sprites_list = pygame.sprite.Group()

missile_sprites_list = pygame.sprite.Group()


for i in range(50):
    # This represents a block
    block = Block(BLACK, 20, 15)

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # circx = Missle()
    # circx.rect.x = random.randrange(screen_width)
    # circx.rect.y = random.randrange(screen_height)

    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
    purple_sprites_list.add(block)
    # missile_sprites_list.add(circx)

# Create a RED player block
player = Block(RED, 20, 15)
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            missile = Missle()
            missile.rect.x = player.rect.x
            missile.rect.y = player.rect.y
            missile_sprites_list.add(missile)




    # Clear the screen
    screen.fill(WHITE)

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()

    # Fetch the x and y out of the list,
    # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)


    missles_hit_list = pygame.sprite.groupcollide(missile_sprites_list, block_list, True, True, None)


    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print(score)

    for blockx in missile_sprites_list:
        blockx.update()



    # purple_hit_list = pygame.sprite.groupcollide(purple_sprites_list, block_list, True, True, None)
    # Draw all the spites


    all_sprites_list.draw(screen)
    purple_sprites_list.draw(screen)
    missile_sprites_list.draw(screen)

    for hits in missles_hit_list:
        list_egg.append((hits.rect.x, hits.rect.y))

    for all in list_egg:
        screen.blit(yolk, all)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()