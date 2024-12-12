import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 640
screen=pygame.display.set_mode((width, height))

# 3 - Load images
background = pygame.image.load("assets/bgs/bg.jpg")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(background, (0,0))
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                background = pygame.image.load("bg_start.jpg")
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)