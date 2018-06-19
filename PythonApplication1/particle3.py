
# import the pygame module, so you can use it
import pygame
import random
import math
from collections import namedtuple
from pygame import gfxdraw

ui_id = namedtuple("ui_id", "Owner Item Index")

class particle:
    def __init__(self, surface_width, surface_height, x, y, size, color, vector_x, vector_y, isanomoly, particle_distance, particle_motion):
        self.width = surface_width
        self.height = surface_height
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.vector_x = vector_x
        self.vector_y = vector_y
        self.isanomoly = isanomoly
        self.particle_distance = particle_distance
        self.particle_motion = particle_motion
        self.isattop = False
        self.changeddirection = False
        #self.anomolygravity = random.randint(particle_distance/2, particle_distance)
        #self.mult = random.randint(0, 255)
        #self.x = random.randint(1, surface_width)
        #self.y = random.randint(1, surface_height)
        #self.size = random.randint(1, 2)
        #self.color = (int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)))
        #self.vector_x = random.randint(-2, 2)
        #self.vector_y = random.randint(-2, 2)

    def reset(self, x, y, size, color, vector_x, vector_y, isanomoly, particle_distance):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.vector_x = vector_x
        self.vector_y = vector_y
        self.isattop = False
        self.changeddirection = False
        
    def update(self, *args):
        self.particle_motion.update(self)

class particle_motion_none():
    def update(self, particle):
        particle.isattop = False
        particle.changeddirection = False

class particle_motion_twirl():
    def __init__(self, *args):
        self.t = 0
        self.adder = (2*3.14158)/360
        self.degree = 1
        self.a = 75
        self.b = 25
        self.center_x = args[0]
        self.center_y = args[1]

    def update(self, particle):
        particle.isattop = False
        particle.changeddirection = False
        particle.x = self.center_x + int(self.a * math.cos(self.adder*self.degree))
        particle.y = self.center_y + int(self.b * math.sin(self.adder*self.degree))

        self.degree += 3
        if (self.degree == 361):
            self.degree = 1


class particle_motion_wrapsides():
    def update(self, particle):
        particle.x += particle.vector_x
        particle.y += particle.vector_y
        if particle.x > particle.width:
            particle.x = 1
            #particle.vector_x = random.randint(-2, 2)
            #particle.vector_y = random.randint(-2, 2)
            particle.changeddirection = True
        if particle.x < 1:
            particle.x = particle.width
            #particle.vector_x = random.randint(-2, 2)
            #self.vector_y = random.randint(-2, 2)
            particle.changeddirection = True
        if particle.y > particle.height:
            particle.y = 1
            #particle.vector_x = random.randint(-2, 2)
            #particle.vector_y = random.randint(-2, 2)
            particle.changeddirection = True
        if particle.y < 1:
            particle.isattop = True
            particle.y = particle.height
            #particle.vector_x = random.randint(-2, 2)
            #particle.vector_y = self.vector_y*-1
            particle.changeddirection = True
        else:
            particle.isattop = False
            particle.changeddirection = False

class particle_motion_bouncesides():
    #def __init__(self):
    #    self.particle = particle;

    def update(self, particle):
        particle.x += particle.vector_x
        particle.y += particle.vector_y
        if particle.x > particle.width:
            particle.x = particle.width-1
            particle.vector_x = particle.vector_x*-1 #random.randint(-2, 2)
            #self.vector_y = random.randint(-2, 2)
            #self.changeddirection = True
        if particle.x < 1:
            particle.x = 1 #self.width
            particle.vector_x = particle.vector_x*-1 #random.randint(-2, 2)
            #self.vector_y = random.randint(-2, 2)
            #self.changeddirection = True
        if particle.y > particle.height:
            particle.y = 1
            particle.vector_x = random.randint(-2, 2)
            particle.vector_y = random.randint(-2, 2)
            particle.changeddirection = True
        if particle.y < 1:
            particle.isattop = True
            particle.y = 1
            particle.vector_x = random.randint(-2, 2)
            particle.vector_y = self.vector_y*-1
            particle.changeddirection = True
        else:
            particle.isattop = False
            particle.changeddirection = False
        while (particle.vector_x == 0):
            particle.vector_x = random.randint(-2, 2)
        while (particle.vector_y == 0):
            particle.vector_y = random.randint(-2, 2)

