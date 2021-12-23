from server import *
from enum import Enum
from .unit import Unit
units = {'Worker': 1, 'Scout': 2, 'Knight': 3, 'Archer': 4}

class Units(Enum):
    WORKER = 1
    SCOUT = 2
    KNIGHT = 3
    ARCHER = 4

class UnitFactory():

    id_count = 0

    def createUnit(self,uid, *restInfo):
        '''
        Deserializes unit, this is the factory used to create new units
        '''

        unit = None
        if uid == Units.WORKER:
            unit = WorkerUnit(*restInfo, self.id_count)
        elif uid == Units.SCOUT:
            unit = ScoutUnit(*restInfo, self.id_count)
        elif uid == Units.KNIGHT:
            unit = KnightUnit(*restInfo, self.id_count)
        elif uid == Units.ARCHER:
            unit = ArcherUnit(*restInfo, self.id_count)
        else:
            return None

        return unit


class GameUnit(Unit):
  def __init__(self,x,y,UnitType, id, health, speed):
    self.health = health
    self.speed = speed
    self.has_flag = False
    super().__init__(x,y,UnitType, id)
    #Include custom statuses like is_mining, is_stunned etc here
    self.unit_type = UnitType
    self.id = id
    self.x = x
    self.y = y

  def __repr__(self):
      return NotImplemented()

  def attack():
      return NotImplemented()

  def can_move(direction):
      return NotImplemented()

  def can_hit(direction):
      return NotImplemented()

class WorkerUnit(GameUnit):

    def __init__(self, x, y, id):
        super().__init__(x, y, Unit.WORKER, id, 100, 1)

    def __repr__(self):
        return "Worker"

    def attack():
        pass

    def can_move():
        pass

    def can_hit(direction):
        pass

class ScoutUnit(GameUnit):

    def __init__(self, x, y, id):
        super().__init__(x, y, Unit.SCOUT, id, 60, 1.3)

    def __repr__(self):
        return "Scout"

    def attack():
        pass

    def can_move():
        pass

    def can_hit(direction):
        pass

    def capture():
        self.has_flag = True

class KnightUnit(MeleeUnit):

    def __init__(self, x, y, id):
        super().__init__(x, y, Unit.KNIGHT, id, 130, 0.7)

    def __repr__(self):
        return "Knight"

    def attack():
        pass

    def can_move():
        pass

    def can_hit(direction):
        pass

class ArcherUnit(MeleeUnit):

    def __init__(self, x, y, id):
        super().__init__(x,y, Unit.ARCHER, id, 100, 1)


    def __repr__(self):
        return "Archer"

    def attack():
        pass

    def can_move():
        pass

    def can_hit(direction):
        pass


