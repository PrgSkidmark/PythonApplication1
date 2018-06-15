
# import the pygame module, so you can use it
import pygame
class ui_id:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

Hot = ui_id(Owner=None, Item=None, Index=None)
Active = ui_id(Owner=None, Item=None, Index=None)

#class button:
#    def __init__(self, screen, windowtitlebar_xpos, windowtitlebar_ypos, windowtitlebar_width, windowtitlebar_heigth):
#        self.windowtitlebar_rect = pygame.Rect(windowtitlebar_xpos, windowtitlebar_ypos, windowtitlebar_width, windowtitlebar_heigth)

#class windowcommandbar:
#    def __init__(self, screen, windowtitlebar_xpos, windowtitlebar_ypos, windowtitlebar_width, windowtitlebar_heigth):
#        self.windowtitlebar_rect = pygame.Rect(windowtitlebar_xpos, windowtitlebar_ypos, windowtitlebar_width, windowtitlebar_heigth)

class windowbuttontray:
    def __init__(self, surface, windowbuttontray_width, window_rect):
        self.surface = surface
        self.windowbuttontray_width = windowbuttontray_width
        self.windowbuttontray_height = 20
        self.windowbuttontray_rect = pygame.Rect(window_rect.left+window_rect.width-self.windowbuttontray_width,window_rect.top+1, self.windowbuttontray_width, self.windowbuttontray_height)
    def update(self, *args):
        self.windowbuttontray_rect = pygame.Rect(args[0].left+args[0].width-self.windowbuttontray_width,args[0].top+1, self.windowbuttontray_width, self.windowbuttontray_height)
        pygame.draw.rect(self.surface, (0,0,0), self.windowbuttontray_rect, 1)

class windowtitlebar:
    def __init__(self, surface, windowtitlebartext, windownavigationbar_width, windowbuttontray_width, window_rect):
        self.surface = surface
        self.windownavigationbar_width = windownavigationbar_width
        self.windowtitlebar_width = window_rect.width-windownavigationbar_width-windowbuttontray_width
        self.windowtitlebar_height = 20
        self.windowtitlebar_rect = pygame.Rect(window_rect.left + self.windownavigationbar_width+1, window_rect.top+1, self.windowtitlebar_width, self.windowtitlebar_height)
        self.titlefont = pygame.font.SysFont('Comic Sans MS', 12)
        self.text = windowtitlebartext

    def update(self, *args):
        self.windowtitlebar_rect = pygame.Rect(args[0].left + self.windownavigationbar_width+1, args[0].top+1, self.windowtitlebar_width, self.windowtitlebar_height)
        pygame.draw.rect(self.surface, (0,0,0), self.windowtitlebar_rect, 1)
        titletextsurface = self.titlefont.render(self.text, False, (0, 0, 0))
        self.surface.blit(titletextsurface,(self.windowtitlebar_rect.left+2,self.windowtitlebar_rect.top))


class windownavigationbar:
    def __init__(self, surface, windownavigationbar_width, window_rect):
        self.expanded = True
        self.surface = surface
        self.windownavigationbar_width = windownavigationbar_width
        self.windownavigationbar_rect = pygame.Rect(window_rect.left, window_rect.top, self.windownavigationbar_width, window_rect.height)

    def update(self, *args):
        self.windownavigationbar_rect = pygame.Rect(args[0].left, args[0].top, self.windownavigationbar_width, args[0].height)
        #if self.visible:    # only update the animation if it is playing
        pygame.draw.rect(self.surface, (128,128,128), self.windownavigationbar_rect, 0)

    def get_width():
        return self.windownavigationbar_width

class window:
    def __init__(self, surface, windowtitle, window_xpos, window_ypos, window_width, window_heigth):
        self.visible = True
        self.surface = surface
        self.title = windowtitle
        self.offset_x = 0
        self.offset_y = 0
        self.rectangle_dragging = False
        self.window_rect = pygame.Rect(window_xpos, window_ypos, window_width, window_heigth)
        self.windownavigationbar1_width = 100
        self.windowbuttontray1_width = 18*3
        self.windownavigationbar1 = windownavigationbar(self.surface, self.windownavigationbar1_width, self.window_rect)
        self.windowtitlebar1 = windowtitlebar(self.surface, self.title, self.windownavigationbar1_width, self.windowbuttontray1_width, self.window_rect)
        self.windowbuttontray1 = windowbuttontray(self.surface, self.windowbuttontray1_width, self.window_rect)

    def mousedown(self, *args):
        self.curmousepos = args[0]
        if self.windowtitlebar1.windowtitlebar_rect.collidepoint(self.curmousepos):
            self.rectangle_dragging = True;
            mouse_x, mouse_y = self.curmousepos
            self.offset_x = self.window_rect.left - mouse_x
            self.offset_y = self.window_rect.top - mouse_y

    def mouseup(self):
        if self.rectangle_dragging:
            self.rectangle_dragging = False;

    def mousemotion(self, *args):
        if self.rectangle_dragging:
            mouse_x, mouse_y = args[0]
            self.window_rect.left = mouse_x + self.offset_x
            self.window_rect.top = mouse_y + self.offset_y

    def update(self, *args):
        if self.visible:    # only update the window if it is visible
            pygame.draw.rect(self.surface, (255,255,255), self.window_rect, 0)
            self.windownavigationbar1.update(self.window_rect)
            self.windowtitlebar1.update(self.window_rect)
            self.windowbuttontray1.update(self.window_rect)


# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    pygame.font.init()

    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    screen_width = 740
    screen_height = 463
    
    curwindowxpos = 100
    curwindowypos = 100
    curwindowwidth = 400
    curwindowheight = 400

    bg_image = pygame.image.load("carrearend.jpg")
    bg_image = pygame.transform.scale(bg_image, (1320,990))
    # create a surface on screen that has the size of screen_width x screen_height
    screen = pygame.display.set_mode((screen_width,screen_height))
    mainwindow = window(screen,"Main Window", curwindowxpos, curwindowypos, curwindowwidth, curwindowheight)

    # define a variable to control the main loop
    running = True
    licplatefont = pygame.font.SysFont('Courier New', 80, True)
    
    clock = pygame.time.Clock()
    fps = 30
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mainwindow.mousedown(event.pos)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:            
                    mainwindow.mouseup()

            elif event.type == pygame.MOUSEMOTION:
                mainwindow.mousemotion(event.pos)

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        clock.tick(fps)

        screen.blit(bg_image, (-280, -270))
        
        mainwindow.update()
        #licplacerect = pygame.Rect(200, 200, 400, 120)
        #licplacecountryrect = pygame.Rect(200, 200, 40, 120)
        #pygame.draw.rect(screen, (230,255,0), licplacerect, 0)
        #pygame.draw.rect(screen, (0,0,255), licplacecountryrect, 0)
        #licplatetextsurface = licplatefont.render("BRILMBO", False, (0, 0, 0))
        #screen.blit(licplatetextsurface,(250, 210))
        #pygame.draw.rect(screen, (0,0,0), licplacerect, 2)


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