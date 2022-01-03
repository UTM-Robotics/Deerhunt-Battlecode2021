import pygame


class RenderingEngine:
    def __init__(self, factory):
        self.tile_list = []
        self.tile_size = 20
        self.factory = factory
        self.screen = pygame.display.set_mode((820, 720))
        pygame.display.set_caption("Merlin.io") # TODO this should be passed in as well

    def update(self, tile_list, units, miscellaneous):
        self.units = units
        self.tile_list = tile_list
        self.miscellaneous = miscellaneous

    def draw(self):
        row_count = 0
        for row in self.tile_list:
            col_count = 0
            for tile in row:

                img = pygame.transform.scale(
                    self.factory.get_tile_image(tile), (self.tile_size, self.tile_size)
                )
                img_rect = img.get_rect()
                img_rect.x = col_count * self.tile_size
                img_rect.y = row_count * self.tile_size
                tile = (img, img_rect)
                self.tile_list.append(tile)
                col_count += 1
            row_count += 1

        for tile in self.tile_list:
            self.screen.blit(tile[0], tile[1])
        # TODO render units

        # TODO render miscellaneous
        pygame.display.update()

class BaseRenderFactory:
    def get_tile_image(self, tile):
        raise NotImplementedError