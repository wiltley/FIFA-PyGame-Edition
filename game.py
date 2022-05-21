
import teammate as t, opp

# class that will control most of the game logic

class game:

    teammates = []
    opposition = []

    def init(self):
        # i guess we declare a new game in here? the official score would be kept in main?
        for i in range(10):
            self.teammates[i] = t.teammate("striker");

 
