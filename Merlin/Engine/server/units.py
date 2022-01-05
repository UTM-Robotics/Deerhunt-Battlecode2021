class Unit:
    """
    Units are given to players and can interact with the map
    """
    def __init__(self, x, y,unitType, id):
        self.x = x
        self.y = y
        self.id = id
        self.unitType = unitType
        self.type = None

    def pos_tuple(self):
        return self.x, self.y

    def set_relative_location(self, all_units, x, y):
        nx = self.x + x
        ny = self.y + y

        if '{},{}'.format(nx, ny) not in all_units:
            self.x = nx
            self.y = ny

    def __repr__(self):
        return NotImplemented()

