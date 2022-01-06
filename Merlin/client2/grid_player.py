#from helper_classes import *
from game.constants import *

class GridPlayer:

    def __init__(self):
        self.foo = True
        self.count = 0
    def tick(self, game_map, your_units, enemy_units, resources,turns_left, your_flag, enemy_flag):
             #Task, the player codes this
        self.count += 1
        print("turn taken: ", self.count)
        return []
