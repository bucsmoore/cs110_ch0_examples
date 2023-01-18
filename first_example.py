# The below code fills the screen with 3 colors of your choosing. 
# After each color, it waits 1000 milliseconds before continuing.
import pygame
pygame.init()
screen = pygame.display.set_mode()
color = [255, 0, 0]
screen.fill(color)
pygame.display.flip()
pygame.time.wait(1000)
color = [0, 255, 0]
screen.fill(color)
pygame.display.flip()
pygame.time.wait(1000)
color = [255, 0, 255]
screen.fill(color)
pygame.display.flip()
