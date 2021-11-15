import pygame

tile_size = 200
map_1 = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
]


class Tiles:
    def __init__(self):
        self.tile_list = []
        self.map = map

    def convert_map(self, map):
        wall_img = pygame.image.load("assets/wall.png")
        bubble_img = pygame.image.load("assets/bubble.png")
        row_count = 0
        for row in map:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(wall_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


pygame.init()

wall_img = pygame.image.load("assets/wall.png")

background_colour = (255, 255, 255)
screen_height = 1000
screen_width = 1000
screen_dim = (screen_width, screen_height)

screen = pygame.display.set_mode(screen_dim)

pygame.display.set_caption("Battlecode 2021")

world = Tiles()

running = True
while running:
    world.convert_map(map_1)
    print(world.tile_list)
    world.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
