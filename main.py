# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import * 
from player import Player
from circleshape import CircleShape


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    while True:
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000  # seconds
        #display fps in title bar
        pygame.display.set_caption(f"FPS: {clock.get_fps():.2f}")


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    pygame.quit()

if __name__ == "__main__":
    main()
