#Figure out import

from Engine.server.move import Move

from game.constants import Moves
class MerlinMoveFactory:
    def createMove(uid:str, *restInfo):
        '''
        Deserializes move, this is the factory used in client_connection.py 
        '''
        if uid == Moves.ATTACK:
          return AttackMove(*restInfo)
        elif uid == Moves.BUY:
          return BuyMove(*restInfo)
        elif uid == Moves.CAPTURE:
          return CaptureMove(*restInfo)
        elif uid == Moves.DIRECTION:
          return DirectionMove(*restInfo)
        elif uid == Moves.MINE:
          return MineMove(*restInfo)
        elif uid == Moves.UPGRADE:
          return UpgradeMove(*restInfo)


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



  
