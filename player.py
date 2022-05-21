class player:

    has_pos = False;
    speed = 12;

    # this will be the current entity to manipulate
    currently_controlled = None;


    def __init__(self, entity):

        self.currently_controlled = entity
        # entity

        pass

    # need to figure out what determines them gaining possesion
    def gained_possesion(self):

        # need a check to see if its a cpu that got the ball and not the player
        self.speed = 10

    def move_around(self):

        # need to directly alter the currentlly controlled entity
        #still not sure if the ball should be its own entity
        pass

    def boost(self):
        self.speed = 12


