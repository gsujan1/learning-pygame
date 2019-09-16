import pygame
import time
import random

# first thing to initialize all necessary pygame libraries
pygame.init()
# sets display resolution as a TUPLE ()
WIDTH = 800
HEIGHT = 600
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
# sets window title
pygame.display.set_caption('Racey Car')
# FPS counter kinda
clock = pygame.time.Clock()
# load car image
carImg = pygame.image.load('car.png')
car_width = 32
car_height = 64
# some basic colors
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)

def obstacles(x_pos, y_pos, obsh, obsw, color):
    pygame.draw.rect(gameDisplay, color, [x_pos, y_pos, obsh, obsw])

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 110)
    textSurf, textRect = text_objects(text, largeText)
    textRect.center = ((WIDTH/2), (HEIGHT/2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    time.sleep(2)

    game_loop()

def crash():
    message_display('You Crashed!')

def game_loop():
    x = 380
    y = 500
    x_change = 0
    y_change = 0

    obs_startx = random.randrange(0, WIDTH)
    obs_starty = -400
    obs_speed = 5
    obs_width = 100
    obs_height = 100

    # game loop variable initialize
    gameExit = False
    while not gameExit:
        for event in pygame.event.get(): # list of events per frame per second
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
            # Checks to see if any keys are held down and remembers them with the variable keys.
            keys = pygame.key.get_pressed()

            # If the palyer is holding down one key or the other the car moves in that direction
            if keys[pygame.K_LEFT]:
                x_change = -5
            if keys[pygame.K_RIGHT]:
                x_change = 5

            # If the player is holding down both or neither of the keys the car stops
            if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
                x_change = 0
            if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                x_change = 0
            # print(event) prints out every event pygame registers
        x += x_change
        y += y_change
        gameDisplay.fill(white)

        # obstacles(x_pos, y_pos, obsh, obsw, color)
        obstacles(obs_startx, obs_starty, obs_height, obs_width, red)
        obs_starty += obs_speed

        car(x,y)

        if x < 0 or x > (WIDTH - car_width):
            crash()

        if obs_starty > HEIGHT:
            obs_starty = 0 - obs_width
            obs_startx = random.randrange(0, WIDTH)

        # if y < obs_starty + obs_height:
        #     if x + car_width > obs_startx and x < obs_startx + obs_width:
        #         print('x crossover')
        #         crash()

        # if x in range(obs_startx - car_width, obs_startx + obs_width):
        #     if y in range(obs_starty - car_height, obs_starty + obs_height):
        #         crash()
        if y < obs_starty + obs_height:
            # print('y crossover')
            if x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x + car_width < obs_startx+obs_width:
                # print('x crossover')
                crash()

        pygame.display.update() # update takes block of screen as parameter for speeeeeed

        clock.tick(100)

game_loop()
pygame.quit()
quit()
