from server import *
from Engine.server.units import Unit

from game.constants import Units

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
        self.id_count += 1
        return unit


class GameUnit(Unit):
  def __init__(self,x,y,UnitType, id, health, speed):
    self.health = health
    self.speed = speed
    self.level = 1
    self.has_flag = False
    super().__init__(x,y,UnitType, id)

    self.unit_type = UnitType
    self.id = id
    self.x = x
    self.y = y

  def __repr__(self):
      return NotImplemented()


class WorkerUnit(GameUnit):

    def __init__(self, x, y, id):
        super().__init__(x, y, Unit.WORKER, id, 100, 1)
        self.duplication_time = -1
        self.duplicating_to = None
        self.is_duplicating = False
        self.action_direction = None
        self.mining_status = -1

    def __repr__(self):
        return "Worker"
    
    def is_duplicating(self):
        return self.is_duplicating

    def start_duplication(self, duplicating_to_type, duplication_time):
        self.is_duplicating = True
        self.duplicating_to_type = duplicating_to_type
        self.duplication_time = duplication_time

    def finish_duplicating(self):
        self.duplication_time = -1
        self.duplicating_to = None
        self.is_duplicating = False
    
    def is_mining(self):
        return self.mining_time > 0

class ScoutUnit(GameUnit):

    def __init__(self, x, y, id):
        super().__init__(x, y, Unit.SCOUT, id, 60, 1.3)

    def __repr__(self):
        return "Scout"

    def capture(self):
        self.has_flag = True

class KnightUnit(GameUnit):

    def __init__(self, x, y, id):
        super().__init__(x, y, Unit.KNIGHT, id, 130, 0.7)

    def __repr__(self):
        return "Knight"


class ArcherUnit(GameUnit):

    def __init__(self, x, y, id):
        super().__init__(x,y, Unit.ARCHER, id, 100, 1)


    def __repr__(self):
        return "Archer"

    def attack():
        pass

    def can_hit(direction):
        pass


