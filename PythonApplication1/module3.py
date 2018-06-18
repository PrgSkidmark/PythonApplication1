
# import the pygame module, so you can use it
import pygame
#from pygame import gfxdraw
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
        self.windowbuttontray_left = window_rect.left+window_rect.width-self.windowbuttontray_width
        self.windowbuttontray_height = 20
        #self.windowbuttontray_rect = pygame.Rect(window_rect.left+window_rect.width-self.windowbuttontray_width,window_rect.top+1, self.windowbuttontray_width, self.windowbuttontray_height)
        self.windowbuttontray_rect = pygame.Rect(self.windowbuttontray_left,window_rect.top+1, self.windowbuttontray_width, self.windowbuttontray_height)
        self.button_width = 18
        self.buttonfont = pygame.font.SysFont('Comic Sans MS', 12)
        #self.button_space = title_button_width/2
        self.button1_rect = pygame.Rect(self.windowbuttontray_rect.left,self.windowbuttontray_rect.top+1,self.button_width,self.button_width)
        self.button2_rect = pygame.Rect(self.windowbuttontray_rect.left+self.button_width,self.windowbuttontray_rect.top+1,self.button_width,self.button_width)
        self.button3_rect = pygame.Rect(self.windowbuttontray_rect.left+(self.button_width*2),self.windowbuttontray_rect.top+1,self.button_width,self.button_width)

    def update(self, *args):
        self.windowbuttontray_left = args[0].left+args[0].width-self.windowbuttontray_width
        self.windowbuttontray_rect = pygame.Rect(self.windowbuttontray_left,args[0].top+1, self.windowbuttontray_width, self.windowbuttontray_height)
        self.button1_rect = pygame.Rect(self.windowbuttontray_rect.left,self.windowbuttontray_rect.top+1,self.button_width,self.button_width)
        self.button2_rect = pygame.Rect(self.windowbuttontray_rect.left+self.button_width,self.windowbuttontray_rect.top+1,self.button_width,self.button_width)
        self.button3_rect = pygame.Rect(self.windowbuttontray_rect.left+(self.button_width*2),self.windowbuttontray_rect.top+1,self.button_width,self.button_width)
        pygame.draw.rect(self.surface, (100,100,100), self.windowbuttontray_rect, 1)
        #pygame.draw.rect(self.surface, (0,0,0), self.button1_rect, 1)
        #pygame.draw.rect(self.surface, (0,0,0), self.button2_rect, 1)
        #pygame.draw.rect(self.surface, (0,0,0), self.button3_rect, 1)
        button1_surface = self.buttonfont.render("_", False, (0, 0, 0))
        if args[1]:
            button2_surface = self.buttonfont.render("v", False, (0, 0, 0))
        else :
            button2_surface = self.buttonfont.render("^", False, (0, 0, 0))
        button3_surface = self.buttonfont.render("X", False, (0, 0, 0))
        self.surface.blit(button1_surface,(self.button1_rect.left+4,self.windowbuttontray_rect.top+1))
        self.surface.blit(button2_surface,(self.button2_rect.left+4,self.windowbuttontray_rect.top+1))
        self.surface.blit(button3_surface,(self.button3_rect.left+4,self.windowbuttontray_rect.top+1))


class windowtitlebar:
    def __init__(self, surface, windowtitlebartext, windownavigationbar_width, windowbuttontray_width, window_rect):
        self.surface = surface
        self.windownavigationbar_width = windownavigationbar_width
        self.windowtitlebar_width = window_rect.width-window_rect.left-windownavigationbar_width-windowbuttontray_width
        self.windowtitlebar_height = 20
        self.windowtitlebar_rect = pygame.Rect(window_rect.left + self.windownavigationbar_width+1, window_rect.top+1, self.windowtitlebar_width, self.windowtitlebar_height)
        self.titlefont = pygame.font.SysFont('Comic Sans MS', 12)
        self.text = windowtitlebartext

    def update(self, *args):
        self.windowtitlebar_rect = pygame.Rect(args[0].left + self.windownavigationbar_width+1, args[0].top+1, self.windowtitlebar_width, self.windowtitlebar_height)
        pygame.draw.rect(self.surface, (100,100,100), self.windowtitlebar_rect, 0)
        titletextsurface = self.titlefont.render(self.text, False, (0, 0, 0))
        self.surface.blit(titletextsurface,(self.windowtitlebar_rect.left+2,self.windowtitlebar_rect.top))

