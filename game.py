
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


        # initialize player with striker entitity




# ideas -
# i think i will split the field into "12" imaginary boxes to calculate  where people should be play

 
