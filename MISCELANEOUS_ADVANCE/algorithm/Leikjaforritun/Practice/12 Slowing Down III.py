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

# we now use a function of the pygame library(get_ticks) # that counts the ticks
# since the pygame.init() was called.
# The idea is to be able to make some sort of an individual speed control
# that does not rely on slowing everything down with the clock.tick() or sleep() functions.
# This idea is implemented by getting the tick count once before we enter the loop
# and put it in a variable. We will then update this variable constantly from within the loop.
# The next thing is to figure out how long we will slow down.  To do this we need to figure out
# for how many ticks we want to "wait" and put it in a variable(here: relax).  All of this is done
# pre- loop(before we enter the game loop)
# NOTE: The lower the value stored in the relax the greater the speed.
last = pygame.time.get_ticks()
relax = 30

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # The "trick" in this slowing down is to find out how many ticks
    # have been counted since the last round of the loop and put in in a variable(named: now)
    # then we need to see if the difference between now and last is equal to or more than
    # our pre defined slow down value(stored in the relax variable).
    # Only if that is so do we update the x-position of the red rectangle.
    # We then finish the round by updating the last variable with the number of ticks
    # stored in the now variable before it will be updated in the next round.
    now = pygame.time.get_ticks()
    if now - last >= relax:
        x_position += 2
        last = now

    pygame.draw.rect(window, RED, pygame.Rect(x_position, 190, 60, 60))
    pygame.display.update()

    window.fill(WHITE)

pygame.quit()
