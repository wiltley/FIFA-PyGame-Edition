import pygame

# both teammate and opp will inherit from this class

class character:


    acceleration = 0


    # some state variables
    is_running = False

    # char speed (same signage as a graph)

    speed = 0


    # vector
    face_vector = 0

    # animations
    
    animations = []
    animation_index = 0

    # relates to the animation translations
    # i dont want it to just immediately slow down

    frames_since_last_input = 0

    def __init__(self, pos, face_vector, animations, entity, entity_rect):

        self.pos = pos
        self.face_vector = face_vector
        self.animations = animations
        self.entity = entity
        self.entity_rect = entity_rect
        self.moving = False
        self.vel = [0,0, self.acceleration]


    def change_direction(self):

        # not only should this change the idle facing direction, but it should
        # load the running animation for said direction
        # need to figure out how ill code the (gap in phases, i guess ill do something
        # where i check how many frames have gone by or sum)
        pass

    def move(self):
        # make it so that once it passes a certain animation, is running becomes true
        # then the speed increases

        if (self.moving): 
            self.animation_frame_manager()

            if self.face_vector == 0:
                pass

            elif self.face_vector == 1:
                pass


            elif self.face_vector == 2:
                pass

            elif self.face_vector == 3:

                pass


            elif self.face_vector == 4:

                pass

            elif self.face_vector == 5:

                pass


            elif self.face_vector == 6:

                pass

            elif self.face_vector == 7:

                pass
                
        else:
            self.entity = pygame.image.load(self.animations[self.face_vector][0])


            
        self.check_if_running()

    # implement something which checks if they currently have possesion of the ball
    def check_if_running(self):
        if self.animation_index > 3:
            self.speed = 12

    def animation_frame_manager(self):

        # basic animation 

        self.animation_index+=1

        if(self.animation_index == 4):
            self.animation_index = 0

        if(self.face_vector == 0):
            self.entity = pygame.image.load(self.animations[0][self.animation_index])

        if(self.face_vector ==4):
            self.entity = pygame.image.load(self.animations[4][self.animation_index])

