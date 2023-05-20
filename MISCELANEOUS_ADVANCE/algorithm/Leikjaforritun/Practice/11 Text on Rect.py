import pygame

pygame.init()

window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)

pygame.display.set_caption('X\'s on rectangles in a row')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (70, 80, 90)
YELLOW = (255, 255, 0)

window.fill(WHITE)

# font for "drawing" a text on the screen put in the my_font variable
my_font = pygame.font.SysFont("", 30)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw a red rectangle
    pygame.draw.rect(window, RED, pygame.Rect(30, 30, 60, 60))

    # the text is rendered and put in the variable label
    label = my_font.render('X', 1, YELLOW)
    # and then drawn on the screen and positioned within the red rectangle
    window.blit(label, (53, 53))

    # the display is updated so the the user can see the any changes that
    # have occurred since the last round of the loop
    pygame.display.update()
pygame.quit()