class particle_motion_down_straight():
    def update(self, particle):
        #particle.x += particle.vector_x
        particle.y += particle.vector_y
        if particle.y > particle.height:
            particle.isattop = False
            particle.y = -10
            particle.changeddirection = True
        else:
            particle.isattop = False
            particle.changeddirection = False

class particle_motion_down_zigzag():
    def update(self, particle):
        particle.x += particle.vector_x
        particle.y += particle.vector_y
        if particle.y > particle.height:
            particle.isattop = False
            particle.y = -10
            particle.vector_x = random.randint(-4, 4)
            #particle.vector_y = random.randint(-2, 2)
            particle.changeddirection = True
        elif particle.x > particle.width:
            particle.x = 1
            #particle.vector_x = random.randint(-2, 2)
            #particle.vector_y = random.randint(-2, 2)
            particle.changeddirection = True
        elif particle.x < 1:
            particle.x = particle.width
            #particle.vector_x = random.randint(-2, 2)
            #self.vector_y = random.randint(-2, 2)
            particle.changeddirection = True
        else:
            particle.isattop = False
            particle.changeddirection = False
        while (particle.vector_x == 0):
            particle.vector_x = random.randint(-4, 4)

class particle_connector:
    def __init__(self, surface, particle_array):
        self.surface = surface
        self.particle_array = particle_array
        self.currentstyle = 1
        self.frame_count = 30
        self.frames_array = []

    def setstyle(self, *args):
        self.currentstyle = int(args[0])
        if (self.currentstyle == 1):
            self.frame_count = 30
        else:
            self.frame_count = 30

    def finddestination(self, *args):
        current_frame = args[0]
        direction = args[2]
        current_sourceparticle = current_frame[0]
        for particle in self.particle_array:
            if (direction == "down"):
                if ((particle.y > current_sourceparticle.y) and (abs(particle.y - current_sourceparticle.y) <= particle.particle_distance) and (abs(particle.x - current_sourceparticle.x) <= particle.particle_distance)):
                    new_frame = (current_sourceparticle, particle, 1)
                    current_frame = new_frame
                    self.frames_array[args[1]] = new_frame
                    break
            else:
                if ((abs(particle.y - current_sourceparticle.y) <= particle.particle_distance) and (abs(particle.x - current_sourceparticle.x) <= particle.particle_distance)):
                    new_frame = (current_sourceparticle, particle, 1)
                    self.frames_array.append(new_frame)
        if (current_frame[1] == None):
            new_frame = (current_sourceparticle, None, -1)
            self.frames_array[args[1]] = new_frame

    def renderframe(self, *args):
        current_frame = args[0]
        direction = args[2]
        current_sourceparticle = current_frame[0]
        current_destparticle = current_frame[1]
        current_frame_number = current_frame[2]
        if ((current_sourceparticle.changeddirection == True) or (current_destparticle.changeddirection == True)):
            new_frame = (current_sourceparticle, current_destparticle, -1)
        else:
            if (direction == "down"):
                if ((current_destparticle.y > current_sourceparticle.y) and (abs(current_destparticle.y - current_sourceparticle.y) <= current_destparticle.particle_distance) and (abs(current_destparticle.x - current_sourceparticle.x) <= current_destparticle.particle_distance)):
                    rednumber = (current_sourceparticle.color[0]+current_destparticle.color[0])/2
                    greennumber = (current_sourceparticle.color[1]+current_destparticle.color[1])/2
                    bluenumber = (current_sourceparticle.color[2]+current_destparticle.color[2])/2
                    color = (int(rednumber),int(greennumber),int(bluenumber))
                    pygame.draw.aaline(self.surface, color, (current_sourceparticle.x,current_sourceparticle.y),(current_destparticle.x,current_destparticle.y), 1)
            else:
                if ((abs(current_destparticle.y - current_sourceparticle.y) <= current_destparticle.particle_distance) and (abs(current_destparticle.x - current_sourceparticle.x) <= current_destparticle.particle_distance)):
                    rednumber = (current_sourceparticle.color[0]+current_destparticle.color[0])/2
                    greennumber = (current_sourceparticle.color[1]+current_destparticle.color[1])/2
                    bluenumber = (current_sourceparticle.color[2]+current_destparticle.color[2])/2
                    color = (int(rednumber),int(greennumber),int(bluenumber))
                    pygame.draw.aaline(self.surface, color, (current_sourceparticle.x,current_sourceparticle.y),(current_destparticle.x,current_destparticle.y), 1)
            new_frame = (current_sourceparticle, current_destparticle, current_frame_number+1)
        self.frames_array[args[1]] = new_frame

    def updatelinedrop(self, *args):
        # find new particles at the top
        for particle in self.particle_array:
            if (particle.isattop == True):
                self.frames_array.append((particle, None, 0))
                #finddestinationparticle(frames_array)
        frame_number = 0
        for frame in self.frames_array:
            if ((frame[2] == -1) or (frame[0].changeddirection == True)):
                self.frames_array.pop(frame_number)
            elif (frame[2] == 0):
                self.finddestination(frame, frame_number, "down")
            elif ((frame[2] > 0) and (frame[2] < self.frame_count)):
                self.renderframe(frame, frame_number, "down")
            elif (frame[2] >= self.frame_count):
                current_destparticle = frame[1]
                self.frames_array.pop(frame_number)
                new_frame = (current_destparticle, None, 0)
                self.frames_array.append(new_frame)
            frame_number += 1
    def updateanomoly(self, *args):
        # anomolies will attach to particles around it
        for particle1 in self.particle_array:
            if (particle1.isanomoly == True):
                self.frames_array.append((particle1, None, 0))
        frame_number = 0
        for frame in self.frames_array:
            if ((frame[2] == -1) or (frame[0].changeddirection == True)):
                self.frames_array.pop(frame_number)
            elif (frame[2] == 0):
                self.finddestination(frame, frame_number, "any")
            elif ((frame[2] > 0) and (frame[2] < self.frame_count)):
                self.renderframe(frame, frame_number, "any")
            elif (frame[2] >= self.frame_count):
                current_destparticle = frame[1]
                self.frames_array.pop(frame_number)
                # When the frame is complete look for new dest particle
                #new_frame = (current_destparticle, None, 0)
                #self.frames_array.append(new_frame)
            frame_number += 1
    def updateanomoly2(self, *args):
        # anomolies will attach to particles around it
        for particle1 in self.particle_array:
            if (particle1.isanomoly == True):
                anomolyparticle = particle1
            for particle2 in self.particle_array:
                if ((abs(particle1.y - anomolyparticle.y) <= anomolyparticle.particle_distance) and (abs(particle1.x - anomolyparticle.x) <= anomolyparticle.particle_distance) and (abs(particle2.y - anomolyparticle.y) <= anomolyparticle.particle_distance) and (abs(particle2.x - anomolyparticle.x) <= anomolyparticle.particle_distance)):
                    new_frame = (particle1, particle2, 1)
                    #check_frame = (particle2, particle1, 1)
                    #check_frame_index = -1
                    #try:
                    #    check_frame_index = self.frames_array.index(check_frame) > -1
                    #except:
                    #    check_frame_index = -1
                    #if (check_frame_index >= 0):
                    self.frames_array.append(new_frame)
        frame_number = 0
        for frame in self.frames_array:
            if ((frame[2] == -1) or (frame[0].changeddirection == True)):
                self.frames_array.pop(frame_number)
            elif (frame[2] == 0):
                self.finddestination(frame, frame_number, "any")
            elif ((frame[2] > 0) and (frame[2] < self.frame_count)):
                self.renderframe(frame, frame_number, "any")
            elif (frame[2] >= self.frame_count):
                current_destparticle = frame[1]
                self.frames_array.pop(frame_number)
                # When the frame is complete look for new dest particle
                #new_frame = (current_destparticle, None, 0)
                #self.frames_array.append(new_frame)
            frame_number += 1

    def update(self, *args):
        if (self.currentstyle == 1):
            self.updateanomoly()
        if (self.currentstyle == 2):
            self.updateanomoly2()
        if (self.currentstyle == 3):
            self.updatelinedrop()

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
            gfxdraw.filled_circle(self.surface, particle.x, particle.y, particle.size, particle.color)

    def reset(self, *args):
        particle_number = 1
        for particle_number in range(self.particle_count):
            self.particle_array[particle_number].reset()

    def mousemotion(self, *args):
        self.mouse_x, self.mouse_y = args[0]

    def pause(self, *args):
        self.pausing = not self.pausing
    
    def get_particle_array(self, *args):
        return self.particle_array

