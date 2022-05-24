import player as p, pygame, character as c

class teammate(c.character):

    entity = pygame.image.load("")

    # not sure if get_rect is the correct thing we want
    # either way, each player is gonna have a like, an invisible circle under them

    bounds = entity.get_rect()

    team_has_pos = False
    position = None

    cpu = True
    entity = None

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
        self.cpu = False

        # return the entity

    def eval(self, argument):
        argument()










        
