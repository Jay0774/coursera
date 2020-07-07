# createing a small illustration of pong game.

import pygame,sys,os
from pygame.locals import * # importing all files

red=[255,0,0]

catx = 10
caty = 10
screen = 0

# defining the quit function

def myquit():
    pygame.quit()
    sys.exit(0)
    
# defining the check input function

def check_input(events):
    global catx,caty,screen
    for event in events:
        if event.type == QUIT:
            quit()
        else:
            if event.type == KeyDown:
                if event.type == K_ESCAPE:
                    myquit()
                elif event.type == 276:
                    catx -= 5
                    print("MOVE RECT LEFT")
                elif event.type == 275:
                    catx+=5
                    print("MOVE RECT RIGHT")
                else:
                    print(event.key)
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),(catx,50,50,10))
    pygame.display.update()
    
# defining main function

def main():
    global screen
    pygame.init()
    # set up window

    window = pygame.display.set_mode((400,600))
    pygame.display.set_caption('Slither.eat - The Snake Game')

    # set up drawing surface
    screen = pygame.display.get_surface()
    pygame.display.update()
    
    while True:
        check_input(pygame.event.get())
        
main()

    