class particle_generate_wraparound(particle_generator):
    def __init__(self, surface, particle_count, particle_maxdistancefromother, anomoly_count):
        particle_generator.pausing = False
        particle_generator.surface = surface
        particle_generator.surface_width = surface.get_width()
        particle_generator.surface_height = surface.get_height()
        particle_generator.particle_count = particle_count
        particle_generator.particle_maxdistancefromother = particle_maxdistancefromother
        particle_generator.particle_array = [] # start with an empty list
        particle_generator.anomoly_count = anomoly_count
        self.myparticlemotion = particle_motion_wrapsides()
        particle_number = 1
        for particle_number in range(self.particle_count):
            isAnomoly = False
            if (particle_number < self.anomoly_count):
                isAnomoly = True
            particle_x = random.randint(1, particle_generator.surface_width)
            particle_y = random.randint(1, particle_generator.surface_height)
            particle_radius = random.randint(1, 2)
            particle_vector_x = random.randint(-2, 2)
            particle_vector_y = random.randint(-2, 2)
            while (particle_vector_x == 0):
                particle_vector_x = random.randint(-2, 2)
            while (particle_vector_y == 0):
                particle_vector_y = random.randint(-2, 2)
            particle_color = (int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)))
            myparticle = particle(self.surface_width, self.surface_height, particle_x, particle_y, particle_radius, particle_color, particle_vector_x, particle_vector_y, isAnomoly, self.particle_maxdistancefromother, self.myparticlemotion)

            self.particle_array.append(myparticle) # top of 1st story, upper left
            #if (isAnomoly):
            #    self.anomoly_array.append(myparticle)
    def update(self, *args):
        particle_generator.update(self, *args)
        particle_generator.render(self, *args)

    def reset(self, *args):
        particle_generator.reset(self, *args)
    
    def pause(self, *args):
        particle_generator.pause(self, *args)
    
    def get_particle_array(self, *args):
        particle_generator.get_particle_array(self, *args)

