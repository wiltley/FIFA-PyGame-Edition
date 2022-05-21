import player as p

class teammate:

    team_has_pos = False
    position = None
    cpu = True

    def __init__(self, position):
        self.position = position

    def defence(self):

        # controls the general logic of where they want to be
        # need to figure out how i want to make them "follow" someone on the other team
        if(self.position == "striker"):

            # make be the furthest one pushed up
            pass

        elif(self.position == "midfielder"):
            pass

        elif(self.position == "defender"):
            pass


    def offense(self):

        if(self.position == "striker"):
            # logic for what a striker not controlled by the computer would do
            pass

        elif(self.position == "midfielder"):
            pass

        elif(self.position == "defender"):

            pass

    def attempt(self, steal_chance, opp):

        """
        do a random change thing and if it works call
        if(stolen())
        """

        # compare positions
        # ideally i wouldnt have to compare the positions of everyone and everything, id just compare them
        # based on whether or not they are even in the same split
        # i can probably make a simple algorithm for that
        pass

    def stolen(self):

        # if cpu managed to steal the ball
        cpu = False

        # return the entity





        
