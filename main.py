import pygame
from pygame.locals import *

pygame.init()
WINDOW_MODE = 800, 800
RUNNING = True
SCREEN = pygame.display.set_mode(WINDOW_MODE)

while RUNNING:
    for event in pygame.event.get():
        if event.type == QUIT:
            RUNNING = False
            break



pygame.quit()