class windowntabcontent:
    def __init__(self, surface, tabcontent_index, tabcontent_count, tabcontent_text, windownavigationbar_width, window_rect):
        self.surface = surface
        self.window_rect = window_rect
        self.tabcontent_index = tabcontent_index
        self.tabcontent_count = tabcontent_count
        self.tabcontent_active = False
        self.tabcontent_showing = False
        self.tabcontent_hiding = False
        self.tabcontent_showing_framecount = 30
        self.tabcontent_showing_framecurrent = 30
        self.tabcontent_hiding_framecount = 15
        self.tabcontent_hiding_framecurrent = 1

        self.tabcontent_font = pygame.font.SysFont('Comic Sans MS', 12)
        self.tabcontent_text = tabcontent_text
        self.windownavigationbar_width = windownavigationbar_width
        self.windownavigationbar_top = self.window_rect.top
        self.tabcontent_width = self.window_rect.left+self.window_rect.width - self.windownavigationbar_width-20
        self.tabcontent_notchtop = self.window_rect.top+50
        self.tabcontent_notchwidth = 20
        self.tabcontent_notchheight = 480 #need to get height dynamic
        self.tabcontent_height = self.window_rect.height-20
        self.tabcontent_left = self.window_rect.left+self.windownavigationbar_width+20
        self.tabcontent_top = self.window_rect.top+20

        self.tabcontentnotch_poly = [(self.tabcontent_left,self.tabcontent_notchtop),
                                     (self.tabcontent_left,self.tabcontent_notchtop+self.tabcontent_notchheight),
                                     (self.tabcontent_left-self.tabcontent_notchwidth,self.tabcontent_notchtop+self.tabcontent_notchheight-20),
                                     (self.tabcontent_left-self.tabcontent_notchwidth,self.tabcontent_notchtop+20)]
        self.tabcontent_rect = pygame.Rect(self.tabcontent_left,self.tabcontent_top,self.tabcontent_width,self.tabcontent_height)

    def show(self, *args):
        self.tabcontent_active = True
        self.tabcontent_showing = True
        self.tabcontent_showing_framecurrent = self.tabcontent_showing_framecount

    def hide(self, *args):
        self.tabcontent_hiding = True
        self.tabcontent_hiding_framecurrent = 1
        #self.tabcontent_active = False   # set the content to inactive after the hide animation

    #def mousedown(self, *args):
    #    self.curmousepos = args[0]
    #    self.tab_active = True

    def update(self, *args):
        if self.tabcontent_active:
            if self.tabcontent_showing:
                self.tabcontent_left = self.window_rect.left+self.windownavigationbar_width+((self.window_rect.width/self.tabcontent_showing_framecount)*self.tabcontent_showing_framecurrent)
                self.tabcontent_showing_framecurrent = self.tabcontent_showing_framecurrent-1
                self.tabcontentnotch_poly = [(self.tabcontent_left,self.tabcontent_notchtop),
                                             (self.tabcontent_left,self.tabcontent_notchtop+self.tabcontent_notchheight),
                                             (self.tabcontent_left-self.tabcontent_notchwidth,self.tabcontent_notchtop+self.tabcontent_notchheight-20),
                                             (self.tabcontent_left-self.tabcontent_notchwidth,self.tabcontent_notchtop+20)]
                self.tabcontent_rect = pygame.Rect(self.tabcontent_left,self.tabcontent_top,self.tabcontent_width,self.tabcontent_height)

                pygame.draw.rect(self.surface, (100,100,100), self.tabcontent_rect, 0)
                pygame.draw.polygon(self.surface, (100,100,100), self.tabcontentnotch_poly, 0)

                tabcontenttextsurface = self.tabcontent_font.render(self.tabcontent_text, False, (255, 255, 255))
                tabcontenttextsurface = pygame.transform.rotate(tabcontenttextsurface, 270)
                self.surface.blit(tabcontenttextsurface,(self.tabcontent_left-self.tabcontent_notchwidth,self.tabcontent_top+(self.tabcontent_notchheight/2)))
                
                #increment frames
                if self.tabcontent_showing_framecurrent == 1:
                    self.tabcontent_showing = False

            elif self.tabcontent_hiding:
                self.tabcontent_left = self.window_rect.left+self.windownavigationbar_width+20-((self.window_rect.width/self.tabcontent_hiding_framecount)*self.tabcontent_hiding_framecurrent)
                self.tabcontent_hiding_framecurrent = self.tabcontent_hiding_framecurrent+1
                #self.tabcontentnotch_poly = [(self.tabcontent_left,self.tabcontent_notchtop),
                #                             (self.tabcontent_left,self.tabcontent_notchtop+self.tabcontent_notchheight),
                #                             (self.tabcontent_left-self.tabcontent_notchwidth,self.tabcontent_notchtop+self.tabcontent_notchheight-20),
                #                             (self.tabcontent_left-self.tabcontent_notchwidth,self.tabcontent_notchtop+20)]
                self.tabcontent_rect = pygame.Rect(self.tabcontent_left,self.tabcontent_top,self.tabcontent_width,self.tabcontent_height)

                pygame.draw.rect(self.surface, (100,100,100), self.tabcontent_rect, 0)
                #pygame.draw.polygon(self.surface, (100,100,100), self.tabcontentnotch_poly, 0)

                #tabcontenttextsurface = self.tabcontent_font.render(self.tabcontent_text, False, (255, 255, 255))
                #tabcontenttextsurface = pygame.transform.rotate(tabcontenttextsurface, 270)
                #self.surface.blit(tabcontenttextsurface,(self.tabcontent_left-self.tabcontent_notchwidth,self.tabcontent_top+(self.tabcontent_notchheight/2)))
                #increment frames
                if self.tabcontent_hiding_framecurrent == self.tabcontent_hiding_framecount:
                    self.tabcontent_hiding = False
                    self.tabcontent_active = False

            else:
                self.tabcontent_left = self.window_rect.left+self.windownavigationbar_width+20

                self.tabcontentnotch_poly = [(self.tabcontent_left,self.tabcontent_notchtop),
                                             (self.tabcontent_left,self.tabcontent_notchtop+self.tabcontent_notchheight),
                                             (self.tabcontent_left-self.tabcontent_notchwidth,self.tabcontent_notchtop+self.tabcontent_notchheight-20),
                                             (self.tabcontent_left-self.tabcontent_notchwidth,self.tabcontent_notchtop+20)]
                self.tabcontent_rect = pygame.Rect(self.tabcontent_left,self.tabcontent_top,self.tabcontent_width,self.tabcontent_height)

                pygame.draw.rect(self.surface, (100,100,100), self.tabcontent_rect, 0)
                pygame.draw.polygon(self.surface, (100,100,100), self.tabcontentnotch_poly, 0)

                tabcontenttextsurface = self.tabcontent_font.render(self.tabcontent_text, False, (255, 255, 255))
                tabcontenttextsurface = pygame.transform.rotate(tabcontenttextsurface, 270)
                self.surface.blit(tabcontenttextsurface,(self.tabcontent_left-self.tabcontent_notchwidth,self.tabcontent_top+(self.tabcontent_notchheight/2)))



