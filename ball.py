class ball:

    pos = []
    velocity = 0



    # dir is going to be a vector

    dir = 0

    def __init__(self, x, y):
        self.pos = [x,y]


    # i think roll is also gonna take care of how the ball slows down

    def roll(self,velocity):
        pass


    # the ball needs to be able to be "loose"
    # otherwise when someone has possession of it, it needs to stick on to them
