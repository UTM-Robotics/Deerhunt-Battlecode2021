from Engine.server.engine_core import *
from Engine.server.server_launcher import ServerLauncher
from .render import MerlinRenderFactory
from .move import MerlinMoveFactory
from .tile import MerlinTileFactory

class MerlinServerLauncher(ServerLauncher):
    '''
        A launch system for the Merlin game.
    '''

    def getTileFactory(self):
        return MerlinTileFactory()

    def getMoveFactory(self):
        return MerlinMoveFactory()

    def getMapRenderFactory(self):
        return MerlinRenderFactory()
