import pygame
import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    pos_x = SCREEN_WIDTH / 2
    pos_y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(pos_x, pos_y)


    while True:
        # 1. Event Handling
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # 2. Update Game State
        updatable.update(dt)
        for ele in asteroids:
            if ele.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(ele):
                    log_event("asteroid_shot")
                    shot.kill()
                    ele.kill()

        # 3. Draw / Render
        screen.fill("black")
        for ele in drawable:
            ele.draw(screen)
        pygame.display.flip()

        # 4. Tick the Clock
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
