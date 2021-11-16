import pygame


class BaseRenderFactory:
    def convert(self, tile_list):
        raise NotImplementedError


class ExampleRenderFactory(BaseRenderFactory):
    def get_tile_image(self, tile):
        # Load images
        wall_img = pygame.image.load("assets/wall.png")
        bubble_img = pygame.image.load("assets/bubble.png")

        if tile == 1:
            img = pygame.transform.scale(wall_img, (self.tile_size, self.tile_size))