class particle_generate_falling_straight(particle_generator):
    def __init__(self, surface, particle_count, particle_maxdistancefromother, anomoly_count):
        particle_generator.pausing = False
        particle_generator.surface = surface
        particle_generator.surface_width = surface.get_width()
        particle_generator.surface_height = surface.get_height()
        particle_generator.particle_count = particle_count
        particle_generator.particle_maxdistancefromother = particle_maxdistancefromother
        particle_generator.particle_array = [] # start with an empty list
        particle_generator.anomoly_count = anomoly_count
        self.myparticlemotion = particle_motion_down_straight()
        particle_number = 1
        for particle_number in range(self.particle_count):
            isAnomoly = False
            if (particle_number < self.anomoly_count):
                isAnomoly = True
            particle_x = random.randint(1, particle_generator.surface_width)
            particle_y = random.randint(particle_generator.surface_height*-1, 0)
            particle_radius = random.randint(1, 2)
            particle_vector_x = 0
            particle_vector_y = random.randint(1, 4)
            particle_color = (int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)))
            myparticle = particle(self.surface_width, self.surface_height, particle_x, particle_y, particle_radius, particle_color, particle_vector_x, particle_vector_y, isAnomoly, self.particle_maxdistancefromother, self.myparticlemotion)

            self.particle_array.append(myparticle) # top of 1st story, upper left
    def update(self, *args):
        particle_generator.update(self, *args)
        particle_generator.render(self, *args)

    def reset(self, *args):
        particle_generator.reset(self, *args)
    
    def pause(self, *args):
        particle_generator.pause(self, *args)
    
    def get_particle_array(self, *args):
        particle_generator.get_particle_array(self, *args)

