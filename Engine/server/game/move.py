#Figure out import

#HAVE LIST OF MOVES HERE

class MoveFactory:
    def createMove(uid:String, *restInfo):
         '''
         Deserializes move, this is the factory used in client_connection.py 
         '''
         pass


class GameMove(Move):
  def __init__(self,unit):
    super(unit)
    def serialize(self):
        '''
        Returns the serialized form of this move
        The subclass should implement this
        '''
        pass
    def verifyMove(self):
        '''
        Returns whether the move is valid
        The subclass should implement this
        '''
        pass
    def makeMove(self): #Note that this should take in a game state
        '''
        Perform move on the game state
        The subclass should implement this
        '''
    def transform(x,y,direction, magnitude):
        ''' 
        Returns coordinates starting at <x,y> in the direciton of  <direction> with magnitude <magnitude>
        The subclass should implement this
        '''
        pass
    def _get_relative_moves(lst, magnitude):
      '''
      Get coordinate from a given list of directions
      '''
      x = 0
      y = 0
      for m in lst:
          if isinstance(m, list):
              for n in m:
                  x, y = GameMove.transform(x, y, n, magnitude)
          else:
              x, y = GameMove.transform(x, y, m, magnitude)

      return x, y


#Example subclass
class ExampleAttackMove(GameMove):
  def __init__(self,unit,target):
    super(unit)
    self.target = target 
  def serialize(self):
    return 'ATTACK {}'.format(target)
  def makeMove(self,*gameState):
    #Do some stuff
    return 
  def verifyMove(self):
    return True
