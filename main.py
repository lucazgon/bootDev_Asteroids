import pygame
from constants import*

# game function
def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # primary game loop

    while True:
        # check for player inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # update the game world

        # draw the game to screen
        screen.fill(BLACK)
        pygame.display.flip()

if __name__ == "__main__":
    main()