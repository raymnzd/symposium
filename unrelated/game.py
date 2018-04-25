import pygame
import time
import math
import glob

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surface_sz = 480   # Desired physical surface size, in pixels.
    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))
    yolk = pygame.image.load("yolk.png")
    yolk = pygame.transform.scale(yolk, (50,30))
    rect = yolk.get_rect()

    u = 0
    y = 0

    my_font = pygame.font.SysFont("Courier", 16)
    the_text = my_font.render("Hello, world!", True, (0, 0, 0))

    # Set up some data to describe a small rectangle and its color
    small_rect = (300, 200, 150, 90)
    some_color = (0, 100, 100)        # A color is a mix of (Red, Green, Blue)



    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break  # ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((0, 200, 255))

        # Overpaint a smaller rectangle on the main surface
        main_surface.fill(some_color)

        main_surface.blit(yolk, rect)
        main_surface.blit(the_text, (10, 10))
        circ = pygame.draw.circle(main_surface, (50, 0, 50), (200, 200), 30, 0)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

        if rect.x == 240:
            u = -2
            y = -2
        if rect.x == 0:
            u = 2
            y = 2
        rect = rect.move(u,y)
        time.sleep(.05)


    pygame.quit()     # Once we leave the loop, close the window.

class Egg(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = "images/yolk.png"
egg = Egg()
main()


