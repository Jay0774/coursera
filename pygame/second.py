# adding the close button functionality


import pygame,sys,os
from pygame.locals import * # importing all files

red=[255,0,0]

# initializing pygame

pygame.init()

# set up window

window = pygame.display.set_mode((400,600))
pygame.display.set_caption('Slither.eat - The Snake Game')

# set up drawing surface
screen = pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption("Snake")
pygame.display.flip()

while True:
    for event in pygame.event.get():
        print(event)
        if(event.type==QUIT):
            pygame.quit()
            sys.exit()
    pygame.display.update()        

 
