# import the pygame module, so you can use it
import pygame
from pygame.sprite import Sprite

class SimpleAnimation(Sprite):

    def __init__(self, frames):
        Sprite.__init__(self)
        self.frames = frames       # save the images in here
        self.current = 0       # idx of current image of the animation
        self.image = frames[0]  # just to prevent some errors
        self.rect = self.image.get_rect()    # same here
        self.playing = 0
        
    def update(self, *args):
        if self.playing:    # only update the animation if it is playing
            self.current += 1
            if self.current == len(self.frames):
                self.current = 0
            self.image = self.frames[self.current]
            # only needed if size changes within the animation
            self.rect = self.image.get_rect(center=self.rect.center)
            
    def start(self):
        self.current = 0
        self.playing = True
        
    def stop(self):
        self.playing = False
        
    def pause(self):
        self.playing = False
        
    def resume(self):
        self.playing = True


cache = {} # has to be global (or a class variable)
def get_sequence(frames_names, sequence, optimize=True):
    frames = []
    global cache
    for name in frames_names:
        #if not cache.has_key(name): # check if it has benn loaded already
        image = pygame.image.load(name) # not optimized
        if optimize:
            if image.get_alpha() is not None:
                image = image.convert_alpha()
            else:
                image = image.convert()
        image = pygame.transform.scale2x(image)
        cache[name] = image
            
        # constructs a sequence of frames equal to frames_names
        frames.append(cache[name]) 
    frames2 = []
    for idx in sequence:
        # constructing the animation sequence according to sequence
        frames2.append(frames[idx]) 
    return frames2

def get_names_list(basename, ext, num, num_digits=1, offset=0):
    names = []
    # format string basename+zero_padded_number+.+ext
    format = "%s%0"+str(num_digits)+"d.%s"
    for i in range(offset, num+1):
        names.append(format % (basename, i,ext)) 
    return names


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
    
    bg_image = pygame.image.load("spacee-740x463.jpg")


    ##image = pygame.image.load("01_image.png")
    ##imagexpos = 50
    ##imageypos = 50
    ##image_rect = image.get_rect()
    ##image_width = image_rect.width
    ##image_height = image_rect.height
    ##
    ##image2 = pygame.image.load("01_image.png")
    ##image2xpos = screen_width - 50
    ##image2ypos = 50
    ##image2_rect = image2.get_rect()
    ##image2_width = image2_rect.width
    ##image2_height = image2_rect.height
    ##
    ##
    ##
    ## 
    ##
    ### how many pixels we move our smily each frame
    ##imagestep_x = 1
    ##imagestep_y = 1
    ##image2step_x = -1
    ##image2step_y = -1
    # create a surface on screen that has the size of screen_width x screen_height
    screen = pygame.display.set_mode((screen_width,screen_height))

    # define a variable to control the main loop
    running = True
    # generate a list of names    
    image_names = get_names_list("running", "png", 6, 1, 1)
    # generate a sequence, here simply 0,1,2,3...
    sequence = range(5)
    # load images
    frames = get_sequence(image_names, sequence) # [0,1,2,3,2,1]
    # prepare animation
    anim = SimpleAnimation(frames)
    anim.rect.topleft = (400-75,300-75) 
    anim.start()

    clock = pygame.time.Clock()
    fps = 6
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        clock.tick(fps)

        # check if the smily is still on screen, if not change direction
        #if pygame.time.get_ticks() % 30 == 0:

        ##if imagexpos>screen_width-image_width or imagexpos<0:
        ##    imagestep_x = -imagestep_x
        ##if imageypos>screen_height-image_height or imageypos<0:
        ##    imagestep_y = -imagestep_y
        ##if image2xpos>screen_width-image_width or image2xpos<0:
        ##    image2step_x = -image2step_x
        ##if image2ypos>screen_height-image_height or image2ypos<0:
        ##    image2step_y = -image2step_y
        ### update the position of the smily
        ##imagexpos += imagestep_x # move it to the right
        ##imageypos += imagestep_y # move it down
        ##image2xpos += image2step_x # move it to the right
        ##image2ypos += image2step_y # move it down
        screen.blit(bg_image, (0, 0))
        # update anim
        anim.update()
        ##screen.blit(image, (imagexpos, imageypos))
        ##screen.blit(image2, (image2xpos, image2ypos))
        # draw anim
        dirty_rect = screen.blit(anim.image, anim.rect)
        # update screen
        pygame.display.update(dirty_rect)

     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()