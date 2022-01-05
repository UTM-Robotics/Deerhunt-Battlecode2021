from .engine_core import ClientEngine
class DecodeDataFactory:
  def decode(self, js):
    return NotImplementedError

class EncodeDataFactory:
  def encode(self, moves):
    return NotImplementedError
class ClientLauncher:
    '''
        To be extended, acts as a strict guide for how to launch a Battlecode game.
        Once all factories are implemented, the game should function as required for the Client.
    '''
    def getDecodeDataFactory(self):
        raise NotImplementedError
    
    def getEncodeDataFactory(self):
      raise NotImplementedError

    def getPlayer(self):
      raise NotImplementedError

    def start(self):
        encodeDataFactory = self.getEncodeDataFactory()
        decodeDataFactory = self.getDecodeDataFactory()
        player = self.getPlayer()
        engine = ClientEngine(encodeDataFactory= encodeDataFactory, decodeDataFactory=decodeDataFactory, player = player)
        print("Loaded client engine")
        engine.start()