class windownavigationtab:
    def __init__(self, surface, tab_index, tab_count, tab_text, windownavigationbar_width, window_rect):
        self.surface = surface
        self.tab_index = tab_index
        self.tab_count = tab_count
        self.tab_active = False
        self.tab_font = pygame.font.SysFont('Comic Sans MS', 12)
        self.tab_text = tab_text
        self.windownavigationbar_width = windownavigationbar_width
        self.windownavigationbar_top = window_rect.top
        self.tab_width = 30
        self.tab_notchwidth = 20
        self.tab_notchheight = 45
        self.tab_height = 100
        self.tab_left = (self.windownavigationbar_width/2)-(self.tab_width/2)
        self.tab_top = self.windownavigationbar_top+(self.tab_index*(self.tab_height-20))
        self.windownavigationtab_poly = [(self.tab_left,self.tab_top),(self.tab_left+self.tab_notchwidth,self.tab_top),
                                         (self.tab_left+self.tab_notchwidth,self.tab_top+self.tab_notchheight),
                                         (self.tab_left+self.tab_width,self.tab_top+self.tab_notchheight+10),
                                         (self.tab_left+self.tab_width,self.tab_top+self.tab_height),(self.tab_left,self.tab_top+self.tab_height)]
        self.windownavigationtab_rect = pygame.Rect(self.tab_left,self.tab_top,self.tab_width,self.tab_height)

    def activate(self):
        self.tab_active = True

    def inactivate(self):
        self.tab_active = False

    #def mousedown(self, *args):
    #    self.curmousepos = args[0]
    #    self.tab_active = True

    def update(self, *args):
        if self.tab_active:
            pygame.draw.polygon(self.surface, (100,100,100), self.windownavigationtab_poly, 0)
            pygame.draw.polygon(self.surface, (255,255,255), self.windownavigationtab_poly, 1)
        else:
            pygame.draw.polygon(self.surface, (0,(self.tab_count-self.tab_index)*30,255), self.windownavigationtab_poly, 0)
            pygame.draw.polygon(self.surface, (255,255,255), self.windownavigationtab_poly, 1)
        tabtextsurface = self.tab_font.render(self.tab_text, False, (255, 255, 255))
        tabtextsurface = pygame.transform.rotate(tabtextsurface, 270)
        self.surface.blit(tabtextsurface,(self.tab_left+2,self.tab_top+4))

