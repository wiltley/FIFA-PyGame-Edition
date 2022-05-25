import teammate

class player:

    has_pos = False;
    speed = 12;

    def __init__(self, starter):

        self.currently_controlled = starter
        self.moving = False

        # entity

    # need to figure out what determines them gaining possesion
    def gained_possesion(self, entity):
        #entity is who im supposed to be controlling
        self.currently_controlled = entity

        # need a check to see if its a cpu that got the ball and not the player
        self.has_pos = True
        self.speed = 10

    def move_around(self, input):

        if(input == "w"):
            self.currently_controlled.face_vector = 0
            self.currently_controlled.moving = True

        if(input == "a"):
            pass

        elif(input == "s"):
            pass

        elif(input == "a"):
            pass

        # need to directly alter the currentlly controlled entity
        #still not sure if the ball should be its own entity
        pass

    def boost(self):
        self.speed = 12


    def switched_controlled(self, new_teammate):
        self.currently_controlled.cpu = True 
        self.currently_controlled = new_teammate
        self.currently_controlled.cpu = False





