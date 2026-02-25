import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player


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
    Player.containers = (updatable, drawable)
    player = Player(pos_x, pos_y)
    

    while True:
        # 1. Event Handling
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # 2. Update Game State
        updatable.update(dt)

        # 3. Draw / Render
        screen.fill("black")
        for ele in drawable:
            ele.draw(screen)
        pygame.display.flip()

        # 4. Tick the Clock
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
