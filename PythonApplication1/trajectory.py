# import the pygame module, so you can use it
import pygame
import random
import math
from collections import namedtuple
from pygame import gfxdraw

class particle:
    def __init__(self, surface_width, surface_height, x, y, size, color, isanomoly, offset_x, offset_y, particle_distance, particle_motion):
        self.width = surface_width
        self.height = surface_height
        self.x = x
        self.y = y
        self.init_x = x
        self.init_y = y
        self.size = size
        self.color = color
        self.isanomoly = isanomoly
        self.particle_distance = particle_distance
        self.particle_motion = particle_motion
        self.isattop = False
        self.changeddirection = False
        self.frame_number = 1
        self.frame_count = 360
        self.previous_frames = []
        self.ellipse_width = 100
        self.ellipse_height = 10
        self.vector_x = 0
        self.vector_y = 0
        self.initial_angle = 50
        self.offset_x = offset_x #int(self.width/2)
        self.offset_y = offset_y #int(self.height/2)

    def reset(self, x, y, size, color, isanomoly, particle_distance, particle_motion):
        self.x = x
        self.y = y
        self.init_x = x
        self.init_y = y
        self.size = size
        self.color = color
        self.isanomoly = isanomoly
        self.particle_distance = particle_distance
        self.particle_motion = particle_motion
        self.isattop = False
        self.changeddirection = False
        self.frame_number = 1
        self.frame_count = 360
        self.previous_frames = []
        self.ellipse_width = 100
        self.ellipse_height = 10
        self.vector_x = 0
        self.vector_y = 0
       
    def get_vector_x(self, *args):
        return self.vector_x
    def get_vector_y(self, *args):
        return self.vector_y
    def set_vector_x(self, new_vector_x):
        self.vector_x = new_vector_x
    def set_vector_y(self, new_vector_y):
        self.vector_y = new_vector_y
    def update(self, *args):
        self.particle_motion.update(self)
    def render(self, surface):
        self.particle_motion.render(self, surface)

class particle_motion(object):
    pass

class particle_motion_trajectory(particle_motion):
    def init_vector(self, particle):
        particle_vector_y = random.randint(10,70) #velocity
        particle.set_vector_x(1)
        particle.set_vector_y(particle_vector_y)
        particle.initial_angle = random.randint(50, 89)

    def update(self, particle):
        particle_xOffset = int(particle.width/2)
        particle_yOffset = int(particle.height/2)
        particle.x = particle.x+particle.vector_x
        theta = math.radians(particle.initial_angle)

        particle_y = (math.tan(theta)*particle.x) - ( ( 9.8 / (2 * particle.vector_y**2 * math.cos(theta)**2) )*particle.x**2 )

        particle.y = int(particle_y)

        if (particle.y < 0):
            particle.x = particle.init_x
            particle.y = particle.init_y
            particle.vector_y = random.randint(10,70)
        if (particle.y > particle.height):
            particle.x = particle.init_x
            particle.y = particle.init_y
            particle.vector_y = random.randint(10,70)

    def render(self, particle, surface):
        if (random.randint(1, 100) < 50):
            gfxdraw.filled_circle(surface, particle.offset_x + particle.x, particle.offset_y - particle.y, particle.size, particle.color)
        else:
            gfxdraw.filled_circle(surface, particle.offset_x - particle.x, particle.offset_y - particle.y, particle.size, particle.color)

        #for particle_frame in particle.previous_frames:
        #    gfxdraw.filled_circle(self.surface, particle_frame[0], particle_frame[1], particle.size, particle_frame[2])


    def mousescrollup(self, *args):
        particle.set_vector_y(particle.get_vector_y(particle)+1)
    def mousescrolldown(self, *args):
        particle.set_vector_y(particle.get_vector_y(particle)-1)

class particle_placement(object):
    pass

