

# both teammate and opp will inherit from this class

class character:

    # cpu bounds

    # positions on the field

    x_position = 0
    y_position = 0

    # some state variables
    is_running = False

    # char speed (same signage as a graph)

    x_velocity = 0 
    y_velocity = 0

    speed = 0

    # vector
    face_vector = 0

    # animations

    up_left_a = [] # fv 0
    up_a = []   # fv 1
    up_right_a = [] # fv 2
    right_a = []    # fv 3
    down_right_a = []   # fv 4
    down_a = [] # fv 5
    down_left_a = []    # fv 6
    left_a = [] # fv 7

    animation_index = 0

    # relates to the animation translations
    # i dont want it to just immediately slow down

    frames_since_last_input = 0

    def __init__(self, x_position, y_position, face_vector, animations):

        self.x_position = x_position
        self.y_position = y_position
        self.face_vector = face_vector

        self.up_a = animations


    def change_direction(self):

        # not only should this change the idle facing direction, but it should
        # load the running animation for said direction
        # need to figure out how ill code the (gap in phases, i guess ill do something
        # where i check how many frames have gone by or sum)
        pass

    def move(self):

        # make it so that once it passes a certain animation, is running becomes true
        # then the speed increases

        self.animation_frame_manager()
        
        if self.face_vector == 0:

            self.y_velocity = self.speed
            self.y_position += self.y_velocity
            self.animation_index

        elif self.face_vector == 1:
            self.y_velocity = self.speed
            self.y_position += self.y_velocity

            self.x_velocity = self.speed
            self.x_position += self.x_velocity

        elif self.face_vector == 2:
            self.y_velocity = self.speed
            self.y_position += self.y_velocity

        elif self.face_vector == 3:

            self.y_velocity = self.speed
            self.y_position -= self.y_velocity

            self.x_velocity = self.speed
            self.x_position += self.x_velocity

        elif self.face_vector == 4:

            self.y_velocity = self.speed
            self.y_position -= self.y_velocity

        elif self.face_vector == 5:

            self.y_velocity = self.speed
            self.y_position -= self.y_velocity

            self.x_velocity = self.speed
            self.x_position -= self.x_velocity

        elif self.face_vector == 6:

            self.x_velocity = self.speed
            self.x_position -= self.x_velocity

        elif self.face_vector == 7:

            self.y_velocity = self.speed
            self.y_position += self.y_velocity
            
            self.x_velocity = self.speed
            self.x_position -= self.x_velocity
        
        self.check_if_running()

    # implement something which checks if they currently have possesion of the ball
    def check_if_running(self):
        if self.animation_index > 3:
            self.speed = 12

    def animation_frame_manager(self):

        # basic animation 

        self.animation_index+=1

        if(self.animation_index == 8):
            self.animation_index = 0

        # what to do in case







