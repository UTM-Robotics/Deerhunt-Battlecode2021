from enum import Enum

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

# Direction holds string values for each cardinal direction on the board
class Direction(Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'

