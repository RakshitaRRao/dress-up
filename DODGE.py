import pygame
import time
import random

width ,  height = 612 , 302
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("DODGE")

bg = pygame.transform.scale(pygame.image.load("bg.jpg"), (width,height))


def draw():
    win.blit(bg , (0,0))
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw()
    pygame.quit()

if __name__ == "__main__" :
    main()