class particle_generate_falling_zigzag(particle_generator):
    def __init__(self, surface, particle_count, particle_maxdistancefromother, anomoly_count):
        particle_generator.pausing = False
        particle_generator.surface = surface
        particle_generator.surface_width = surface.get_width()
        particle_generator.surface_height = surface.get_height()
        particle_generator.particle_count = particle_count
        particle_generator.particle_maxdistancefromother = particle_maxdistancefromother
        particle_generator.particle_array = [] # start with an empty list
        particle_generator.anomoly_count = anomoly_count
        self.myparticlemotion = particle_motion_down_zigzag()
        particle_number = 1
        for particle_number in range(self.particle_count):
            isAnomoly = False
            if (particle_number < self.anomoly_count):
                isAnomoly = True
            particle_x = random.randint(1, particle_generator.surface_width)
            particle_y = random.randint(particle_generator.surface_height*-1, 0)
            particle_radius = random.randint(1, 2)
            particle_vector_x = random.randint(-4, 4)
            particle_vector_y = random.randint(1, 6)
            particle_color = (int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)))
            myparticle = particle(self.surface_width, self.surface_height, particle_x, particle_y, particle_radius, particle_color, particle_vector_x, particle_vector_y, isAnomoly, self.particle_maxdistancefromother, self.myparticlemotion)

            self.particle_array.append(myparticle) # top of 1st story, upper left
    def update(self, *args):
        particle_generator.update(self, *args)
        particle_generator.render(self, *args)

    def reset(self, *args):
        particle_generator.reset(self, *args)
    
    def pause(self, *args):
        particle_generator.pause(self, *args)
    
    def get_particle_array(self, *args):
        particle_generator.get_particle_array(self, *args)

class particle_generate_twirl(particle_generator):
    def __init__(self, surface, particle_count, particle_maxdistancefromother, anomoly_count):
        particle_generator.pausing = False
        particle_generator.surface = surface
        particle_generator.surface_width = surface.get_width()
        particle_generator.surface_height = surface.get_height()
        particle_generator.particle_count = 2
        particle_generator.particle_maxdistancefromother = particle_maxdistancefromother
        particle_generator.particle_array = [] # start with an empty list
        particle_generator.anomoly_count = anomoly_count
        self.center_x = int(particle_generator.surface_width/2)
        self.center_y = int(particle_generator.surface_height/2)
        self.myparticlemotion = particle_motion_twirl(self.center_x, self.center_y)
        
        particle_radius = 2
        particle_vector_x = 0
        particle_vector_y = 0
        isAnomoly = False
        particle_x = self.center_x
        particle_color = (int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)))

        particle_y = self.center_y-25
        myparticle = particle(self.surface_width, self.surface_height, particle_x, particle_y, particle_radius, particle_color, particle_vector_x, particle_vector_y, isAnomoly, self.particle_maxdistancefromother, self.myparticlemotion)

        particle_y = self.center_y+25
        myparticle2 = particle(self.surface_width, self.surface_height, particle_x, particle_y, particle_radius, particle_color, particle_vector_x, particle_vector_y, isAnomoly, self.particle_maxdistancefromother, self.myparticlemotion)
        self.particle_array.append(myparticle) # top of 1st story, upper left
        self.particle_array.append(myparticle2) # top of 1st story, upper left

    def update(self, *args):
        particle_generator.update(self, *args)
        particle_generator.render(self, *args)

    def reset(self, *args):
        particle_generator.reset(self, *args)
    
    def pause(self, *args):
        particle_generator.pause(self, *args)
    
    def get_particle_array(self, *args):
        particle_generator.get_particle_array(self, *args)

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
    particle_count = 300
    particle_maxdistancefromother = 100
    particle_anomolycount = 1
    bg_image = pygame.image.load("spacee-740x463.jpg")

    # create a surface on screen that has the size of screen_width x screen_height
    screen = pygame.display.set_mode((screen_width,screen_height))
    myparticle_generator = particle_generate_twirl(screen, particle_count, particle_maxdistancefromother, particle_anomolycount);
    #myparticle_connector = particle_connector(screen, myparticle_generator.get_particle_array());
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
                if event.key == pygame.K_1:
                    myparticle_connector.setstyle(1)
                if event.key == pygame.K_2:
                    myparticle_connector.setstyle(2)
                if event.key == pygame.K_3:
                    myparticle_connector.setstyle(3)

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop1
                running = False
        clock.tick(fps)

        #screen.blit(bg_image, (0, 0))
        screen.fill((0,0,0))
        #myparticle_connector.update()
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