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

red_x_position = 0
blue_x_position = 0

window.fill(WHITE)

blue_last = red_last = pygame.time.get_ticks()
red_relax = 10
blue_relax = 30

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = pygame.time.get_ticks()

    if now - red_last >= red_relax:
        red_x_position += 2
        red_last = now
    if now - blue_last >= blue_relax:
        blue_x_position += 2
        blue_last = now

    pygame.draw.rect(window, RED, pygame.Rect(red_x_position, 50, 60, 60))
    pygame.draw.rect(window, BLUE, pygame.Rect(blue_x_position, 190, 60, 60))
    pygame.display.update()

    window.fill(WHITE)

pygame.quit()
