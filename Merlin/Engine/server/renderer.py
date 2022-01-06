import pygame
import time
import threading
class RenderingEngine:

    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    def __init__(self, factory, gameMap):
        self.tile_list = []
        self.map = gameMap
        self.cells_y = len(self.map.map)
        self.cells_x = len(self.map.map[0])
        self.miscellaneous = {}
        # find size of tiles required to be at max 720x720 
        # 720 = cells_x*tile_size,
        pygame.init()
        self.tile_size = min(720/self.cells_x, 720/self.cells_y)
        self.factory = factory
        self.screen = pygame.display.set_mode((920, 720))
        pygame.display.set_caption("Battlecode: Merlin.io") # TODO this should be passed in as well
        pygame.event.set_blocked(pygame.MOUSEMOTION)

    def wait(self):
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                    raise SystemExit

    def update(self, gameMap, units, miscellaneous):

        self.units = units
        self.map = gameMap
        self.miscellaneous = miscellaneous
        print(miscellaneous)

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
        self.draw_units()
        # TODO render miscellaneous
        self.draw_text(self.screen, str(self.miscellaneous))
        pygame.display.update()
        pygame.event.wait()

    def draw_units(self):
        unit_list = []
        for unit in self.units.values():
            img = pygame.transform.scale(self.factory.get_unit_image(unit), (self.tile_size, self.tile_size)
                )
            img_rect = img.get_rect()
            img_rect = img.get_rect()
            img_rect.x = unit.x * self.tile_size
            img_rect.y = unit.y * self.tile_size
            drawn = (img, img_rect)
            unit_list.append(drawn)
        for unit in unit_list:
            self.screen.blit(unit[0], unit[1])
    def draw_text(self, surface, text, color=pygame.Color('white')):
        font = pygame.font.SysFont(None, 40)
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = (720,720)
        pos = (300, 400)
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

class BaseRenderFactory:
    def get_tile_image(self, tile):
        raise NotImplementedError
    def get_unit_image(self, unit):
        raise NotImplementedError