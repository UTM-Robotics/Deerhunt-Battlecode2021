#Figure out import

from Engine.server.move import Move

from game.constants import Moves
class MerlinMoveFactory:
    def createMove(self, moveid:int, *allInfo):
        '''
        Deserializes move, this is the factory used in client_connection.py 
        '''
        valids = [move.value for move in Moves]
        if not moveid in valids:
          raise Exception(f"Invalid move id: {moveid}")

        allInfo = allInfo[1:]
        if moveid == Moves.ATTACK.value:
          return AttackMove(*allInfo)
        elif moveid == Moves.BUY:
          return BuyMove(*allInfo)
        elif moveid == Moves.CAPTURE:
          return CaptureMove(*allInfo)
        elif moveid == Moves.DIRECTION:
          return DirectionMove(*allInfo)
        elif moveid == Moves.MINE:
          return MineMove(*allInfo)
        elif moveid == Moves.UPGRADE:
          return UpgradeMove(*allInfo)


class GameMove(Move):
  def __init__(self,unit):
    super.__init__(unit)

  def __repr__(self):
      '''
      Returns the serialized form of this move
      The subclass should implement this
      '''
      pass


class AttackMove(GameMove):
  def __init__(self, unit, direction, length):
      super().__init__(unit)
      self.direction = direction
      self.length = length
  
  def __repr__(self):
      '''
      Returns the serialized form of this move
      '''
      return {'command': Moves.ATTACK, "unit": self.unit, "target": self.target }


class UpgradeMove(GameMove):
  def __init__(self, unit):
      super().__init__(unit)
  
  def __repr__(self):
      '''
      Returns the serialized form of this move
      '''
      return {'command': Moves.UPGRADE, "unit": self.unit}
class DirectionMove(GameMove):
  def __init__(self, unit, direction, magnitude):
      super().__init__(unit)
      self.direction = direction
      self.magnitude = magnitude
  
  def __repr__(self):
      '''
      Returns the serialized form of this move
      '''
      return {'command': Moves.DIRECTION, "unit": self.unit, "direction": self.direction}

class MineMove(GameMove):
    def __init__(self, unit):
        super().__init__(unit)
    
    def __repr__(self):
        '''
        Returns the serialized form of this move
        '''
        return {'command': Moves.MINE, "unit": self.unit }


class BuyMove(GameMove):
  def __init__(self, unit, unitType, direction):
      super().__init__(unit)
      self.unitType = unitType
      self.direction = direction
  
  def __repr__(self):
      '''
      Returns the serialized form of this move
      '''
      return {'command': Moves.BUY, "unitType": self.unitType, 'direction': self.direction}


class CaptureMove(GameMove):
  def __init__(self, unit, direction):
      super().__init__(unit)
      self.direction = direction
  
  def __repr__(self):
      '''
      Returns the serialized form of this move
      '''
      return {'command': Moves.CAPTURE, "unit": self.unit, 'direction': self.direction}



  
