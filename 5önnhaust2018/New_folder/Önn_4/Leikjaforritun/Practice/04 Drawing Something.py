import pygame

pygame.init()

window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)

pygame.display.set_caption('FOR3G3U')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

window.fill(WHITE)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Now it's time to actually draw something.
    # Let's go crazy and draw a red rectangle :-)

    #the draw.rect() functions takes some parameters.
    # the first one is the surface the function is intended to draw on.
    # In this case it is the window itself(Yes the one we filled with WHITE in line 15)
    # The second is the color of the rectangle. We use the RED constant we declared in line 11
    # The last one here is a rectangle- object.  The first two parameters to the constructor are
    # x-position and y-position.  The last two are the width and height of the rectangle.
    # NOTE: This rectangle is painted on the screen once in every loop round.
    pygame.draw.rect(window, RED, pygame.Rect(30, 30, 60, 60))

    # Want to learn more on the draw() function:
    # Read this: http://www.pygame.org/docs/ref/draw.html

    # Now the display.update() has become very important
    pygame.display.update()

pygame.quit()