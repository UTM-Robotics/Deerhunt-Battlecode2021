import sys, pygame
import tiles
from math import *

# def render()

pygame.init()

background_colour = (255, 255, 255)
screen_height = 100
screen_width = 100
screen_dim = (screen_width, screen_height)

screen = pygame.display.set_mode(screen_dim)

pygame.display.set_caption('Battlecode 2021')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    pygame.display.update()

pygame.quit()