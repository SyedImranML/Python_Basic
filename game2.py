
import pygame
pygame.init()

# Set the window size
size = 400, 400
screen = pygame.display.set_mode(size)

color = 255, 255, 0 # R G B
center = (200, 200)
radius = 25

pygame.draw.circle(screen, color, center, radius)

# display whatever is drawn so far
pygame.display.flip()

# wait for 3 seconds so that we can see the window
pygame.time.wait(3000)
