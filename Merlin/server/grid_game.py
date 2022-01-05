import json
from server import *
from copy import deepcopy

from Engine.server.grid_game import GridGame, GridGameFactory



class MerlinGridGame(GridGame):
    """
    GridGame is the currently running game, it controls all game state and updates the state each turn with tick.
    """

    def verify_move(self, k, v, player_state, player_resources, enemy_units, moved_units):
        pass
        # if k not in player_state:
        #     print('ERROR: Cannot move enemy unit: {}'.format(k))
        #     return False

        # #Checks if unit is currently doing something preventing them from moving
        # if isinstance(player_state[k], Unit):
        #     if player_state[k].is_duplicating():
        #         print('ERROR: {} cannot act while duplicating'.format(k))
        #         return False

        #     if player_state[k].is_mining():
        #         print('ERROR: {} cannot act while mining'.format(k))
        #         return False

        #     if player_state[k].is_stunned():
        #         print('ERROR: {} cannot act while stunned'.format(k))
        #         return False

        #     if k in moved_units:
        #         print('ERROR: Cannot make multiple actions for unit {}'.format(k))
        #         return False

        #     moved_units.add(k)

        # x, y = player_state[k].pos_tuple()

        # #Checks if the arguments for each move is valid
        # if isinstance(v, GroundMove) and (not v.valid_path(self.grid, self.all_units, x, y) or v.len() < 0 or v.len() > 1):
        #     print('ERROR: Invalid path for unit {}'.format(k))
        #     return False
        # elif isinstance(v, AttackMove) and (self.get_matching_unit(x, y, v) is None or v.len() < 0 or v.len() > 1):
        #     print('ERROR: Unit {} cannot attack there'.format(k))
        #     return False
        # elif isinstance(v, StunMove):
        #     if not player_state[k].can_stun(player_resources):
        #         print("ERROR: Unit {} not enough resources to stun".format(k))
        #         return False
        #     if self.get_matching_unit(x, y, v) is None or (v.len() < 0) or (v.len() > 2):
        #         print('ERROR: Unit {} cannot stun there'.format(k))
        #         return False
        # elif isinstance(v, StasisMove) and (not player_state[k].can_duplicate(player_resources, v.unit_type)
        #                                     or not v.free_spot(x, y, self.all_units, self.grid)):
        #     print('ERROR: Unit {} cannot duplicate now'.format(k))
        #     return False
        # elif isinstance(v, MineMove) and (not player_state[k].can_mine() or not self.is_mining_resource(x, y)):
        #     print('ERROR: Unit {} cannot mine now'.format(k))
        #     return False

        # return True

    def is_mining_resource(self, x, y):
        pass
        # return isinstance(self.grid[y][x], ResourceTile)

    def get_matching_unit(self, x, y, attack):
        pass
        # rx, ry = attack.get_relative_moves()

        # x += rx
        # y += ry

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
        pass
        # #Gets a list of moves from the player
        # moves = conn.tick(self, current, opponent, self.resources, turns)

        # moved_units = set()
        # #Goes through each given move and verifies it is valid. If it is execute it.
        # for m in moves:
        #     k, v = m
        #     if self.verify_move(k, v, current, self.resources[name], opponent, moved_units):
        #         self.make_move(k, v, current, name, opponent)


    #tick is run each turn and updates the game state
    def tick(self):
        turns = 0
        #Checks if any units are duplicating, if they are increment the status and create a new unit if they are complete
        # for k, (player, unit) in list(self.currently_duplicating.items()):
        #     unit.duplication_status -= 1
        #     if unit.duplication_status == 0:
        #         del self.currently_duplicating[k]
        #         if self.can_duplicate_to(unit):
        #             self.add_unit(player, self.create_duplicate(unit))

        # #Checks if any units are mining, if they are increment the status and add resources if they complete
        # for k, (p_name, unit) in list(self.currently_mining.items()):
        #     unit.mining_status -= 1
        #     if unit.mining_status == 0:
        #         del self.currently_mining[k]
        #         self.resources[p_name] += 75

        # #Checks if any units are stunned, if they are increment the status
        # for k, (player, unit) in list(self.currently_stunned.items()):
        #     unit.stun_status -= 1
        #     if unit.stun_status == 0:
        #         del self.currently_stunned[k]

        #Gets the moves from each player and executes.
        self.tick_player(self.p1_conn, self.p1_units,
                         self.p2_units, self.p1_conn.name, turns)
        #self.print_map(self.p1_conn.name, self.p2_conn.name)

        if len(self.p2_units) == 0:
            return self.p1_conn.name

        self.tick_player(self.p2_conn, self.p2_units,
                         self.p1_units, self.p2_conn.name, turns)
        #self.print_map(self.p1_conn.name, self.p2_conn.name)

        if len(self.p1_units) == 0:
            return self.p2_conn.name


class MerlinGridGameFactory(GridGameFactory):
    def getGame(self, connections, map)->MerlinGridGame:
        return MerlinGridGame(*connections, map)