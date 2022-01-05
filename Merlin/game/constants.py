from enum import Enum

TURNS_PER_PLAYER = 200
#Represents all the valid moves a player can make
class Moves(Enum):
    ATTACK = 1
    UPGRADE = 2
    DIRECTION = 3
    MINE = 4
    BUY = 5
    CAPTURE = 6

#Represents all units in the game
class Units(Enum):
    WORKER = 1
    SCOUT = 2
    KNIGHT = 3
    ARCHER = 4

class Tiles(Enum):
    GROUND = ' ' # A walkable tile
    WALL = 'X' # A non-walkable tile
    GOLD = 'G' # A gold resource tile, check manual for worth when mined.
    SILVER = 'S'# A silver resource tile, check manual for worth ehwn mined.
    COPPER = 'C' # A copper resource tile, check manual for worth ehwn mined.
    BASE = 'B' # A team's base

# Direction holds string values for each cardinal direction on the board
class Direction(Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'

UPGRADE_COSTS = {
  Units.WORKER: {0:10,
                1:50,
                2:30,
                3:40
                },
  Units.SCOUT: {},
  Units.KNIGHT: {},
  Units.ARCHER: {}
}

MINING_REWARDS = {
    Tiles.GOLD: 75,
    Tiles.SILVER: 75,
    Tiles.COPPER: 75
}
