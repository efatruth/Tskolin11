import pygame
'''
    Does pretty much tha same as 01_Basics.py.
    Has some more code and a LOT less comments.
'''
pygame.init()
window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)  # the screen is now resizable

pygame.display.set_caption('FOR3G3U')   # The window has a caption

running = True

# In the game loop we now also listen if the user hits the Esc button.
# Should that be the case the program quits.
# Need more info on events supported in PyGame:
# Read this: http://www.pygame.org/docs/ref/event.html
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

pygame.quit()