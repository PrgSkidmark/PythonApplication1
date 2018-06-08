
# import the pygame module, so you can use it
import pygame
from collections import namedtuple

ui_id = namedtuple("ui_id", "Owner Item Index")

def draw_window(screen, startxpos,startypos):
    pygame.mouse.get_pos()
    window_width = 300
    window_heigth = 300
    titlexpos = startxpos+1
    titleypos = startypos+1
    title_width = window_width-2
    title_height = 20
    title_button_width = 16
    title_button_space = title_button_width/2
    title_button1_xpos = titlexpos+title_width-title_button_space-title_button_width
    title_button1_ypos = titleypos+2
    title_button2_xpos = title_button1_xpos-title_button_space-title_button_width
    title_button2_ypos = titleypos+2
    title_button3_xpos = title_button2_xpos-title_button_space-title_button_width
    title_button3_ypos = titleypos+2
    
    navbar_xpos = startxpos+1
    navbar_ypos = titleypos+title_height+1
    navbar_width = window_width-2
    navbar_height = 40
    pygame.draw.rect(screen, (255,255,255), (startxpos, startypos, window_width, window_heigth), 0)
    pygame.draw.rect(screen, (160,160,160), (titlexpos, titleypos, title_width, title_height), 0)
    pygame.draw.rect(screen, (128,128,128), (title_button1_xpos, title_button1_ypos, title_button_width, title_button_width), 0)
    pygame.draw.rect(screen, (128,128,128), (title_button2_xpos, title_button2_ypos, title_button_width, title_button_width), 0)
    pygame.draw.rect(screen, (128,128,128), (title_button3_xpos, title_button3_ypos, title_button_width, title_button_width), 0)

    pygame.draw.rect(screen, (224,224,224), (navbar_xpos, navbar_ypos, navbar_width, navbar_height), 0)
    #pygame.draw.rect(screen, (0,0,0), (102, 123, 36, 36), 0)
    #pygame.draw.rect(screen, (255,0,0), (451, 103, 16, 16), 0)
    #pygame.draw.rect(screen, (255,0,0), (427, 103, 16, 16), 0)
    #return names

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    screen_width = 740
    screen_height = 463
    
    curwindowxpos = 100
    curwindowypos = 100
    offset_x = 0
    offset_y = 0
    bg_image = pygame.image.load("spacee-740x463.jpg")

    # create a surface on screen that has the size of screen_width x screen_height
    screen = pygame.display.set_mode((screen_width,screen_height))

    # define a variable to control the main loop
    running = True
    rectangle_dragging = False
    clock = pygame.time.Clock()
    fps = 60
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mousepos = event.pos
                    if mousepos[0] > curwindowxpos and mousepos[0] < curwindowxpos+300 and mousepos[1] > curwindowypos and mousepos[1] < curwindowypos+20:
                        rectangle_dragging = True;
                        mouse_x, mouse_y = event.pos
                        offset_x = curwindowxpos - mouse_x
                        offset_y = curwindowypos - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:            
                    rectangle_dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if rectangle_dragging:
                    mouse_x, mouse_y = event.pos
                    curwindowxpos = mouse_x + offset_x
                    curwindowypos = mouse_y + offset_y
                    #rectangle.x = mouse_x + offset_x
                    #rectangle.y = mouse_y + offset_y
                #if Player.rect.collidepoint(event.pos):
            #        Player.click = True
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        clock.tick(fps)

        screen.blit(bg_image, (0, 0))
        draw_window(screen, curwindowxpos, curwindowypos)
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