import pygame
from player import Player
from constants import*

# game function
def main():

    pygame.init()
    gameClock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    myPlayer = Player( x =SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
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
            myPlayer.update(dt)
        # update the game world

        # draw the game to screen
        screen.fill(BLACK)
        myPlayer.draw(screen)
        pygame.display.flip()

        # calc delta time
        dt = gameClock.tick(60) / 1000

if __name__ == "__main__":
    main()