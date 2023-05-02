import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):

        #get disply surface
        self.display_surface = pygame.display.get_surface()


        #sprite group set up
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        #sprite set up
        self.create_map()

    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):  #y-pos
            for col_index,col in enumerate(row): #x-pos
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y), [self.visible_sprites])
            

    def run(self):
        #updates and draws the game
        self.visible_sprites.draw(self.display_surface)