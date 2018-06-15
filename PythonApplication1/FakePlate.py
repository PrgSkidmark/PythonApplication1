
# import the pygame module, so you can use it
import pygame
class ui_id:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

Hot = ui_id(Owner=None, Item=None, Index=None)
Active = ui_id(Owner=None, Item=None, Index=None)


# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    pygame.font.init()

    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    screen_width = 1700
    screen_height = 1200
    
    curwindowxpos = 100
    curwindowypos = 100
    curwindowwidth = 400
    curwindowheight = 400

    bg_image = pygame.image.load("carrearend3.jpg")
    bg_image = pygame.transform.scale(bg_image, (3300,2191))

    bg_image2 = pygame.image.load("carrearend2.jpg")
    bg_image2 = pygame.transform.scale(bg_image2, (1450,815))

    # create a surface on screen that has the size of screen_width x screen_height
    screen = pygame.display.set_mode((screen_width,screen_height))

    licplate_left = 510
    licplate_top = 460
    licplace_width = 520
    licplace_heigth = 111
    eurosymbol_width = 40
    eurosymbol_height = licplace_heigth
    licplaterect = pygame.Rect(licplate_left, licplate_top, licplace_width, licplace_heigth)
    licplatecountryrect = pygame.Rect(licplate_left, licplate_top, eurosymbol_width, eurosymbol_height)
    licplatefont = pygame.font.Font("MANDATOR.ttf", 108)
    eurosymbolfont = pygame.font.Font("MANDATOR.ttf", 24)
    eurosymboltext = "GB"

    #pygame.font.SysFont('Verdana', 75, False)
    licplatetext = "L89HRH"

    OneRect = pygame.Rect(0, 0, 20, 20)
    TwoRect = pygame.Rect(20, 20, 20, 20)
    # define a variable to control the main loop
    running = True
    
    clock = pygame.time.Clock()
    fps = 30
    active = False
    done = False
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if licplaterect.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(licplatetext)
                        licplatetext = ''
                    elif event.key == pygame.K_BACKSPACE:
                        licplatetext = licplatetext[:-1]
                    else:
                        licplatetext += event.unicode
            #mainwindow.mousedown(event.pos)
            #
            #elif event.type == pygame.MOUSEBUTTONUP:
            #    if event.button == 1:            
            #        mainwindow.mouseup()
            #
            #elif event.type == pygame.MOUSEMOTION:
            #    mainwindow.mousemotion(event.pos)

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        clock.tick(fps)

        screen.blit(bg_image, (-800, -800))
        pygame.draw.rect(screen, (244,200,66), licplaterect, 0)
        pygame.draw.rect(screen, (0,0,255), licplatecountryrect, 0)
        licplatetextsurface1 = licplatefont.render(licplatetext[:-3], False, (0, 0, 0))
        licplatetextsurface2 = licplatefont.render(licplatetext[-3:], False, (0, 0, 0))
        licplatetextsurface3 = licplatefont.render(licplatetext[:-3], False, (200,200,200))
        licplatetextsurface4 = licplatefont.render(licplatetext[-3:], False, (200,200,200))
        licplatetextsurface5 = licplatefont.render(licplatetext[:-3], False, (38,38,38))
        licplatetextsurface6 = licplatefont.render(licplatetext[-3:], False, (38,38,38))

        eurosymboltextsurface = eurosymbolfont.render(eurosymboltext, False, (230,255,0))
        licplatetextsurface1_left = licplate_left+eurosymbol_width+((licplace_width-eurosymbol_width)/2)-licplatetextsurface1.get_width()-10
        licplatetextsurface2_left = licplate_left+eurosymbol_width+((licplace_width-eurosymbol_width)/2)+10
        licplatetextsurface1_top = licplate_top+(licplace_heigth/2)-(licplatetextsurface1.get_height()/2)

        screen.blit(licplatetextsurface3,(licplatetextsurface1_left-1, licplatetextsurface1_top-1))
        screen.blit(licplatetextsurface4,(licplatetextsurface2_left-1, licplatetextsurface1_top-1))

        screen.blit(licplatetextsurface5,(licplatetextsurface1_left+1, licplatetextsurface1_top+1))
        screen.blit(licplatetextsurface6,(licplatetextsurface2_left+1, licplatetextsurface1_top+1))

        screen.blit(licplatetextsurface1,(licplatetextsurface1_left, licplatetextsurface1_top))
        screen.blit(licplatetextsurface2,(licplatetextsurface2_left, licplatetextsurface1_top))


        eurosymboltext_left = int(licplate_left+(eurosymbol_width/2)-(eurosymboltextsurface.get_width()/2))
        eurosymboltext_top = int(licplate_top+(licplace_heigth/2)+10)
        eurosymbolcircle_center_top = int(licplate_top+(licplace_heigth/2)-10-(licplace_heigth/4))
        eurosymbolcircle_center_left = int(licplate_left+(eurosymbol_width/2)-10-(eurosymbol_width/4))
        screen.blit(eurosymboltextsurface, (eurosymboltext_left, eurosymboltext_top))
        pygame.draw.circle(screen, (230,255,0), (licplate_left+20, licplate_top+35), int((eurosymbol_width/2)-6), 1)
        pygame.draw.rect(screen, (0,0,0), licplaterect, 2)

        pygame.display.flip()

     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()