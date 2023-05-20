import pygame
'''
    The program imports the PyGame library.
    The only other thing it does is to open a 640X480 window with a black background.
    It however demonstrates a program structure that is important in the development
    of games.
    Good stuff on PyGame basics:  http://www.nerdparadise.com/tech/python/pygame/basics/
'''
pygame.init()   # we always need this

window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size)

running = True  # loop control variable(for the game loop)

# This is the game loop. At present it contains  a so called event loop
# that is responsible for "catching" every event belonging to
# the program.
# It is of course up to the programmer/designer to respond to these events.
# Here the event loop "listens" for the user quitting the program by clicking
# the top right corner(the X)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # This is the section of the program in which the game state is changed
    # and then finally the screen(game screen) is updated.
    # However in this demo not very much is going on
    # so a screen update is not necessary :-)

pygame.quit() # When the game loop is no longer running this causes the program to quit.