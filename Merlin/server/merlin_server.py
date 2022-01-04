from Engine.server.engine_core import *
from Engine.server.server_launcher import ServerLauncher
from .render import MerlinRenderFactory
from .move import MerlinMoveFactory
from .tile import MerlinTileFactory
from .grid_game import MerlinGridGameFactory
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

    def getGameFactory(self):
        return MerlinGridGameFactory()
