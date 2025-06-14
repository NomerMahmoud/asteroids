# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from os import sys


def main():
    pygame.init()  # Initalize Pygame
    clock = pygame.time.Clock()

    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():  # Exit button
            if event.type == pygame.QUIT:
                return

        screen.fill((10, 50, 90))
        updateable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for obj in asteroids:
            if obj.collision(player):
                print("Game over!")
                sys.exit()

        pygame.display.flip()

        # Set the FPS to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
