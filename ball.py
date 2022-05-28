import math

class ball:

    pos = []
    velocity = 0

    # eventually ill make the ball deccelerate due to friction, not for now tho

    # dir is going to be a vector

    dir = 0

    def __init__(self, x, y):
        self.pos = [x,y]


    # i think roll is also gonna take care of how the ball slows down

    # mouse assisted pass
    def raw_pass(self):
         

        pass

    def propulse(self, dir, velocity):


        # gonna have to be calculated using angles
        # this angle will also be used to determine the "rotation" of the ball image
        pass


    # just realized this may or may not require differential calculus so imma worry about it later
    def auto_pass(self, sender, receiver):

        pos_s = sender.pos
        pos_r = receiver.pos

        vel_s = sender.vel
        vel_r = receiver.vel

        # were going to calculate the velocity to launch the based, based off the angle
        # determined by the positions

        net_vel = [vel_s[0] - vel_r[0], vel_s[1] - vel_r[1]]
        net_pos = [pos_s[0] - pos_r[0], pos_s[1] - pos_r[1]]


        # to calculate tan, were going to do the y/x since it seems more natural

        constructed_angle = math.atan(net_pos[1]/net_pos[0])


    def distance_from_ball(self, who):
        pos_w = who.pos
        net_pos = [pos_w[0] - self.pos[0], pos_w[1] - self.pos[1]]

        return math.atan(net_pos[1]/net_pos[0])


    # the ball needs to be able to be "loose"
    # otherwise when someone has possession of it, it needs to stick on to them