class windownavigationbar:
    def __init__(self, surface, windownavigationbar_width, window_rect, parent):
        self.parent = parent
        self.expanded = True
        self.surface = surface
        self.windownavigationbar_width = windownavigationbar_width
        self.windownavigationbar_rect = pygame.Rect(window_rect.left, window_rect.top, self.windownavigationbar_width, window_rect.height)
        self.windownavigationtab1 = windownavigationtab(self.surface, 1, 5, "First", self.windownavigationbar_width, window_rect)
        self.windownavigationtab2 = windownavigationtab(self.surface, 2, 5, "Second", self.windownavigationbar_width, window_rect)
        self.windownavigationtab3 = windownavigationtab(self.surface, 3, 5, "Third", self.windownavigationbar_width, window_rect)
        self.windownavigationtab4 = windownavigationtab(self.surface, 4, 5, "Fourth", self.windownavigationbar_width, window_rect)
        self.windownavigationtab5 = windownavigationtab(self.surface, 5, 5, "Fifth", self.windownavigationbar_width, window_rect)
        self.windownavigationbarnotch_top = self.windownavigationbar_rect.top+50
        self.windownavigationbarnotch_width = 20
        self.windownavigationbarnotch_height = 480 #need to get height dynamic
        self.windownavigationbarnotch_poly = [(self.windownavigationbar_width,self.windownavigationbarnotch_top),
                                              (self.windownavigationbar_width,self.windownavigationbarnotch_top+self.windownavigationbarnotch_height),
                                              (self.windownavigationbar_width-self.windownavigationbarnotch_width,self.windownavigationbarnotch_top+self.windownavigationbarnotch_height-20),
                                              (self.windownavigationbar_width-self.windownavigationbarnotch_width,self.windownavigationbarnotch_top+20)]
        self.tab_currentactiveindex = 0

    def activatetab(self, *args):
        tab_selected = args[0]
        if tab_selected != self.tab_currentactiveindex:
            self.tab_currentactiveindex = tab_selected
            self.parent.tab_currentactiveindex = tab_selected
            self.windownavigationtab1.inactivate()
            self.windownavigationtab2.inactivate()
            self.windownavigationtab3.inactivate()
            self.windownavigationtab4.inactivate()
            self.windownavigationtab5.inactivate()
            if tab_selected == 1:
                self.windownavigationtab1.activate()
            if tab_selected == 2:
                self.windownavigationtab2.activate()
            if tab_selected == 3:
                self.windownavigationtab3.activate()
            if tab_selected == 4:
                self.windownavigationtab4.activate()
            if tab_selected == 5:
                self.windownavigationtab5.activate()

    def mousedown(self, *args):
        self.curmousepos = args[0]
        tab_selected = 0
        if self.windownavigationtab1.windownavigationtab_rect.collidepoint(self.curmousepos):
            tab_selected = 1
        if self.windownavigationtab2.windownavigationtab_rect.collidepoint(self.curmousepos):
            tab_selected = 2
        if self.windownavigationtab3.windownavigationtab_rect.collidepoint(self.curmousepos):
            tab_selected = 3
        if self.windownavigationtab4.windownavigationtab_rect.collidepoint(self.curmousepos):
            tab_selected = 4
        if self.windownavigationtab5.windownavigationtab_rect.collidepoint(self.curmousepos):
            tab_selected = 5
        self.activatetab(tab_selected)        

    def update(self, *args):
        self.windownavigationbar_rect = pygame.Rect(args[0].left, args[0].top, self.windownavigationbar_width, args[0].height)
        #if self.visible:    # only update the animation if it is playing
        pygame.draw.rect(self.surface, (128,128,128), self.windownavigationbar_rect, 0)
        pygame.draw.polygon(self.surface, (255,255,255), self.windownavigationbarnotch_poly, 0)
        self.windownavigationtab1.update()
        self.windownavigationtab2.update()
        self.windownavigationtab3.update()
        self.windownavigationtab4.update()
        self.windownavigationtab5.update()

    def get_width():
        return self.windownavigationbar_width

