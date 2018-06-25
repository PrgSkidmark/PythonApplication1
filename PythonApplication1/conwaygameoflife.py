# import the pygame module, so you can use it
import pygame
import random
import math
from collections import namedtuple
from pygame import gfxdraw

def drawboard(surface, screen_width, screen_height):
    rowcount = 100
    colcount = 100

    mingridsize = min(screen_width/colcount, screen_height/rowcount)
    row_number = 1
    for row_number in range(rowcount):
        left = 0
        down = row_number*mingridsize
        pygame.draw.line(surface, (100,100,100), (left,down), (screen_width, down), 1)

    col_number = 1
    for col_number in range(colcount):
        left = col_number*mingridsize
        top = 0
        pygame.draw.line(surface, (100,100,100), (left,top), (left,screen_height), 1)

def drawpattern(surface, screen_width, screen_height, pattern):
    rowcount = 100
    colcount = 100

    mingridsize = min(screen_width/colcount, screen_height/rowcount)
    row_number = 1
    for row_number in range(len(pattern)):
        down = row_number*mingridsize
        col_number = 1
        for col_number in range(len(pattern[row_number-1])):
            left = col_number*mingridsize
            top = 0
            if (pattern[row_number-1][col_number-1] == 1):
                rect = pygame.Rect(left+1, down+1, mingridsize-2, mingridsize-2)
                pygame.draw.rect(surface, (100,100,100), rect, 0)

def createnextpattern(pattern):
    newpattern = []
    row_number = 1
    for row_number in range(len(pattern)):
        newpattern.append(pattern[row_number-1].copy())
        #col_number = 1
        #newrow = []
        #for col_number in range(len(pattern[row_number-1])):
        #    newrow.pu
        #    newpattern[row_number-1][col_number-1] = pattern[row_number-1][col_number-1]

    row_number = 2
    for row_number in range(len(pattern)):
        col_number = 2
        for col_number in range(len(pattern[row_number-1])):
            #Fewer than 2 live neighbors, Underpopulation
            if (pattern[row_number-1][col_number-1] ==1):
                neighbortotal = pattern[row_number-2][col_number-2]+pattern[row_number-2][col_number-1]+pattern[row_number-2][col_number]+pattern[row_number-1][col_number]+pattern[row_number][col_number]+pattern[row_number][col_number-1]+pattern[row_number][col_number-2]+pattern[row_number-1][col_number-2]
                if (neighbortotal < 2):
                    newpattern[row_number-1][col_number-1] = 0
            #Has 2 or 3 live neighbors, Still Lives
            if (pattern[row_number-1][col_number-1] == 1):
                neighbortotal = pattern[row_number-2][col_number-2]+pattern[row_number-2][col_number-1]+pattern[row_number-2][col_number]+pattern[row_number-1][col_number]+pattern[row_number][col_number]+pattern[row_number][col_number-1]+pattern[row_number][col_number-2]+pattern[row_number-1][col_number-2]
                if (neighbortotal == 2) or (neighbortotal == 3):
                    newpattern[row_number-1][col_number-1] = 1
            #More than 3 live neighbors, overpopulation
            if (pattern[row_number-1][col_number-1] ==1):
                neighbortotal = pattern[row_number-2][col_number-2]+pattern[row_number-2][col_number-1]+pattern[row_number-2][col_number]+pattern[row_number-1][col_number]+pattern[row_number][col_number]+pattern[row_number][col_number-1]+pattern[row_number][col_number-2]+pattern[row_number-1][col_number-2]
                if (neighbortotal > 3):
                    newpattern[row_number-1][col_number-1] = 0
            #Dead with exactly 3 live neighbors, reproduction
            if (pattern[row_number-1][col_number-1] ==0):
                neighbortotal = pattern[row_number-2][col_number-2]+pattern[row_number-2][col_number-1]+pattern[row_number-2][col_number]+pattern[row_number-1][col_number]+pattern[row_number][col_number]+pattern[row_number][col_number-1]+pattern[row_number][col_number-2]+pattern[row_number-1][col_number-2]
                if (neighbortotal == 3):
                    newpattern[row_number-1][col_number-1] = 1
    return newpattern

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    screen_width = 1500
    screen_height = 800
    particle_count = 10
    particle_maxdistancefromother = 100
    particle_anomolycount = 1
    #bg_image = pygame.image.load("spacee-740x463.jpg")

    # create a surface on screen that has the size of screen_width x screen_height
    screen = pygame.display.set_mode((screen_width,screen_height))

    seedpattern = [[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]]
    currentpattern = seedpattern
    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
    fps = 10
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop1
                running = False
        clock.tick(fps)

        #screen.blit(bg_image, (0, 0))
        screen.fill((0,0,0))
        #myparticle_connector.update()
        drawboard(screen, screen_width, screen_height)
        drawpattern(screen, screen_width, screen_height, currentpattern)
        currentpattern = createnextpattern(currentpattern)
        # draw anim
        #dirty_rect = screen.blit(100, 240)
        # update screen
        #pygame.display.update(dirty_rect)
        pygame.display.flip()

     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()