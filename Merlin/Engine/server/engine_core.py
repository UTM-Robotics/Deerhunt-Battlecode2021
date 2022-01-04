
import argparse
import socket
import os
import random
from sys import platform
from Engine.server.renderer import RenderingEngine
from Engine.server import renderer

from server import *
from .grid_game import GridGame
from .client_connection import ClientConnection
from .maps import TileFactory, Map

class GameEngine:
    def __init__(self, renderFactory, tileFactory:TileFactory, moveFactory, gameFactory):
        self.renderFactory = renderFactory
        self.tileFactory = tileFactory
        self.moveFactory = moveFactory
        self.gameFactory = gameFactory
        self.sock = None
        self.host = None
        self.totalPlayers = 0
        self.NUMPLAYERS = 2
        self.connections = []
        self.addresses = []
        self.verbose = False
        self.render = False

    def __launchServer(self, port, timeout=8):
        ''' Launches the server on the desired port, handling OS descrepencies.
        '''
        #Creates and connects the socket connection to the clients
        sock = socket.socket()
        host = None
        if platform == "linux" or platform == "linux2":
            host = socket.gethostname()
        elif platform == "darwin":
            host = 'localhost'
        elif 'win' in platform:
            host = socket.gethostname()
        else:
            print(f"The platform {platform} is not natively suppported and there may be errors")
        sock.bind((host,port))

        sock.settimeout(7)
        sock.listen(self.NUMPLAYERS)
        self.sock = sock

    def __connectNextPlayer(self):
        player = self.totalPlayers + 1
        print(f'Waiting for client {player}...')
        conn, addr = self.sock.accept()
        self.connections.append(ClientConnection(conn, f'p{player}', verbose=self.verbose,moveFactory=self.moveFactory))
        self.addresses.append(addr)

        if not self.verbose:
            self.connections[-1].conn.settimeout(3)
        print(f'Connected to client {player} at addr')
        self.totalPlayers += 1

    def __loadMap(self):
        #Picks a random map from the maps folder and creates the game
        # TODO: CHANGE MAP LOADING SYSTEM
        file_name = 'maps/{}'.format(random.choice(os.listdir('maps')))
        print("Loading Map:", file_name)
        self.map = Map(file_name, self.tileFactory)

    def __runGameLoop(self, map):
        game = self.gameFactory(self.connections, map)
        # TODO: Change end game logic
        #Ticks the game unit there is a winner or the max_turns is reached
        turn = 0
        winner = None
        print('Game starting...')
        while turn < self.MAX_TURNS and winner == None: # TODO: Raise notimplementedError
            winner = game.tick(self.MAX_TURNS - turn)
            current_map, current_units, current_misc = game.get_state()
            if self.does_render:
                self.renderEngine.update(current_map, current_units, current_misc)
                self.renderEngine.draw()
            if self.verbose:
                print(game.get_state)
            turn += 1
        print('Winner:', winner)
        return winner

    def start(self, doRender=False, savePath="", maxTurns=200):
        #Retrieves the port and verbose flag from arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('port', type=int, help='The port to listen on')
        parser.add_argument('--logpath', type=str, help='The port to listen on', nargs='?', const=None)
        parser.add_argument('--outputpath', type=str, help='The port to listen on', nargs='?', const=None)

        parser.add_argument('--verbose', help='Should display the game turn by turn', action='store_true')
        parser.add_argument('--render', help='Should render the game\'s images turn by turn', action='store_true')

        args = parser.parse_args()
        self.verbose = args.verbose
        self.does_render = args.render
        self.save_path = args.logpath
        # TODO: implement save_path feature - Should serialize all contents directly to a file at save_path.
        # TODO: implement a 
        self.__loadMap()
        
        self.__launchServer(args.port)
        for player in range(self.NUMPLAYERS):
            self.__connectNextPlayer()
        if self.does_render:
            self.renderEngine = RenderingEngine(self.mapRenderFactory)
        self.__runGameLoop(self.map)
        for connection in self.connections:
            connection.close()
        self.sock.close()
