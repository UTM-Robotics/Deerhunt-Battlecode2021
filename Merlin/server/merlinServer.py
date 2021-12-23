import sys
import os
sys.path.append(os.path.abspath('../Engine'))
from Engine.server.EngineCore import *
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
        tileFactory = MerlinServerLauncher.getTileFactory()
        mapRenderFactory = MerlinServerLauncher.getMapRenderFactory()
        moveFactory = MerlinServerLauncher.getMoveFactory()
        engine = GameEngine(tileFactory= tileFactory, mapRenderFactory=mapRenderFactory, moveFactory=moveFactory)
        engine.start()

