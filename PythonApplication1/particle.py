
# import the pygame module, so you can use it
import pygame
import random
from collections import namedtuple
from pygame import gfxdraw

ui_id = namedtuple("ui_id", "Owner Item Index")

class particle:
    def __init__(self, width, height, anomoly, particle_distance):
        self.width = width
        self.height = height
        self.x = random.randint(1, width)
        self.y = random.randint(1, height)
        self.size = random.randint(1, 2)
        self.mult = random.randint(0, 255)
        self.vector_x = random.randint(-2, 2)
        self.vector_y = random.randint(-2, 2)
        self.color = (int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)))
        self.anomoly = anomoly
        self.anomolygravity = random.randint(particle_distance/2, particle_distance)+50
    def update(self, *args):
        self.x += self.vector_x
        self.y += self.vector_y
        if self.x > self.width:
            self.x = 1
            self.vector_x = random.randint(-2, 2)
            self.vector_y = random.randint(-2, 2)
        if self.x < 1:
            self.x = self.width
            self.vector_x = random.randint(-2, 2)
            self.vector_y = random.randint(-2, 2)
        if self.y > self.height:
            self.y = 1
            self.vector_x = random.randint(-2, 2)
            self.vector_y = random.randint(-2, 2)
        if self.y < 1:
            self.y = self.height
            self.vector_x = random.randint(-2, 2)
            self.vector_y = random.randint(-2, 2)
        while (self.vector_x == 0) or (self.vector_y == 0):
            self.vector_x = random.randint(-2, 2)
            self.vector_y = random.randint(-2, 2)


class particle_generator:
    def __init__(self, surface, particle_count, particle_distance, anomoly_count):
        self.pausing = False
        self.surface = surface
        self.surface_width = surface.get_width()
        self.surface_height = surface.get_height()
        self.particle_count = particle_count
        self.particle_distance = particle_distance
        self.particle_array = [] # start with an empty list
        self.anomoly_count = anomoly_count
        self.anomoly_array = []
        particle_number = 1
        for particle_number in range(self.particle_count):
            isAnomoly = False
            if (particle_number <= self.anomoly_count):
                isAnomoly = True
            myparticle = particle(self.surface_width, self.surface_height, isAnomoly, self.particle_distance)
            self.particle_array.append(myparticle) # top of 1st story, upper left
            if (isAnomoly):
                self.anomoly_array.append(myparticle)

    def update(self, *args):
        #for particle in self.particle_array:
            #pygame.draw.circle(self.surface, (100,100,100), (particle[0], particle[1]), particle[2], 0)
            #gfxdraw.circle(self.surface, particle[0], particle[1], particle[2], (100,100,100))
            #gfxdraw.pixel(self.surface, particle[0], particle[1], (100,100,100))
        #for anomolyparticle in self.anomoly_array:
        for particle in self.particle_array:
            if (not self.pausing):
                particle.update()
            gfxdraw.filled_circle(self.surface, particle.x, particle.y, particle.size, particle.color)
            if (abs(anomolyparticle.x-particle.x) < anomolyparticle.anomolygravity) and (abs(anomolyparticle.y-particle.y) < anomolyparticle.anomolygravity):
                for particle2 in self.particle_array:
                    if (abs(particle2.x-particle.x) < anomolyparticle.anomolygravity) and (abs(particle2.y-particle.y) < anomolyparticle.anomolygravity) and (particle.size == particle2.size):
                        rednumber = (particle.color[0]+particle2.color[0])/2
                        greennumber = (particle.color[1]+particle2.color[1])/2
                        bluenumber = (particle.color[2]+particle2.color[2])/2
                        color = (int(rednumber),int(greennumber),int(bluenumber))
                        pygame.draw.aaline(self.surface, color, (particle.x,particle.y),(particle2.x,particle2.y), 1)

    def reset(self, *args):
        self.particle_array = [] # start with an empty list
   
        particle_number = 1
        for particle_number in range(self.particle_count):
            myparticle = particle(self.surface_width, self.surface_height, False, self.particle_distance)
            self.particle_array.append(myparticle) # top of 1st story, upper left

    def mousemotion(self, *args):
        self.mouse_x, self.mouse_y = args[0]

    def pause(self, *args):
        self.pausing = not self.pausing
        



# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    screen_width = 1500
    screen_height = 1100
    
    bg_image = pygame.image.load("spacee-740x463.jpg")

    # create a surface on screen that has the size of screen_width x screen_height
    #screen = pygame.display.set_mode((screen_width,screen_height))
    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    myparticle_generator = particle_generator(screen, 200, 100, 200);
    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
    fps = 60
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            #if event.type == pygame.MOUSEBUTTONDOWN:
            #
            #elif event.type == pygame.MOUSEBUTTONUP:
            #
            #elif event.type == pygame.MOUSEMOTION:
            if event.type == pygame.MOUSEMOTION:
                myparticle_generator.mousemotion(event.pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    myparticle_generator.reset()
                if event.key == pygame.K_SPACE:
                    myparticle_generator.pause()
                if event.key == pygame.K_ESCAPE:
                    running = False

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        clock.tick(fps)

        #screen.blit(bg_image, (0, 0))
        screen.fill((0,0,0))
        myparticle_generator.update()
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