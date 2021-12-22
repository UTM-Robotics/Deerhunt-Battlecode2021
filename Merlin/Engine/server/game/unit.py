from server import *
class UnitFactory():
    def createUnit(uid, *restInfo):
        '''
        Deserializes unit, this is the factory used to create new units
        '''
        pass

class GameUnit:
  def __init__(self,x,y,unitType, id):
    #Include custom statuses like is_mining, is_stunned etc here
    self.unit_type = UnitType
    self.id = id
    self.x = x
    self.y = y

  def __repr__(self):
    return NotImplemented()

#EXAMPLE
MELEE_UNIT = 1
WORKER_UNIT = 1
STUN_COST = 2
WORKER_COST = 3
MELEE_COST = 5
class MeleeUnit(GameUnit):
    def __init__(self, x, y, id):
        self.type = MELEE_UNIT
        self.stun_cost = STUN_COST

        super().__init__(x, y,MELEE_UNIT,id)

    def string(self):
        if self.is_stunned():
            return '"s"'
        return '"m"'

    def __repr__(self):
        if self.is_stunned():
            return "s"
        return 'm'

    def is_mining(self):
        return False

    def is_duplicating(self):
        return False

    def can_stun(self, resources):
        if resources >= STUN_COST:
            return True
        return False


class WorkerUnit(GameUnit):
    def __init__(self, x, y, id):
        self.type = WORKER_UNIT
        self.mining_time = 5
        self.mining_status = 0

        self.duplication_status = 0
        self.stasis_direction = None
        self.duplication_time = 4
        self.duplication_unit = None

        self.melee_cost = MELEE_COST
        self.worker_cost = WORKER_COST

        super().__init__(x, y)

    def string(self):
        if self.is_stunned():
            return '"s"'
        return '"w"'

    def __repr__(self):
        if self.is_stunned():
            return "s"
        return 'w'

    def can_mine(self) -> bool:
        return self.mining_status <= 0

    def is_mining(self) -> bool:
        return self.mining_status > 0

    def start_mining(self):
        self.mining_status = self.mining_time
        return self

    def can_duplicate(self, resouces: int, unit_type: str) -> bool:
        if (unit_type == MELEE_UNIT and resouces >= self.melee_cost) or \
                (unit_type == WORKER_UNIT and resouces >= self.worker_cost):
            return self.duplication_status <= 0
        return False

    def is_duplicating(self) -> bool:
        return self.duplication_status > 0

    def start_duplication(self, direction: str, unit_type: str):
        self.duplication_status = self.duplication_time
        self.stasis_direction = direction
        self.duplication_unit = unit_type
        return self