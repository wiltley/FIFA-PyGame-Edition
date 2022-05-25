
import teammate as t, opp as o, player as p

# class that will control most of the game logic
class game:

    current_possession = None
    current_ball_loc = None

    def __init__(self):
        # i guess we declare a new game in here? the official score would be kept in main?

        self.teammates = []
        self.opposition = []


        for i in range(10):
            self.teammates.append(t.teammate(100,200, 0));

        self.player = p.player(self.teammates[0]);

        self.affect_whole_team("argument here")
        
        # initialize player with striker entitity

    # lmao i have absolutely 0 clue if this will work even a little but 
    # defo an interesting idea
    def affect_whole_team(self, argument):
        pass
        #for i in self.teammates:
            #self.teammates[i].eval(argument)

    def switch_possession(self, argument):

        pass

    def get_player(self):
        return self.player

    def update(self):

        self.player.currently_controlled.move()
        # this will update everything







# ideas -
# i think i will split the field into "12" imaginary boxes to calculate  where people should be play

 
