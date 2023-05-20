import pygame
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 255)
window_size = 640, 480
window = pygame.display.set_mode(window_size)
window.fill(BLUE)
pygame.display.set_caption('Intro to Game Programming')

#upphafsstaða
x_position = 0
y_position = 0

# upphafs hraði
x_velocity = 5
y_velocity = 2
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    window.fill(BLUE)
    pygame.draw.rect(window, RED, pygame.Rect(x_position, y_position, 20, 20))
    # ný staða fengin miðað við uppgefinn hraða
    x_position += x_velocity
    y_position += y_velocity
    # hér fyrir neðan er tékkað á hvort kassin snerti útlínur gluggans
    # ef hann gerir það þá kassanum snúið við með því að margfalda með -1
    # það þarf að draga frá særðina á kassanum til að fá þetta rétt(640-20 og 480-20)
    if y_position > 460 or y_position < 0:  # top - bottom check
        y_velocity *= -1
    if x_position > 620 or x_position < 0:  # left - right check
        x_velocity *= -1
    pygame.display.update()
    clock.tick(60)
pygame.quit()

