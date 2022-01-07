from .helper_classes import *
from game.constants import *
from typing import List
class GridPlayer:

    def __init__(self):
        self.foo = True
        self.count = 0

    def tick(self, game_map:Map, your_units:Units, enemy_units:Units, resources:int,turns_left:int, your_flag:dict, enemy_flag:dict):
             #Task, the player codes this
        self.count += 1
        my_workers = your_units.get_all_unit_of_type(Units.WORKER)
        return [createDirectionMove(my_workers[0].id, Direction.UP, 1)]
