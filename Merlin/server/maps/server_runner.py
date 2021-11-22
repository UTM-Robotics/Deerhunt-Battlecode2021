from Engine.server.EngineCore import GameEngine
from ..Engine import *

class MerlinServerLauncher:
    @staticmethod
    def getTileFactory():
        return None

    @staticmethod

    def getMoveFactory():
        return None

    @staticmethod
    def getMapRenderFactory():
        return None

    @staticmethod
    def start():
        tileFactory = getTileFactory()
        mapRenderFactory = getMapRenderFactory()
        moveFactory = getMoveFactory()
        engine = GameEngine(tileFactory= tileFactory, mapRenderFactory=mapRenderFactory, moveFactory=moveFactory=)


MerlinServerLauncher.start()