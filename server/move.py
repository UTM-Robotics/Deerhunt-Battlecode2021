
#### GAME ENGINE CODE
### MOVE
# transform -> (x,y,direction,magnitude), direction can be game specific [abstract]
# serialize -> ()
# isValid -> ()

#### GAME SPECIFIC CODE
#A list of valid moves
#Factory for creating moves -> given a moveset, create a move
### GAME-MOVE  
#transform -> import from GAME ENGINE MOVE, transforms based on direction
#serialize -> (), return a string version of the move, the subClass should implemenet this
# isValid -> (game state) check to see if this is a valid move, the subClass should implement this

class Move:
    '''The bare basics functionality needed for a move
    '''
    def __init__(self, unit):
        self.unit = unit #The unit ID of the unit making the move

    def transform(x,y,direction, magnitude):
        ''' 
        Returns coordinates starting at <x,y> in the direciton of  <direction> with magnitude <magnitude>
        The subclass should implement this
        '''
        pass
    def serialize():
        '''
        Returns the serialized form of this move
        The subclass should implement this
        '''
        pass
    def verifyMove():
        '''
        Returns whether the move is valid
        The subclass should implement this
        '''
        pass
    def makeMove(): #Note that this should take in a game state
        '''
        Perform move on the game state
        The subclass should implement this
        '''










class Move:
    def transform(x, y, direction):
        if direction == 'UP'    : y -= 1
        if direction == 'DOWN'  : y += 1
        if direction == 'RIGHT' : x += 1
        if direction == 'LEFT'  : x -= 1
        return x, y

    def _can_follow_path(self, lst, board, all_units, x, y):
        for m in lst:
            x, y = Move.transform(x, y, m)

            if all_units.get('{},{}'.format(x, y)) is not None:
                return False

            if isinstance(board[y][x], WallTile):
                return False

        return True

class AttackMove(Move):

    def __init__(self, unit, target):
        self.unit = unit
        self.target = target

    def len(self):
        return len(self.target)

    def get_relative_moves(self):
        return Move._get_relative_moves(self.target)

class StunMove(Move):

    def __init__(self, unit, target):
        self.unit = unit
        self.target = target

    def len(self):
        return len(self.target)

    def get_relative_moves(self):
        return Move._get_relative_moves(self.target)


class StasisMove(Move):

    def __init__(self, unit, direction, unit_type):
        self.unit = unit
        self.direction = direction
        self.unit_type = unit_type

    def len(self):
        return 0

    def free_spot(self, x, y, all_units, board):
        nx, ny = Move.transform(x, y, self.direction)
        if isinstance(board[ny][nx], WallTile):
            return False

        return '{},{}'.format(nx, ny) not in all_units


class GroundMove(Move):

    def __init__(self, unit, moves):
        self.unit = unit
        self.moves = moves

    def len(self):
        return len(self.moves)

    def get_dict(self):
        return {self.unit.id: self.moves}

    def valid_path(self, board, all_units, x, y):
        return self._can_follow_path(self.moves, board, all_units, x, y)
        
    def get_relative_moves(self):
        return Move._get_relative_moves(self.moves)


class MineMove(Move):

    def __init__(self, unit):
        self.unit = unit

    def len(self):
        return 0
