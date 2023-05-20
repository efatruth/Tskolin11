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

pygame.display.set_caption('Teningakast')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255,192,203)
HOT_PINK = (255,105,180)


x_position = 0
y_position = 0
x_velocity = 5
y_velocity = 2
window.fill(PINK)
clock = pygame.time.Clock()
frames_per_second = 30
my_font = pygame.font.SysFont("", 30)
last = pygame.time.get_ticks()
relax = 30
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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    x_position += 0.1
    y_position += 0.1

    pygame.draw.rect(window, HOT_PINK, pygame.Rect(x_position, y_position, 60, 60))
    label = my_font.render('trixie', 1, BLUE)
    window.blit(label, (53, 53))
    now = pygame.time.get_ticks()
    if now - last >= relax:
        x_position += 2
        last = now
    # This is the section of the program in which the game state is changed
    # and then finally the screen(game screen) is updated.
    # However in this demo not very much is going on
    # so a screen update is not necessary :-)
    #x_position += x_velocity
    #y_position += y_velocity
    #if y_position > 460 or y_position < 0:
     #   y_velocity *= -1
    #if x_position > 620 or x_position < 0:
     #   x_velocity *= -1
    pygame.display.update()
    clock.tick(60)

pygame.quit() # When the game loop is no longer running this causes the program to quit.