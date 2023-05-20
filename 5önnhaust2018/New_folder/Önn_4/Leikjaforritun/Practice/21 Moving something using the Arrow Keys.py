# coding=UTF-8
import pygame

pygame.init()

window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size)

pygame.display.set_caption('Move the box in 2D')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# upphafsstaÃ°a rauÃ°a kassans er Ã¡ miÃ°jum skjÃ¡num
x_position = 310
y_position = 230

# upphafshraÃ°inn er nÃºll Ã­ bÃ¡Ã°ar Ã¡ttir(kassinn er kjurr)
x_velocity = 0
y_velocity = 0

window.fill(BLUE)

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # ef einhver takki Ã¡ lyklaborÃ°inu fer niÃ°ur Ã¾Ã¡ Ã¾arf aÃ° tÃ©kka
        # Ã¡ Ã¾vÃ­ hvaÃ°a takki Ã¾aÃ° er. Ã Ã¾essu demÃ³i erum viÃ° bara aÃ°
        # vinna meÃ° Ã¶rvartakkana.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # playerinn Ã½tti Ã¡ vinstri Ã¶rina og viÃ° setjum hraÃ°ann Ã¡ 2 Ã­ mÃ­nus(til vinstri)
                x_velocity = -2
            elif event.key == pygame.K_RIGHT:
                x_velocity = 2
            elif event.key == pygame.K_UP:
                y_velocity = -2
            elif event.key == pygame.K_DOWN:
                y_velocity = 2
        # ef playerinn sleppir takkanum Ã¾Ã¡ er hreyfingin stoppuÃ° Ã­ x og y Ã¡tt.
        # hÃ©r mÃ¡ bÃ¦ta viÃ° ef einungis Ã¡ aÃ° stoppa Ã­ Ã¾Ã¡ Ã¡tt sem sleppti takkinn
        # sÃ½nir.
        # ALTSVO: ef Ã©g er aÃ° fara upp til hÃ¦gri og sleppi hÃ¦gri Ã¶rinni en held
        #         hinni niÃ°ri Ã¾Ã¡ er einungis hraÃ°inn til hÃ¦gti settur Ã¡ 0, ekki bÃ¡Ã°ar Ã¡ttir
        elif event.type == pygame.KEYUP:
            x_velocity = 0
            y_velocity = 0

    # staÃ°an Ã¡ rauÃ°a kassanum uppfÃ¦rÃ° miÃ°aÃ° viÃ° hraÃ°an(current speed)
    x_position += x_velocity
    y_position += y_velocity

    window.fill(BLUE)
    pygame.draw.rect(window, RED, pygame.Rect(x_position, y_position, 20, 20))

    # ef kasinn okkar er kominn aÃ° brÃºnum sjÃ¡sins Ã¾Ã¡ er hreyfing stÃ¶Ã°vuÃ°
    # i Ã¾Ã¡ Ã¡tt sem kassinn er aÃ° fara Ã¾egar hann rekst Ã¡ skjÃ¡brÃºnina
    if y_position > 460 or y_position < 0:
        y_velocity = 0
    if x_position > 620 or x_position < 0:
        x_velocity = 0

    pygame.display.update()
    clock.tick(60)
pygame.quit()