import pygame
from game import *
from premades import *

def locateCell(pos):
    x, y = pos
    x = x * 4 + 320
    y = y * 4 + 240
    return x,y

# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Conway's Game of Life")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((640, 480))

    game = Game()
    addBlinker(game, (0,0))
    addToad(game, (10,3))
    addGlider(game, (-80,-60))

    game.updateNeighborCounts()

    black = pygame.Color(0, 0, 0)

    clock = pygame.time.Clock()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        screen.fill(black)

        game.draw(screen, offset = (320, 240))

        pygame.display.flip()

        game.nextCycle()

        clock.tick_busy_loop(15)

        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()