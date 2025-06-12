# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    pygame.init() # Initalize Pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get(): # Exit button
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen,(0,0,0)) # Black screen
        pygame.display.flip() # Updates the screen or something














if __name__ == "__main__":
    main()