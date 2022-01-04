import pygame
from Engine.server.renderer import BaseRenderFactory

class MerlinRenderFactory(BaseRenderFactory):
    def get_tile_image(self, tile):
        # Load images
        wall_img = pygame.image.load("assets/wall.png")
        bubble_img = pygame.image.load("assets/bubble.png")