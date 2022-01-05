import json
from game.constants import Tiles
from server import *
from copy import deepcopy

from Engine.server.grid_game import GridGame, GridGameFactory
from Engine.server.grid_game import ClientConnection
from Engine.server.maps import Map
from .unit import *
from .tile import BaseTile
from .move import *
from game.constants import Units
from game.constants import Direction
from game.constants import MINING_REWARDS
from game.constants import TURNS_PER_PLAYER

class MerlinGridGame(GridGame):
    """
    GridGame is the currently running game, it controls all game state and updates the state each turn with tick.
    
    This game is won by a player capturing the other player's flag
    
    """
    def __init__(self, player_one_connection:ClientConnection, player_two_connection:ClientConnection, gamemap:Map):
        super().__init__(player_one_connection, player_two_connection, gamemap)
        self.turns = 0
        self.totalTurns = TURNS_PER_PLAYER*2
        self.p1_flag = {}
        self.p2_flag = {}
        self.unitFactory = UnitFactory()
        # Make team's initial units
        for row in range(len(self.grid)):
            for col in range(len(row)):
                tile = self.top[row][col]
                if isinstance(tile, BaseTile):
                    if row < len(self.grid)/2:
                        unit = self.unitFactory(Units.WORKER, row, col, 0)
                        self.add_unit(self.p1_units, unit)
                    else:
                        unit = self.unitFactory(Units.WORKER, row, col, 0)
                        self.add_unit(self.p2_units, unit)
        for row in range(len(self.grid)):
            for col in range(len(row)):
                tile = self.top[row][col]
                if isinstance(tile, BaseTile):
                    if row < len(self.grid)/2:
                        self.setFlag(self.p1_flag, col, row)
                    else:
                        self.setFlag(self.p2_flag, col, row)

    def setFlag(self, player_flag, x, y):
        player_flag['x'] = x
        player_flag['y'] = y

    def verify_move(self, k:int, v:Move, player_state, player_resources, enemy_units, moved_units):
        
        if k not in player_state:
            print('ERROR: Cannot move enemy unit: {}'.format(k))
            return False
        unit = player_state[k]
        #Checks if unit is currently doing something preventing them from moving
        if isinstance(unit, Unit):
            if isinstance(v, MineMove):
                if v.verifyMove(self.grid):
                    moved_units.add(unit.id)
                    return True
                else:
                    return False
            elif isinstance(v, BuyMove):
                if v.verifyMove(self.grid, player_resources):
                    moved_units.add(unit.id)
                    return True
                else:
                    return False
            elif isinstance(v, CaptureMove):

                    if v.verifyMove(self.all_units, ):
                        moved_units.add(unit.id)
                        return True
                    else:
                        return False
            elif isinstance(v, DirectionMove):
                    if v.verifyMove(self.grid, self.all_units):
                        moved_units.add(unit.id)
                        return True
                    else:
                        return False
            elif isinstance(v, AttackMove):
                    if v.verifyMove(self.all_units):
                        moved_units.add(unit.id)
                        return True
                    else:
                        return False
            elif isinstance(v, UpgradeMove):
                    if v.verifyMove(self.grid):
                        moved_units.add(unit.id)
                        return True
                    else:
                        return False
        return False

    def get_matching_unit(self, x, y, attack):
        pass
        # rx, ry = attack.get_relative_moves()

        # x += rx
        # y += ry

        # return self.all_units.get('{},{}'.format(x, y), None)

    def get_direction_change(self, direction):
        x = 0
        y = 0
        if direction == Direction.UP:
            y = 1
        elif direction == Direction.Down:
            y = -1
        elif direction == Direction.Left:
            x = -1
        elif direction == Direction.Right:
            x = 1
        return x,y

    def get_relative_location(self, x, y, direction):

        rx, ry = self.get_direction_change(direction)

        x += rx
        y += ry
        return x,y

        # return self.all_units.get('{},{}'.format(x, y), None)
    def make_move(self, k, v, player_state, player_name, opponent_state):
        pass
        # if isinstance(v, GroundMove):
        #     m = v.get_relative_moves()
        #     x, y = player_state[k].pos_tuple()
        #     player_state[k].set_relative_location(self.all_units, *m)
        #     self.move_unit(x, y, player_state[k])
        # elif isinstance(v, AttackMove):
        #     x, y = player_state[k].pos_tuple()
        #     rx, ry = v.get_relative_moves()
        #     uid = str(self.get_unit(x+rx, y+ry).id)
        #     try:
        #         del opponent_state[uid]
        #     except KeyError:
        #         # User tried to delete their own unit
        #         pass

        #     self.del_unit(x+rx, y+ry)
        # elif isinstance(v, StasisMove):
        #     self.currently_duplicating[k] = (
        #         player_state, player_state[k].start_duplication(v.direction, v.unit_type))
        #     if v.unit_type == MELEE_UNIT:
        #         self.resources[player_name] -= player_state[k].melee_cost
        #     else:
        #         self.resources[player_name] -= player_state[k].worker_cost
        # elif isinstance(v, MineMove):
        #     self.currently_mining[k] = (
        #         player_name, player_state[k].start_mining())
        # elif isinstance(v, StunMove):
        #     x, y = player_state[k].pos_tuple()
        #     rx, ry = v.get_relative_moves()
        #     uid = str(self.get_unit(x+rx, y+ry).id)
        #     try:
        #         self.currently_stunned[k] = (player_name, opponent_state[uid].stun())
        #         self.resources[player_name] -= player_state[k].stun_cost
        #     except:
        #         pass


    def json_str(self):
        display = deepcopy(self.grid)
        for u in self.p1_units.values():
            display[u.y][u.x] = u
        for u in self.p2_units.values():
            display[u.y][u.x] = u.string().upper()
        print(display)
        def inner(r): return '[{}]'.format(
            ','.join(map(lambda x: (x if isinstance(x, str) else x.string()), r)))
        return '[{}]'.format(','.join(map(inner, display)))

    def print_map(self, p1_name, p2_name):
        j = json.dumps({
            'map': self.json_str(),
            'p1_resources': self.resources[p1_name],
            'p2_resources': self.resources[p2_name]
        })
        print('MAP:{}'.format(j))

    def get_state(self):
        return self.grid, self.all_units, self.resources

    def getWinner(self):
        return None

    def tick_player(self, conn, current, opponent, name, turns):
        #Gets a list of moves from the player
        misc = {"your_flag": {},
                "enemy_flag": {}
        }

        if name  == self.p1_conn.name:
            misc = {"your_flag":self.p1_flag,
                    "enemy_flag":self.p2_flag
            }
        else:
            misc = {"your_flag":self.p2_flag,
                    "enemy_flag":self.p1_flag
            }
        moves = conn.tick(self, current, opponent, self.resources, turns, misc)

        moved_units = {} # id to n number of moves
        #Goes through each given move and verifies it is valid. If it is execute it.
        for m in moves:
            unit_id, move_object = m
            # Key is unit id , value is move arguments
            if self.verify_move(unit_id, move_object, current, self.resources[name], opponent, moved_units):
                self.make_move(unit_id, move_object, current, name, opponent)

    # Creates the workers desired duplicate at a given tile.
    def create_duplicate(self,unit:WorkerUnit):
        location = self.get_relative_location(*unit.pos_tuple(), unit.action_direction)
        return self.unitFactory.createUnit(unit.duplicating_to_type, *location) # TODO finish directional spawning.


    #tick is run each turn and updates the game state
    def tick(self):
        # manage each units actions that change game state overall.
        #Checks if any units are duplicating, if they are increment the status and create a new unit if they are complete
        for unit in self.all_units:
            player = self.get_unit_player()
            if isinstance(unit, WorkerUnit) and unit.is_duplicating():
                unit.duplication_status -= 1
                location = self.get_relative_location(*unit.pos_tuple(), unit.action_direction)
                if unit.duplication_status <= 0 and not self.has_unit(*location):
                    self.add_unit(player, self.create_duplicate(unit))
                    unit.finish_duplicating()

        #Checks if any units are mining, if they are increment the status and add resources if they complete
        for unit in self.all_units:
            player_name = self.get_unit_player_name(unit)
            if isinstance(unit, WorkerUnit) and unit.is_mining():
                unit.mining_status -= 1
                if unit.mining_status == 0:
                    unit.mining_status = -1
                    tile = self.get_tile(unit)
                    self.resources[player_name] += MINING_REWARDS[str(tile)]

        #Gets the moves from each player and executes.
        if self.turns % 2 == 0:
            print("tick 1")
            self.tick_player(self.p1_conn, self.p1_units,
                         self.p2_units, self.p1_conn.name, self.turns)
            self.print_map(self.p1_conn.name, self.p2_conn.name)
        else:
            print("Tick 2")
            self.tick_player(self.p2_conn, self.p2_units,
                            self.p1_units, self.p2_conn.name, self.turns)
            self.print_map(self.p1_conn.name, self.p2_conn.name)
        self.turns += 1

class MerlinGridGameFactory(GridGameFactory):
    def getGame(self, connections, map)->MerlinGridGame:
        return MerlinGridGame(*connections, map)