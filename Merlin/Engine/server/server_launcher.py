from .engine_core import GameEngine

class ServerLauncher:
    '''
        To be extended, acts as a strict guide for how to launch a Battlecode game.
        Once all factories are implemented, the game should function as required for the Server.
    '''

    def getTileFactory(self):
        raise NotImplementedError

    def getMoveFactory(self):
        raise NotImplementedError

    def getMapRenderFactory(self):
        raise NotImplementedError

    def getGameFactory(self):
        raise NotImplementedError

    def start(self):
        tileFactory = self.getTileFactory()
        renderFactory = self.getMapRenderFactory()
        moveFactory = self.getMoveFactory()
        engine = GameEngine(tileFactory= tileFactory,
            renderFactory=renderFactory,
            moveFactory=moveFactory,
            gameFactory=self.getGameFactory()
            )
        engine.start()
