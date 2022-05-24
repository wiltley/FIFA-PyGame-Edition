
import teammate as t, opp as o, player as p

# class that will control most of the game logic

class game:

    current_possession = None
    current_ball_loc = None
    player = None

    

    def init(self):
        # i guess we declare a new game in here? the official score would be kept in main?

        self.teammates = []
        self.opposition = []

        for i in range(10):
            self.teammates[i] = t.teammate("striker");

        self.player = p.player(self.teammates[0].entity);

        self.affect_whole_team("argument here")



        # initialize player with striker entitity

    # lmao i have absolutely 0 clue if this will work even a little but 
    # defo an interesting idea
    def affect_whole_team(self, argument):
        for i in self.teammates:
            self.teammates[i].eval(argument)






# ideas -
# i think i will split the field into "12" imaginary boxes to calculate  where people should be play

 