class window:
    def __init__(self, surface, windowtitle, window_xpos, window_ypos, window_width, window_heigth):
        self.tab_previousactiveindex = 0
        self.tab_currentactiveindex = 0
        self.visible = True
        self.maximized = True
        self.surface = surface
        self.title = windowtitle
        self.offset_x = 0
        self.offset_y = 0
        self.rectangle_dragging = False
        self.minwindowfont = pygame.font.SysFont('Comic Sans MS', 20)
        self.window_rect = pygame.Rect(window_xpos, window_ypos, window_width, window_heigth)
        self.min_rect = pygame.Rect(0, 0, 30, 30)
        self.max_rect = pygame.Rect(0, 0, surface.get_width(), surface.get_height())
        self.windownavigationbar1_width = 50
        self.windowbuttontray1_width = 18*3
        self.windownavigationbar1 = windownavigationbar(self.surface, self.windownavigationbar1_width, self.window_rect, self)
        self.windowtitlebar1 = windowtitlebar(self.surface, self.title, self.windownavigationbar1_width, self.windowbuttontray1_width, self.window_rect)
        self.windowbuttontray1 = windowbuttontray(self.surface, self.windowbuttontray1_width, self.window_rect)
        self.windowtabcontent1 = windowntabcontent(self.surface, 1, 5, "First",self.windownavigationbar1_width,self.window_rect)
        self.windowtabcontent2 = windowntabcontent(self.surface, 2, 5, "Second",self.windownavigationbar1_width,self.window_rect)
        self.windowtabcontent3 = windowntabcontent(self.surface, 3, 5, "Third",self.windownavigationbar1_width,self.window_rect)
        self.windowtabcontent4 = windowntabcontent(self.surface, 4, 5, "Fourth",self.windownavigationbar1_width,self.window_rect)
        self.windowtabcontent5 = windowntabcontent(self.surface, 5, 5, "Fifth",self.windownavigationbar1_width,self.window_rect)

    def changetabs(self, *args):
        if self.tab_previousactiveindex == 1:
            self.windowtabcontent1.hide()
        if self.tab_currentactiveindex == 1:
            self.windowtabcontent1.show()
        if self.tab_previousactiveindex == 2:
            self.windowtabcontent2.hide()
        if self.tab_currentactiveindex == 2:
            self.windowtabcontent2.show()
        if self.tab_previousactiveindex == 3:
            self.windowtabcontent3.hide()
        if self.tab_currentactiveindex == 3:
            self.windowtabcontent3.show()
        if self.tab_previousactiveindex == 4:
            self.windowtabcontent4.hide()
        if self.tab_currentactiveindex == 4:
            self.windowtabcontent4.show()
        if self.tab_previousactiveindex == 5:
            self.windowtabcontent5.hide()
        if self.tab_currentactiveindex == 5:
            self.windowtabcontent5.show()


    def mousedown(self, *args):
        self.curmousepos = args[0]
        #if self.windowtitlebar1.windowtitlebar_rect.collidepoint(self.curmousepos):
        #    self.rectangle_dragging = True;
        #    mouse_x, mouse_y = self.curmousepos
        #    self.offset_x = self.window_rect.left - mouse_x
        #    self.offset_y = self.window_rect.top - mouse_y
        if self.windowbuttontray1.button1_rect.collidepoint(self.curmousepos):
            self.visible = False
        if self.windowbuttontray1.button2_rect.collidepoint(self.curmousepos):
            self.maximized = not self.maximized
        if self.min_rect.collidepoint(self.curmousepos):
            self.visible = True
        if self.windowbuttontray1.button3_rect.collidepoint(self.curmousepos):
            return True
        if self.windownavigationbar1.windownavigationbar_rect.collidepoint(self.curmousepos):
            self.tab_previousactiveindex = self.tab_currentactiveindex
            self.windownavigationbar1.mousedown(self.curmousepos)
            if self.tab_previousactiveindex != self.tab_currentactiveindex:
                self.changetabs()

    def mouseup(self):
        if self.rectangle_dragging:
            self.rectangle_dragging = False;

    def mousemotion(self, *args):
        if self.rectangle_dragging:
            mouse_x, mouse_y = args[0]
            self.window_rect.left = mouse_x + self.offset_x
            self.window_rect.top = mouse_y + self.offset_y

    def update(self, *args):
        if self.visible and self.maximized == False:    # only update the window if it is visible
            pygame.draw.rect(self.surface, (255,255,255), self.window_rect, 0)
            self.windowtitlebar1.update(self.window_rect)
            self.windowbuttontray1.update(self.window_rect, self.maximized)
            self.windowtabcontent1.update()
            self.windowtabcontent2.update()
            self.windowtabcontent3.update()
            self.windowtabcontent4.update()
            self.windowtabcontent5.update()
            self.windownavigationbar1.update(self.window_rect)
        elif self.visible == False:
            pygame.draw.rect(self.surface, (255,255,255), self.min_rect, 0)
            mintextsurface = self.minwindowfont.render("1", False, (0, 0, 0))
            self.surface.blit(mintextsurface,(self.min_rect.left+4,self.min_rect.top))
        elif self.visible and self.maximized:
            pygame.draw.rect(self.surface, (255,255,255), self.max_rect, 0)
            self.windowtitlebar1.update(self.max_rect)
            self.windowbuttontray1.update(self.max_rect, self.maximized)
            self.windowtabcontent1.update()
            self.windowtabcontent2.update()
            self.windowtabcontent3.update()
            self.windowtabcontent4.update()
            self.windowtabcontent5.update()
            self.windownavigationbar1.update(self.max_rect)


# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    pygame.font.init()

    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    screen_width = 1024
    screen_height = 768
    
    curwindowxpos = 0
    curwindowypos = 0
    #curwindowwidth = 1024
    #curwindowheight = 768

    #bg_image = pygame.image.load("spacee-740x463.jpg")

    # create a surface on screen that has the size of screen_width x screen_height
    #screen = pygame.display.set_mode((screen_width,screen_height))
    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    curwindowwidth = screen.get_width()
    curwindowheight = screen.get_height()

    mainwindow = window(screen,"Main Window", curwindowxpos, curwindowypos, curwindowwidth, curwindowheight)

    # define a variable to control the main loop
    running = True
    
    clock = pygame.time.Clock()
    fps = 30
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mainwindow.mousedown(event.pos):
                        running = False

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

        #screen.blit(bg_image, (0, 0))

        mainwindow.update()
        # draw anim
        #dirty_rect = screen.blit(100, 240)
        # update screen
        #pygame.display.update(dirty_rect)
        pygame.display.update()
        pygame.display.flip()

     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()