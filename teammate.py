import player as p, pygame, character as c, game as g

class teammate(c.character):


    # not sure if get_rect is the correct thing we want
    # either way, each player is gonna have a like, an invisible circle under them

    team_has_pos = False
    role = None

    cpu = True

    def __init__(self, pos, face_vector):

        animations = [["./assets/up4.png", "./assets/up3.png", "./assets/up2.png","./assets/up1.png", "./assets/up0.png"],[],[],[],
                ["./assets/down4.png", "./assets/down3.png", "./assets/down2.png","./assets/down1.png", "./assets/down0.png"]]

        self.entity = pygame.image.load("./assets/up4.png")
        self.entity_rect = self.entity.get_rect()
        c.character.__init__(self, pos, face_vector, animations,self.entity,self.entity_rect)
        self.goal_side = "right"

    def defence(self):

        # controls the general logic of where they want to be
        # need to figure out how i want to make them "follow" someone on the other team

        if(self.role == "striker"):

            # make be the furthest one pushed up
            pass

        elif(self.role == "midfielder"):
            pass

        elif(self.role == "defender"):
            pass


    def offense(self):

        if(self.role == "striker"):
            # logic for what a striker not controlled by the computer would do
            pass


        elif(self.role == "midfielder"):
            pass

        elif(self.role == "defender"):

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

    #def eval(self, argument):
    #    argument()


    def get_entity(self):
        return self.entity








        
