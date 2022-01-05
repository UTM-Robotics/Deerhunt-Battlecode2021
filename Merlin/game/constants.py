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

class Tiles():
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

# 0 represents cost to buy, anything above represents cost to upgrade
UPGRADE_COSTS = {
  Units.WORKER: {
    0:10,
    1:50,
    2:30,
    3:40
    },
  Units.SCOUT: {
      0:10,
      1:50,
      2:30,
      3:40
  },
  Units.KNIGHT: {
    0:10,
    1:50,
    2:30,
    3:40
  },
  Units.ARCHER: {
    0:10,
    1:50,
    2:30,
    3:40
  }
}
 # unittype to 
ATTACK_DAMAGE = {
  Units.WORKER: {
    0:10,
    1:50,
    2:30,
    3:40
    },
  Units.SCOUT: {
      0:10,
      1:50,
      2:30,
      3:40
  },
  Units.KNIGHT: {
    0:10,
    1:50,
    2:30,
    3:40
  },
  Units.ARCHER: {
    0:10,
    1:50,
    2:30,
    3:40
  }
}


MAX_LEVEL = 3

MAX_ATTACK_RANGE = {
    Units.ARCHER: 2,
    Units.WORKER: 0,
    Units.SCOUT: 1,
    Units.KNIGHT: 1
}

MINING_REWARDS = {
    Tiles.GOLD: 75,
    Tiles.SILVER: 75,
    Tiles.COPPER: 75
}
MINING_TIME = 3 # One of your turns, one of the enemies turns.

DUPLICATION_TIME = 3  # One of your turns, one of the enemies turns.
