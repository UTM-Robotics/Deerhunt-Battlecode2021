from pygame import *

class RenderFactory:
    def __init__(self):
        self.tile_list = []
        self.tile_size = (100, 100)
        display.set_caption("Merlin.io")
        self.window = display.set_mode((720, 360))
        self.background.fill((255, 255, 255))

    def convert(self, tile_list):

    def display(self):