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

# lets add a y-position of the rectangle in  new  variable and initialize to 0
x_position = 0
y_position = 0

window.fill(BLUE)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Each time the game loop runs the value in both position variables is increased.
    # This now  "moves" the red rect to the right and down at the same time.
    x_position += 0.1
    y_position += 0.1

    pygame.draw.rect(window, RED, pygame.Rect(x_position, y_position, 60, 60))
    pygame.display.update()

    window.fill(BLUE)

pygame.quit()