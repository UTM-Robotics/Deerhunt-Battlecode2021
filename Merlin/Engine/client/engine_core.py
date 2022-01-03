import argparse
import socket
import sys

from .controller import NetworkedController

class ClientEngine:
  def __init__(self, encodeDataFactory, decodeDataFactory, player ):
      self.encodeDataFactory = encodeDataFactory
      self.decodeDataFactory = decodeDataFactory
      self.player = player
  
  def start(self):
    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str, help='The host to connect to')
    parser.add_argument('port', type=int, help='The port to listen on')
    args = parser.parse_args()

    sock = socket.socket()
    sock.connect((args.host, args.port))
    sys.stdout = None

    player = self.player

    controller = NetworkedController(sock, player, encodeDataFactory = self.encodeDataFactory, decodeDataFactory = self.decodeDataFactory)

    while controller.tick():
        pass

    sock.close()