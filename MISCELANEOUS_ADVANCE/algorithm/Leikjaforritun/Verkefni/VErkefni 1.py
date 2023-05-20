import pygame
import random

pygame.init()   # we always need this

GREEN = (48, 91, 74)
BLUE = (0, 0, 255)
MAXIMUM_THROWS = 3

dice_list = list()
image_list = list()
rethrow_list = list()
dice_positions = [(200, 100), (350, 100), (120, 250), (275, 250), (425, 250)]

window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size)

image_list.append(pygame.image.load('images/sd1.png'))
image_list.append(pygame.image.load('images/sd2.png'))
image_list.append(pygame.image.load('images/sd3.png'))
image_list.append(pygame.image.load('images/sd4.png'))
image_list.append(pygame.image.load('images/sd5.png'))
image_list.append(pygame.image.load('images/sd6.png'))


class Dice:
    def __init__(self, display, position, size=(100, 100)):
        self.position = position
        self.display = display
        self.size = size
        self.width_offset = self.position[0] + self.size[0]
        self.height_offset = self.position[1] + self.size[1]
        self.dice_image = None
        self.roll()


    def show(self):
        self.display.blit(self.dice_image, self.position)


    def is_mouse_within(self, m_pos):
        if self.position[0] <= m_pos[0] <= self.width_offset and self.position[1] <= m_pos[1] <= self.height_offset:
            return True
        else:
            return False

    def select(self):
        pygame.draw.rect(self.display, BLUE, (self.position, self.size), 2)

    def roll(self):
        rand = random.randint(0, 5)
        self.dice_image = image_list[rand]


for i in range(0, 5):
    dice_list.append(Dice(window, dice_positions[i]))


window.fill(GREEN)

for die in dice_list:
    die.show()

NUM_THROWS = 1




running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            for die in dice_list:
                if die.is_mouse_within(mouse):
                    if NUM_THROWS < MAXIMUM_THROWS:
                        die.select()
                        rethrow_list.append(die)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if NUM_THROWS < MAXIMUM_THROWS:
                    if len(rethrow_list) == 0:
                        for die in dice_list:
                            die.roll()
                    else:
                        for die in rethrow_list:
                            die.roll()

                    NUM_THROWS += 1

                    rethrow_list.clear()

                    window.fill(GREEN)

                    for die in dice_list:
                        die.show()
        pygame.display.flip()

pygame.quit()


"""
import pygame
import random

pygame.init()   # we always need this

GREEN = (48, 91, 74)
BLUE = (0, 0, 255)
MAXIMUM_THROWS = 3

dice_list = list()
image_list = list()
rethrow_list = list()
dice_positions = [(200, 100), (350, 100), (120, 250), (275, 250), (425, 250)]

window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size)

image_list.append(pygame.image.load('images/sd1.png'))
image_list.append(pygame.image.load('images/sd2.png'))
image_list.append(pygame.image.load('images/sd3.png'))
image_list.append(pygame.image.load('images/sd4.png'))
image_list.append(pygame.image.load('images/sd5.png'))
image_list.append(pygame.image.load('images/sd6.png'))


class Dice:
    def __init__(self, display, position, size=(100, 100)):
        self.position = position
        self.display = display
        self.size = size
        self.width_offset = self.position[0] + self.size[0]
        self.height_offset = self.position[1] + self.size[1]
        self.dice_image = None
        self.roll()


    def show(self):
        self.display.blit(self.dice_image, self.position)


    def is_mouse_within(self, m_pos):
        if self.position[0] <= m_pos[0] <= self.width_offset and self.position[1] <= m_pos[1] <= self.height_offset:
            return True
        else:
            return False

    def select(self):
        pygame.draw.rect(self.display, BLUE, (self.position, self.size), 2)

    def roll(self):
        rand = random.randint(0, 5)
        self.dice_image = image_list[rand]


for i in range(0, 5):
    dice_list.append(Dice(window, dice_positions[i]))


window.fill(GREEN)

for die in dice_list:
    die.show()

NUM_THROWS = 1




running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            remove = False
            mouse = pygame.mouse.get_pos()
            for die in dice_list:
                if die.is_mouse_within(mouse):
                    for x in rethrow_list:
                        if remove == True:
                            break
                        elif x == die:
                            rethrow_list.remove(x)
                            remove = True
                            window.fill(GREEN)
                            for die in dice_list:
                                die.show()

                    if NUM_THROWS < MAXIMUM_THROWS and remove == False:
                        die.select()
                        rethrow_list.append(die)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if NUM_THROWS < MAXIMUM_THROWS:
                    if len(rethrow_list) == 0:
                        for die in dice_list:
                            die.roll()
                    else:
                        for die in rethrow_list:
                            die.roll()

                    NUM_THROWS += 1

                    rethrow_list.clear()

                    window.fill(GREEN)

                    for die in dice_list:
                        die.show()
        pygame.display.flip()

pygame.quit()
"""