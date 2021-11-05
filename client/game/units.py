#TODO: import from unit class


#EXAMPLE
class GameUnit:
    def __init__(self, attr: dict) -> None:
        """
        Initialize a new Unit.
        """
        self.attr = attr
        self.type = attr['type']  # 'worker' or 'melee'.
        self.x = attr['x']
        self.y = attr['y']
        self.id = attr['id']

    def attack(self, *directions: (str)) -> Move:
        """
        Return an 'attack' Move for this Unit in the given <*directions>.
        """
        return Move(self.id, 'ATTACK', *directions)

    def can_attack(self, enemy_units: 'Units') -> ['Unit', str]:
        """
        Returns a list of enemy Unit that can be attacked \
            and the direction needed to attack them.(?)
        """
        enemies = []
        for id in enemy_units.units:
            unit = enemy_units.get_unit(id)
            direction = self.direction_to((unit.x, unit.y))
            if self.coordinate_from_direction(self.x, self.y, direction) == \
                    (unit.x, unit.y):
                enemies.append((unit, direction))
        return enemies

    def stun(self, *directions: (str)) -> Move:
        """
        Return an 'stun' Move for this Unit in the given <*directions>.
        """
        return Move(self.id, 'STUN', *directions)

    def can_stun(self, enemy_units: 'Units') -> ['Unit', [str]]:
        """
        Returns a list of enemy Units that can be stunned and 
        the direction needed to attack them.
        """
        enemies = []
        for id in enemy_units.units:
            unit = enemy_units.get_unit(id)
            direction = self.direction_to((unit.x, unit.y))
            check_coord = self.coordinate_from_direction(self.x, self.y, direction)
            check_coord2 = self.coordinate_from_direction(check_coord[0], check_coord[1], direction)
            if check_coord == \
                    (unit.x, unit.y):
                enemies.append((unit, [direction]))
            elif check_coord2 == (unit.x, unit.y):
                enemies.append((unit, [direction, direction]))
        return enemies

    def can_duplicate(self, resources: int, unit_type: str) -> bool:
        """
        Returns if this Unit can duplicate.
        """
        if self.type == 'worker' \
                and self.attr['duplication_status'] <= 0:
            if (unit_type == 'melee' and self.attr['melee_cost'] <= resources) or \
                    (unit_type == 'worker' and self.attr['worker_cost'] <= resources):
                return True
        else:
            return False

    def can_mine(self, game_map: 'Map') -> bool:
        """
        Returns if this Unit can mine.
        """
        if self.type == 'worker' and game_map.is_resource(self.x, self.y) \
                and self.attr['mining_status'] <= 0:
            return True
        else:
            return False

    def mine(self) -> None:
        """
        Returns a 'mine' Move for this Unit.
        """
        return Move(self.id, 'MINE')

    def duplicate(self, direction: (str), unit_type: str) -> Move:
        """
        Returns a 'duplicate' Move for this Unit in the given <direction>.
        """
        return Move(self.id, 'DUPLICATE_M' if unit_type == 'melee' else 'DUPLICATE_W', direction)

