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

# lets put the x-position of the rectangle in a variable.
x_position = 0

window.fill(WHITE)

# Sometimes programs run too fast for a graphical component
# to have any real meaning.
# In order to fix this one method is to "slow down the clock".
# PyGame includes a Clock class in its time library and within
# that class is the method tick().
# By manipulating the frames that are displayed per second we can slow things down
clock = pygame.time.Clock()
frames_per_second = 20

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x_position += 2

    pygame.draw.rect(window, RED, pygame.Rect(x_position, 190, 60, 60))
    pygame.display.update()

    # Try to comment this out and see what happens :-)
    window.fill(WHITE)

    # calling the clock.tick() method. The value we set in line 27 will be used.
    clock.tick(frames_per_second)

pygame.quit()
