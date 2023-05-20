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

# From the previous examples(05 and 08) we have x and y positions
x_position = 0
y_position = 0

# Now we will add velocity as two variables representing movement in the two directions; x and y
# You will not be surprised by the fact these are the only dimensions we can use to move around in
# a 2D system and in such a system, movement can always be broken down into horizontal and vertical
# components, in this case x and y
# We will start with a equal velocity in both directions.
x_velocity = 3
y_velocity = 1

window.fill(GREEN)

# Lest control the frames per second in this program.
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BLUE)
    pygame.draw.rect(window, RED, pygame.Rect(x_position, y_position, 60, 60))

    # Now the position is calculated with respect to the velocity that is kept in the two
    # velocity variables(x_velocity and y_velocity).
    # What this means in terms of speed is that it is controlled by the values in these
    # velocity variables => the higher the value of each variable, the faster the speed
    # in that respective direction.
    x_position += x_velocity
    y_position += y_velocity

    pygame.display.update()
    clock.tick(60)
pygame.quit()
