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
        my_archers = your_units.get_all_unit_of_type(Units.ARCHER)

        if len(my_workers) < 2:
            # buy worker until have 2 workers.
            moves.append(createBuyMove(my_workers[0].id, Units.WORKER, Direction.LEFT))
        else:
            # miner moves
            miner = my_workers[1]
            loc_nearest_copper = game_map.closest_tile_of_type(miner, Tiles.COPPER)
            miner_pos = miner.position() # returns x, y. Otherwise known as col, row
            start = miner_pos
            dir_nearest_copper = game_map.bfs(start,(loc_nearest_copper[0],loc_nearest_copper[1]))
            if dir_nearest_copper:
                moves.append(createDirectionMove(miner.id, direction_to(miner, dir_nearest_copper[1:][0]), 1))
            else:
                moves.append(createMineMove(miner.id))
            # Spawner creates units
            spawner = my_workers[0]
            if len(my_scouts) < 2:
                moves.append(createBuyMove(spawner.id, Units.SCOUT, Direction.UP))
            elif len(my_knights) < 1:
                moves.append(createBuyMove(spawner.id, Units.KNIGHT, Direction.LEFT))
            elif len(my_archers) < 1:
                moves.append(createBuyMove(spawner.id, Units.ARCHER, Direction.RIGHT))
            else:
                moves.append(createDirectionMove(spawner.id, get_random_direction(), 1))
        if len(my_scouts) >= 1:
            scout = my_scouts[0]
            if not does_have_flag(scout): # Note only scouts can hold the flag.
                loc_flag = get_flag_pos(enemy_flag)
                flag_path = game_map.bfs(scout.position(),loc_flag)
                flag_dir = direction_to(scout, flag_path[1]) # Direction for the next best move
                if len(flag_path) >=2: # Check if adjacent. Can only capture in a direction.
                    moves.append(createCaptureMove(scout.id, flag_dir))
                moves.append(createDirectionMove(scout.id, flag_dir, 1))
            else:
                loc_flag = get_flag_pos(your_flag)
                flag_path = game_map.bfs(scout.position(),loc_flag)
                flag_dir = direction_to(scout, flag_path[1])
                moves.append(createDirectionMove(scout.id, flag_dir, 1))
        if len(my_scouts) > 1:
            # Randomly exploring scout,might get in the way might not.
            moves.append(createDirectionMove(my_scouts[1].id, get_random_direction(), 1))

        if len(my_knights) >= 1:
            hunter = my_knights[0]
            if hunter.level < 3:
                moves.append(createUpgradeMove(hunter.id))
            else:
                if len(enemy_units.get_all_unit_ids()) >= 1:
                    prey_pos = enemy_units.get_unit(enemy_units.get_all_unit_ids()[0]).position()
                    prey_path = game_map.bfs(hunter.position(),prey_pos)
                    prey_dir = direction_to(hunter, prey_path[1]) # Direction for the next best move
                    if len(prey_path) >=2: # Check if adjacent. Can only capture in a direction.
                        moves.append(createAttackMove(hunter.id, prey_dir, 1))
                    moves.append(createDirectionMove(hunter.id, prey_dir, 1))
                else:
                    moves.append(createDirectionMove(hunter.id, get_random_direction(), 2))
        if len(my_archers) >= 1:
            hunter = my_archers[0]
            if len(enemy_units.get_all_unit_ids()) >= 1:
                prey_pos = enemy_units.get_unit(enemy_units.get_all_unit_ids()[0]).position()
                prey_path = game_map.bfs(hunter.position(),prey_pos)
                prey_dir = direction_to(hunter, prey_path[1]) # Direction for the next best move

                if len(prey_path) >=2: # Check if adjacent. Can only capture in a direction.
                    moves.append(createAttackMove(hunter.id, prey_dir, 1))
                moves.append(createDirectionMove(hunter.id, prey_dir, 1))
            else:
                moves.append(createDirectionMove(hunter.id, get_random_direction(), 2))
            # Note knights can move up to two tiles, new algorithms must be made to account for this.
        return moves

