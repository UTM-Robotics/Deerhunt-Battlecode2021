from Engine.client.client_launcher import ClientLauncher

from .grid_player import GridPlayer
class MerlinClientLauncher(ClientLauncher):
    '''
        A launch system for the Merlin game Client
    '''
    def getDecodeDataFactory(self):
        return MerlinTileFactory() #TODO

    def getEncodeDataFactory(self):
        return MerlinMoveFactory() #TODO

    def getPlayer(self):
        return GridPlayer()
