import pygame
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import*
import sys

# game function
def main():

    pygame.init()
    gameClock = pygame.time.Clock()
    dt = 0
    # set up groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots,updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    myPlayer = Player( x =SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    myAsteroidField = AsteroidField()
    
    # primary game loop
    while True:
        '''
        Should accomplish 3 main things:
            - check for inputs
            - update the game world
            - draw the game to the screen
        '''

        # check for player inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # update the game world
        for obj in updatable:
            obj.update(dt)
            # iterate over all of the objects in your asteroids group. Check if any of them collide with the player.
        for asteroid in asteroids:
            if asteroid.detect_collision(myPlayer) == True:
                print("GAME OVER")
                sys.exit()

        # draw the game to screen
        screen.fill(BLACK)
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        # calc delta time
        dt = gameClock.tick(60) / 1000

if __name__ == "__main__":
    main()