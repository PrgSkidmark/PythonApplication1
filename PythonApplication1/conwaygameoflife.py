# import the pygame module, so you can use it
import pygame
import random
import math
import copy
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
    rowcount = 122
    colcount = 122

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

    row_number = 0
    row_count = len(pattern)
    for row_number in range(row_count):
        newrow = []
        col_number = 0
        col_count = len(pattern[row_number])
        for col_number in range(col_count):
            value = copy.deepcopy(pattern[row_number][col_number])
            NW = 0
            if (row_number > 0) and (col_number > 0):
                NW = pattern[row_number-1][col_number-1]
            N = 0
            if (row_number > 0):
                N = pattern[row_number-1][col_number]
            NE = 0
            if (row_number > 0) and (col_number < col_count-1):
                NE = pattern[row_number-1][col_number+1]
            E = 0
            if (col_number < col_count-1):
                E = pattern[row_number][col_number+1]
            SE = 0
            if (row_number < row_count-1) and (col_number < col_count-1):
                SE = pattern[row_number+1][col_number+1]
            S = 0
            if (row_number < row_count-1):
                S = pattern[row_number+1][col_number]
            SW = 0
            if (row_number < row_count-1) and (col_number > 0):
                SW = pattern[row_number+1][col_number-1]
            W = 0
            if (col_number > 0):
                W = pattern[row_number][col_number-1]
            neighbortotal = NW+N+NE+E+SE+S+SW+W
            #Fewer than 2 live neighbors, dies from Underpopulation
            if (pattern[row_number][col_number] == 1) and (neighbortotal < 2):
                    value = 0
            #Has 2 or 3 live neighbors, Still Lives
            #if (pattern[row_number-1][col_number-1] == 1):
            #    if (neighbortotal == 2) or (neighbortotal == 3):
            #        newpattern[row_number-1][col_number-1] = 1
            #More than 3 live neighbors, dies from overpopulation
            if (pattern[row_number][col_number] == 1) and (neighbortotal > 3):
                    value = 0
            #Dead with exactly 3 live neighbors, reproduction
            if (pattern[row_number][col_number] == 0) and (neighbortotal == 3):
                    value = 1
            newrow.append(value)
        newpattern.append(newrow)
    return newpattern

def centerpattern(pattern, grid_width, grid_height):
    pattern_width = len(pattern[0])
    pattern_height = len(pattern)

    emptycells_width = int((grid_width - pattern_width)/2)
    emptycells_height = int((grid_height - pattern_height)/2)

    fill_width = (emptycells_width*2) + pattern_width
    newpattern = []
    
    row_number = 1
    for row_number in range(emptycells_height):
        newrow = []
        col_number = 1
        for col_number in range(fill_width):
            newrow.append(0)
        newpattern.append(newrow)
    row_number = 0
    for row_number in range(pattern_height):
        newrow = []
        col_number = 1
        for col_number in range(emptycells_width):
            newrow.append(0)
        col_number = 0
        for col_number in range(pattern_width):
            newrow.append(int(pattern[row_number][col_number]))
        col_number = 1
        for col_number in range(emptycells_width):
            newrow.append(0)
        newpattern.append(newrow)
    row_number = 1
    for row_number in range(emptycells_height):
        newrow = []
        col_number = 1
        for col_number in range(fill_width):
            newrow.append(0)
        newpattern.append(newrow)

    return newpattern
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    screen_width = 800
    screen_height = 800
    particle_count = 10
    particle_maxdistancefromother = 100
    particle_anomolycount = 1
    #bg_image = pygame.image.load("spacee-740x463.jpg")

    # create a surface on screen that has the size of screen_width x screen_height
    screen = pygame.display.set_mode((screen_width,screen_height))

    seedpattern = [[0,0,0,0,0],
                   [0,0,0,0,0],
                   [0,1,1,1,0],
                   [0,0,0,0,0],
                   [0,0,0,0,0]]
    acornpattern = [[0,0,0,0,0,0,0,0,0],
                    [0,0,1,0,0,0,0,0,0],
                    [0,0,0,0,1,0,0,0,0],
                    [0,1,1,0,0,1,1,1,0],
                    [0,0,0,0,0,0,0,0,0]]
    toadpattern = [[0,0,0,0,0,0],
                   [0,0,0,0,0,0],
                   [0,0,1,1,1,0],
                   [0,1,1,1,0,0],
                   [0,0,0,0,0,0],
                   [0,0,0,0,0,0]]
    beaconpattern = [[0,0,0,0,0,0],
                     [0,1,1,0,0,0],
                     [0,1,1,0,0,0],
                     [0,0,0,1,1,0],
                     [0,0,0,1,1,0],
                     [0,0,0,0,0,0]]
    pulsarpattern = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
                     [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
                     [0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,1,1,1,0,0,1,1,0,1,1,0,0,1,1,1,0],
                     [0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0],
                     [0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0],
                     [0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0],
                     [0,1,1,1,0,0,1,1,0,1,1,0,0,1,1,1,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0],
                     [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
                     [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    gunpattern = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
        [0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    currentpattern = centerpattern(gunpattern, 120, 120)
    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
    fps = 2
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