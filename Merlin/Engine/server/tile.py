class TileFactory:
    def __init__(self):
        pass
    ''' Given a TileID, returns a new Tile object'''

    def createTile(self, tileId): 
        '''
        Takes a tileId for your game, generates a Tile object correspondingly.
        If not matching, returns None.
        '''
        raise NotImplementedError

class Tile():
    pass

class IllegalTileException(Exception):
    pass
