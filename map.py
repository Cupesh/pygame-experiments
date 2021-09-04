import pytmx
import pygame
from pytmx.util_pygame import load_pygame

def create_map():
    tiled_map = load_pygame('pygame test map.tmx')
    tilewidth = tiled_map.tilewidth
    tileheight = tiled_map.tileheight

    collision = tiled_map.get_layer_by_name('collision')

    tiles = []
    for x, y, tile in collision.tiles():
            if (tile):
                tiles.append(pygame.Rect([(x*tilewidth), (y*tileheight), tilewidth, tileheight]));

    world = pygame.Surface((1600, 1600))


    for layer in tiled_map.layers:
        if isinstance(layer, pytmx.TiledTileLayer) and (layer!=collision):
            for x, y, tile in layer.tiles():
                if (tile):
                    world.blit(tile, [x*tilewidth,y*tileheight])

    return world