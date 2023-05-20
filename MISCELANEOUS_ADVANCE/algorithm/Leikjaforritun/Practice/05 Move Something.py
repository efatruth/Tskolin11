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

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Each time the game loop runs the value in the x_position variable is increased.
    # This "moves" the red rect to the right.
    x_position += 2

    pygame.draw.rect(window, RED, pygame.Rect(x_position, 190, 60, 60))
    pygame.display.update()

    # Try to comment this out and see what happens :-)
    window.fill(WHITE)

pygame.quit()
