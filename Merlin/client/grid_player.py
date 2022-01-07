from .helper_classes import *
from game.constants import *
from typing import List
class GridPlayer:

    def __init__(self):
        self.foo = True # You can initialize your stuff here if you need information to withstand ticks.
        self.count = 0
        self.base_coords = None

    def tick(self, game_map:Map, your_units:Units, enemy_units:Units, resources:int,turns_left:int, your_flag:dict, enemy_flag:dict):
             #Task, the player codes this
        
        if self.count in [0,1]:
            self.starter_unit = your_units.get_all_unit_of_type(Units.WORKER)[0]
            self.base_coords = self.starter_unit.position()
        moves = []
        self.count += 1
        my_workers = your_units.get_all_unit_of_type(Units.WORKER)
        my_scouts = your_units.get_all_unit_of_type(Units.SCOUT)
        my_knights = your_units.get_all_unit_of_type(Units.KNIGHT)

        if len(my_workers) < 2:
            # buy worker until have 2 workers.
            moves.append(createBuyMove(my_workers[0].id, Units.WORKER, Direction.LEFT))
        else:
            # miner moves
            miner = my_workers[0]
            loc_nearest_gold = game_map.closest_tile_of_type(miner, Tiles.GOLD)
            print("closest of type ran")
            miner_pos = miner.position() # returns x, y. Otherwise known as col, row
            # Past this is broken, written as examples.
            dir_nearest_gold = game_map.bfs((miner_pos[1],miner_pos[0]),(loc_nearest_gold[1],loc_nearest_gold[0]))
            print(dir_nearest_gold)
            moves.append(createDirectionMove(miner.id, dir_nearest_gold, 1))
            spawner = my_workers[1]
            if len(my_scouts) < 2:
                moves.append(createBuyMove(spawner.id, Units.SCOUT, Direction.LEFT))
            elif len(my_knights) < 2:
                moves.append(createBuyMove(spawner.id, Units.KNIGHT, Direction.LEFT))
            else:
                moves.append(createBuyMove(spawner.id, Units.ARCHER, Direction.LEFT))

        if len(my_scouts) >= 1:
            scout = my_scouts[0]
            loc_flag = get_flag_pos(enemy_flag)
            dir_nearest_gold = game_map.bfs(scout.position(),loc_flag)[0]
            moves.append(createDirectionMove(scout.id, Direction.GOLD, 1))
            # Note scouts can move more than one, new algorithms must be made to account for this.

        return moves

