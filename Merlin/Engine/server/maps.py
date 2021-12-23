class TileFactory:
    def __init__(self):
        raise NotImplementedError
    ''' Given a TileID, returns a new Tile object'''
    def createTile(self, tileId): 
        raise NotImplementedError
class Map:
    """
    # 2D array of tile objects
    Represents a map, methods include ability to serialize and deserialize. this is the base class.
    we expect users to build on top of this
    Nested List structure, first nests list is first row elements, second list is second row elements etc.
    Map file is expected to be a string containing the
    """
    def __init__(self, map_file, tileFactory):
        self.map_file = None
        self.tileFactory = tileFactory
        self.map = []

    def deserialize(self):
        """
        deserializes the map object from the human readable .map file to its state in the game.
        :return:
        """
        if not self.map_file:
            print("error in _deserialize map file is none")
        # note: r by default
        with open(self.map_file) as f:
            i = 0
            for line in f.readlines():
                self.map.append([])
                for char in line:
                    if char not in self.keys:
                        print(f"Error: unknown symbol: {char} found in {self.map_file}")
                    self.map[i].append(char)
                i += 1
            f.close()
        print(f"finished deserializing map {self.map_file}")

    def serialize(self):
        """
        serializes the current state of the map object into a .map human-readable text file representation.
        Essentially converting The tiles to letters or symbols in the map file.
        :return string
        """
        if not self.map:
            print("Error: there is no map to serialize")
        # overwrite existing file with write mode, just easier atm. more efficient way likely exists with append/edit.
        with open(self.map_file, 'w') as f:
            for row in self.map:
                f.writelines(row)
            f.close()
        print(f"Finished Serializing map into {self.map_file}")