class particle_placement_insidecannon(particle_placement):
    def __init__(self, surface_width, surface_height, particle_array, particle_count, anomoly_count, particle_maxdistancefromother, particle_motion_selected):
        self.surface_width = surface_width
        self.surface_height = surface_height
        self.particle_array = particle_array
        self.particle_count = particle_count
        self.anomoly_count = anomoly_count
        self.particle_maxdistancefromother = particle_maxdistancefromother
        self.particle_motion_selected = particle_motion_selected
        particle_number = 1
        for particle_number in range(self.particle_count):
            isAnomoly = False
            particle_x = 0
            particle_y = 0
            particle_radius = random.randint(1, 2)
            particle_color = (int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)))
            offset_x = int(self.surface_width/2)
            offset_y = int(self.surface_height/2)

            myparticle = particle(self.surface_width, self.surface_height, particle_x, particle_y, particle_radius, particle_color, isAnomoly, offset_x, offset_y, self.particle_maxdistancefromother, self.particle_motion_selected)
            self.particle_motion_selected.init_vector(myparticle);
            self.particle_array.append(myparticle) # top of 1st story, upper left

    def reset(self, *args):
        particle_number = 1
        for particle in self.particle_array:
            particle.x = 0
            particle.y = 0
            particle.size = random.randint(1, 2)
            particle.color = (int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)))

class particle_generator(object):
    def __init__(self, surface, particle_count, particle_maxdistancefromother, anomoly_count):
        self.pausing = False
        self.surface = surface
        self.surface_width = surface.get_width()
        self.surface_height = surface.get_height()
        self.particle_count = particle_count
        self.particle_maxdistancefromother = particle_maxdistancefromother
        self.particle_array = [] # start with an empty list
        self.anomoly_count = anomoly_count

    def update(self, *args):
        #for particle in self.particle_array:
            #pygame.draw.circle(self.surface, (100,100,100), (particle[0], particle[1]), particle[2], 0)
            #gfxdraw.circle(self.surface, particle[0], particle[1], particle[2], (100,100,100))
            #gfxdraw.pixel(self.surface, particle[0], particle[1], (100,100,100))
        for particle in self.particle_array:
            if (not self.pausing):
                particle.update()

    def render(self, *args):
        for particle in self.particle_array:
            particle.render(self.surface);
                

    def reset(self, *args):
        pass

    def mousemotion(self, *args):
        self.mouse_x, self.mouse_y = args[0]

    def pause(self, *args):
        self.pausing = not self.pausing
    
    def get_particle_array(self, *args):
        return self.particle_array

class particle_generate_onetype(particle_generator):
    def __init__(self, surface, particle_count, particle_maxdistancefromother, anomoly_count):
        particle_generator.pausing = False
        particle_generator.surface = surface
        particle_generator.surface_width = surface.get_width()
        particle_generator.surface_height = surface.get_height()
        particle_generator.particle_count = particle_count
        particle_generator.particle_maxdistancefromother = particle_maxdistancefromother
        particle_generator.particle_array = [] # start with an empty list
        particle_generator.anomoly_count = anomoly_count
        self.particle_motion_selected = particle_motion_trajectory()
        self.particle_placement_selected = particle_placement_insidecannon(particle_generator.surface_width, particle_generator.surface_height, particle_generator.particle_array, particle_generator.particle_count, particle_generator.anomoly_count, particle_generator.particle_maxdistancefromother, self.particle_motion_selected)

    def update(self, *args):
        particle_generator.update(self, *args)
        particle_generator.render(self, *args)

    def reset(self, *args):
        self.particle_placement_selected.reset(args)
    
    def pause(self, *args):
        particle_generator.pause(self, *args)
    
    def get_particle_array(self, *args):
        particle_generator.get_particle_array(self, *args)

    def mousescrollup(self, *args):
        self.particle_motion_selected.mousescrollup(self, *args)
    def mousescrolldown(self, *args):
        self.particle_motion_selected.mousescrolldown(self, *args)

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
    bg_image = pygame.image.load("spacee-740x463.jpg")

    # create a surface on screen that has the size of screen_width x screen_height
    screen = pygame.display.set_mode((screen_width,screen_height))
    particle_generator_selected = particle_generate_onetype(screen, particle_count, particle_maxdistancefromother, particle_anomolycount);
    #myparticle_connector = particle_connector(screen, myparticle_generator.get_particle_array());
    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
    fps = 60
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
        particle_generator_selected.update()
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