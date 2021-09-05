import pytmx
import pygame
from pytmx.util_pygame import load_pygame

class Map():
    def __init__(self, tiled_map):
        self.tiled_map = load_pygame(tiled_map)
        self.width = self.tiled_map.width
        self.height = self.tiled_map.height
        self.tilewidth = self.tiled_map.tilewidth
        self.tileheight = self.tiled_map.tileheight

    def create_map(self):
        collision = self.tiled_map.get_layer_by_name('collision')

        tiles = []
        for x, y, tile in collision.tiles():
                if (tile):
                    tiles.append(pygame.Rect([(x*self.tilewidth), (y*self.tileheight), self.tilewidth, self.tileheight]))

        world = pygame.Surface((1600, 1600))


        for layer in self.tiled_map.layers:
            if isinstance(layer, pytmx.TiledTileLayer) and (layer!=collision):
                for x, y, tile in layer.tiles():
                    if (tile):
                        world.blit(tile, [x*self.tilewidth,y*self.tileheight])

        return world