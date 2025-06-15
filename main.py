# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from os import sys
from shot import *


def main():
    pygame.init()  # Initalize Pygame
    clock = pygame.time.Clock()

    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    game_score = 0

    Player.containers = (updateable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
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

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()
                    # asteroid.split()
                    game_score += 1

        print(game_score)
        pygame.display.flip()

        # Set the FPS to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
