
import teammate as t, opp as o, player as p, ball as b

# class that will control most of the game logic
class game:

    current_possession = None

    def __init__(self):
        # i guess we declare a new game in here? the official score would be kept in main?

        self.ball = b.ball(200,200)

        self.teammates = []
        self.opposition = []


        for i in range(10):
            self.teammates.append(t.teammate([100,200], 0));

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


    def switch_to(self):
        # when the space key is hit, it should change the player to the optimal defender
        # should also automatically switch to whoever  your team passed to

        # later on add sum that accounts for a "side switch"

        if(self.teammates[0].goal_side == "right"):
            #initialize accordingly
            pass

        # stuff here will be changed to variables eventually


    """
    HEAVY WORK IN PROGRESS FUNCTION, SOURCE FOR BREAKAGE
    """
    def find_best_defender(self):
        search = []
        for t in self.teammates:
            # this line should be determined a diff way, based on the direction being defended 
            if t.pos[0] > self.ball.pos[0]:
                search.append(t)

        # quicksort based off of their distance from the ball
        for o in search:
            pass
            # we will sort them by distance, above the player will have a hotkey to indicate which to switch to 

            pass

    def update(self):

        self.player.currently_controlled.move()
        # this will update everything







# ideas -
# i think i will split the field into "12" imaginary boxes to calculate  where people should be play

 
