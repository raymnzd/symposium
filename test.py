import pygame
import time
DONE = False
screen = pygame.display.set_mode((500,500))
alphaSurface = pygame.Surface((500,500)) # The custom-surface of the size of the screen.
alphaSurface.fill((255,255,255)) # Fill it with whole white before the main-loop.
alphaSurface.set_alpha(0) # Set alpha to 0 before the main-loop.
alph = 0 # The increment-variable.
screen.fill((255,255,255))

# while not DONE:
#     # if alph < 200:
#     #     screen.fill((0,0,0)) # At each main-loop fill the whole screen with black.
#     #     alph += 1 # Increment alpha by a really small value (To make it slower, try 0.01)
#     #     alphaSurface.set_alpha(alph) # Set the incremented alpha-value to the custom surface.
#     #     screen.blit(alphaSurface,(0,0)) # Blit it to the screen-surface (Make them separate)
#     # else:
#     #     surf = pygame.draw.rect(screen, (0, 0, 255), (0, 0, 50, 50))
#     #     while surf.x < 500:
#     #         pygame.display.flip()
#     #         surf = surf.move(100,10)
#     #         print("moved")
#     #
#     for ev in pygame.event.get():
#         if ev.type == pygame.QUIT:
#             DONE = True
#     pygame.display.flip() # Flip the whole screen at each frame.
#     surf = surf.move(1,0)
#     surf = pygame.draw.rect(screen, (0,0,255), pygame.Rect(50, 50, 50, 50), 0)

x = 0
y = 0
while not DONE:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            DONE = True
    pygame.display.update()
    screen.fill((255,255,255))
    surf = pygame.draw.rect(screen, (0, 0, 255), (x, 0, 500, 500))
    time.sleep(.03)
    x += 1


quit()