from constants import *
import pygame

from player import Player


def main():
    pygame.init()
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # player.update(dt)
        updatable.update(dt)
        screen.fill("black")

        # player.draw(screen)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit game to 60 FPS
        amount_time_passed = clock.tick(60)
        dt = amount_time_passed / 1000


if __name__ == "__main__":
    main()
