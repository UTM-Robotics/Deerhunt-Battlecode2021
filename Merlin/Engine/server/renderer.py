import pygame
import time
import threading
class RenderingEngine:
    def __init__(self, factory):
        self.tile_list = []
        self.map = []
        self.tile_size = 20
        self.factory = factory
        self.screen = pygame.display.set_mode((820, 720))
        pygame.display.set_caption("Merlin.io") # TODO this should be passed in as well
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        self.bg_thread = threading.Thread(target=RenderingEngine.keep_alive)
        self.bg_thread.start()

    def keep_alive():
        # A hacky way to keep the program alive.
        print("starting keep alive")
        while(True):
            time.sleep(0.01)
            pygame.event.pump()

    def update(self, gameMap, units, miscellaneous):

        self.units = units
        self.map = gameMap
        self.miscellaneous = miscellaneous

    def draw(self):
        pygame.event.pump()
        row_count = 0
        for row in self.map:
            col_count = 0
            for tile in row:
                img = pygame.transform.scale(
                    self.factory.get_tile_image(tile), (self.tile_size, self.tile_size)
                )
                img_rect = img.get_rect()
                img_rect.x = col_count * self.tile_size
                img_rect.y = row_count * self.tile_size
                drawn = (img, img_rect)
                self.tile_list.append(drawn)
                col_count += 1
            row_count += 1

        for tile in self.tile_list:
            self.screen.blit(tile[0], tile[1])
        # TODO render units

        # TODO render miscellaneous
        pygame.display.update()
        pygame.event.wait()

class BaseRenderFactory:
    def get_tile_image(self, tile):
        raise NotImplementedError