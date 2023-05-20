#livinus felix bassey
#lokaverkefni_pygame
#20.11.2018

import pygame #hérna er að importa pygame
import random #notum við að geravið lekkja

pygame.init()#alltaf nota að byrja á þessu

#hérna er litirnir sem búa til eru byggðir úr RGB, er skilgrein að nota síðar.
colors = {
    'WHITE': (0,255,255),
    'BLUE': (0, 0, 255),
    'GREEN': (0,255,0),
    'RED': (255, 0, 0),
    'BLACK': (0, 0, 0)
}

#hérna er að nota til að stjórna hraðanum
clock = pygame.time.Clock()

#hér eru gluggann sem er lárétti ásinn og lóðrétti ásinn
display_width = 1024
display_height = 768

#hér er fasta(constants) af hvernig hraða virka leikkjum
FPS = 60

#her er aðgerð af font
font = pygame.font.SysFont("calibri", 32, bold=True)

border = {
    'LEFT': 25,
    'RIGHT': display_width - 25,
    'TOP': 0,
    'BOTTOM': display_height
}
#hér er fyrir útsýni gluggi af leik
gameDisplay = pygame.display.set_mode((display_width, display_height))

#allt hérna er að bua til gluggi
def main():

    gameover = False
    gamewin = False
    gamepause = False


    bucket_x = display_width / 2 - 50
    bucket_y = display_height - 50
    bucket_x_change = 0
    bucket_width = 100
    bucket_height = 25
    bucket_width_change = 18
    speed = 30
    balls_missed = 0
    ball_speed = 10
    score = 0
    ball_radius = 25
    rand_ball_x = random.randrange(25, display_width - 75)
    ball_y = - ball_radius
    ball_color = colors['BLUE']

    gameDisplay.fill(colors['WHITE'])#hvítur bakgrunnur

    pygame.display.set_caption('Bucket')#gluggi til að spila leik

    #hérna er loopa(game loop)fyrir leik
    running = True
    while running:
        while gameover:#loopa leik lokið
            gameDisplay.fill(colors['WHITE'])
            center_msg_to_screen("You Lost :( Do you want to play again? (y/n)", colors['RED'])
            for event in pygame.event.get():#hér allt fyrir neðan er að athugar hvort eitthvað hefur gerst leik
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:#ef ýtt er á y takkann byrja aftur leik frá hlé
                        gameover = False
                        running = True
                        bucket_x = display_width / 2 - 50
                        bucket_y = display_height - 50
                        bucket_x_change = 0
                        bucket_width = 100
                        bucket_height = 25
                        ball_speed = 10
                        score = 0
                    elif event.key == pygame.K_n:#ef ýtt er á n takkann,sleppa af leiknum
                        gameover = False
                        running = False
            pygame.display.update()
        
        while gamepause:#hér allt fyrir neðan er að athugar hvort eitthvað hefur gerst hlé á leiknum
            gameDisplay.fill(colors['WHITE'])
            center_msg_to_screen("Do you want to quit the game? (y/n)", colors['BLUE'])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:#ef ýtt er á y takkann leik byrja afram hvar fyrir en
                        running = False
                        gamepause = False
                    elif event.key == pygame.K_n or pygame.K_ESCAPE: #ef ýtt er á n takkann leik
                        gamepause = False
            pygame.display.update()

        while gamewin:#hér allt fyrir neðan er að athugar hvort eitthvað hefur gerst vinna leiknum
            gameDisplay.fill(colors['WHITE'])
            center_msg_to_screen("You Win! Do you want to play again (y/n)?", colors['GREEN'])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        gamewin = False
                        running = True
                        bucket_x = display_width / 2 - 50
                        bucket_y = display_height - 50
                        bucket_x_change = 0
                        bucket_width = 100
                        bucket_height = 25
                        ball_speed = 10
                        score = 0
                    elif event.key == pygame.K_n:
                        gamewin = False
                        running = False
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    bucket_x_change = - speed
                if event.key == pygame.K_RIGHT:
                    bucket_x_change = speed
                if event.key == pygame.K_ESCAPE:
                    gamepause = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    bucket_x_change = 0

           # hér fyrir neðan er tékkað á hvort kassin snerti útlínur gluggans ef hann gerir það þá kassanum snúið við

        if (bucket_x + bucket_x_change) < border['LEFT']:
            bucket_x = border['LEFT']
            bucket_x_change = 0

        elif (bucket_x + bucket_x_change + bucket_width) > border['RIGHT']:
            bucket_x = border['RIGHT'] - bucket_width
            bucket_x_change = 0


        if bucket_x <= (rand_ball_x + ball_radius) and (bucket_x + bucket_width) >= (rand_ball_x - ball_radius): #something wrong here?
            if bucket_y <= (ball_y + ball_radius):
                score += 1
                rand_ball_x = random.randrange(50, display_width - 50)
                ball_y = - ball_radius
                bucket_width += bucket_width_change
                bucket_x += - bucket_width_change/2
                balls_missed = 0
                ball_speed += 1

        elif ball_y > display_height:
            balls_missed += 1
            rand_ball_x = random.randrange(50, display_width - 50)
            ball_y = - ball_radius
            score += -2
            if balls_missed == 3 or score < 0:
                gameover = True


        if bucket_width >= display_width - 50:
            gamewin = True

        bucket_x += bucket_x_change
        ball_y += ball_speed

        gameDisplay.fill(colors['BLACK'])
        draw_circle(ball_color, rand_ball_x, ball_y, ball_radius)
        draw_rectangle(colors['WHITE'], bucket_x, bucket_y, bucket_width, bucket_height)
        msg_to_screen("Score: " + str(score), colors['WHITE'], 5, 10)
        pygame.display.update()


        clock.tick(FPS)
    pygame.quit()#lokar forrituni gluggi

def msg_to_screen(msg, color, x_pos, y_pos):
    text = font.render(msg, True, color)
    gameDisplay.blit(text, (x_pos, y_pos))
    # gameDisplay.blit(screen_text, [display_width/2 - screen_text.get_width()/2, display_height/2 - screen_text.get_height()/2])﻿

    #útsýn
def center_msg_to_screen(msg, color):
    text = font.render(msg, True, color)
    gameDisplay.blit(text, [display_width/2 - text.get_width()/2, display_height/2 - text.get_height()/2])

    #hér kúlurnar(boltin) sem fellur frá uppi
def draw_circle(color, x_pos, y_pos, size):
    pygame.draw.circle(gameDisplay, color, (x_pos,y_pos), size)

    #hér  kassinn sem getur valið kúlurnar(boltin) sem falla frá upp til niður
def draw_rectangle(color, x_pos, y_pos, width, height):
    pygame.draw.rect(gameDisplay, color, [x_pos,y_pos,width,height])

    #hér mouse hvrnig virka
def get_mouse_pos():
    pos = pygame.mouse.get_pos()
    return pos


if __name__ == '__main__':
    main()
