#Figure out import

from server import Units

from Engine.server.move import Move

from game.constants import Moves, Units

# 0 represents cost to buy, anything above represents cost to upgrade
UPGRADE_COSTS = {
  Units.WORKER: {},
  Units.SCOUT: {},
  Units.KNIGHT: {},
  Units.ARCHER: {}
}
class MoveFactory:
    def createMove(uid:String, *restInfo):
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
  def verifyMove(self):
      '''
      Returns whether the move is valid
      The subclass should implement this
      '''
      pass
  def makeMove(self, gameState): #Note that this should take in a game state
      '''
      Perform move on the game state
      The subclass should implement this
      '''


class AttackMove(GameMove):
  def __init__(self, unit, target):
      super().__init__(unit)
      self.target = target
  
  def __repr__(self):
      '''
      Returns the serialized form of this move
      '''
      return {'command': Moves.ATTACK, "unit": self.unit, "target": self.target }
  def verifyMove(self):
      '''
      Returns whether the move is valid
      '''
      pass
  def makeMove(self, gameState): #Note that this should take in a game state
      '''
      Perform move on the game state
      The subclass should implement this
      '''

class UpgradeMove(GameMove):
  def __init__(self, unit):
      super().__init__(unit)
  
  def serialize(self):
      '''
      Returns the serialized form of this move
      '''
      return {'command': Moves.UPGRADE, "unit": self.unit}
  def verifyMove(self):
      '''
      Returns whether the move is valid
      '''
      pass
  def makeMove(self, gameState): #Note that this should take in a game state
      '''
      Perform move on the game state
      The subclass should implement this
      '''
class DirectionMove(GameMove):
  def __init__(self, unit, direction):
      super().__init__(unit)
      self.direction = direction
  
  def serialize(self):
      '''
      Returns the serialized form of this move
      '''
      return {'command': Moves.DIRECTION, "unit": self.unit, "direction": self.direction}
  def verifyMove(self):
      '''
      Returns whether the move is valid
      '''
      pass
  def makeMove(self, gameState): #Note that this should take in a game state
      '''
      Perform move on the game state
      '''
      pass

class MineMove(GameMove):
  def __init__(self, unit):
      super().__init__(unit)
  
  def serialize(self):
      '''
      Returns the serialized form of this move
      '''
      return {'command': Moves.MINE, "unit": self.unit }
  def verifyMove(self):
      '''
      Returns whether the move is valid
      '''
      pass
  def makeMove(self, gameState): #Note that this should take in a game state
      '''
      Perform move on the game state
      '''
      pass

class BuyMove(GameMove):
  def __init__(self, unitType):
      super().__init__(None)
      self.unitType = unitType
  
  def serialize(self):
      '''
      Returns the serialized form of this move
      '''
      return {'command': Moves.BUY, "unitType": self.unitType}
  def verifyMove(self):
      '''
      Returns whether the move is valid
      '''
      pass
  def makeMove(self, gameState): #Note that this should take in a game state
      '''
      Perform move on the game state
      '''

class CaptureMove(GameMove):
  def __init__(self, unit, direction):
      super().__init__(unit)
      self.direction = direction
  
  def serialize(self):
      '''
      Returns the serialized form of this move
      '''
      return {'command': Moves.CAPTURE, "unit": self.unit, 'direction': self.direction}
  def verifyMove(self):
      '''
      Returns whether the move is valid
      '''
      pass
  def makeMove(self, gameState): #Note that this should take in a game state
      '''
      Perform move on the game state
      '''



  
