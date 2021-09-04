import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)
import Player

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WORLD_WIDTH = 1600
WORLD_HEIGHT = 1600

SCREEN_CENTRE_X = SCREEN_WIDTH // 2
SCREEN_CENTRE_Y = SCREEN_HEIGHT // 2

player = Player.Player()
player.x_pos = SCREEN_CENTRE_X
player.y_pos = SCREEN_CENTRE_Y
speed = player.speed

class Scene():
    def __init__(self):
        self.next_scene = None

    def terminate_scene(self):
        self.next_scene = None

class PlayScene(Scene):
    def __init__(self, map=None):
        super().__init__()
        self.world_x = SCREEN_WIDTH - 900
        self.world_y = SCREEN_HEIGHT - 700

        self.world = map

        '''
        self.world = pygame.Surface((WORLD_WIDTH, WORLD_HEIGHT))
        self.world.fill(BLUE)
        self.ground = pygame.Surface((900, 700))
        self.ground.fill(GREEN)
        self.world.blit(self.ground, ( ((WORLD_WIDTH - 900) // 2),((WORLD_HEIGHT - 700) // 2)) )
        '''

    def controls(self, pressed_keys):
        if pressed_keys[K_DOWN] and player.y_pos >= SCREEN_CENTRE_X:
            self.world_y -= speed
        elif pressed_keys[K_DOWN] and player.y_pos < SCREEN_CENTRE_X:
            player.y_pos += speed

        if pressed_keys[K_UP] and player.y_pos <= SCREEN_CENTRE_X:
            self.world_y += speed
        elif pressed_keys[K_UP] and player.y_pos > SCREEN_CENTRE_X:
            player.y_pos -= speed 

        if pressed_keys[K_RIGHT] and player.x_pos >= SCREEN_CENTRE_Y:
            self.world_x -= speed
        elif pressed_keys[K_RIGHT] and player.x_pos < SCREEN_CENTRE_Y:
            player.x_pos += speed

        if pressed_keys[K_LEFT] and player.x_pos <= SCREEN_CENTRE_Y:
            self.world_x += speed
        elif pressed_keys[K_LEFT] and player.x_pos > SCREEN_CENTRE_Y:
            player.x_pos -= speed

        if self.world_x < SCREEN_WIDTH - WORLD_WIDTH:
            self.world_x = SCREEN_WIDTH - WORLD_WIDTH
            player.x_pos += speed
        if self.world_x > 0:
            self.world_x = 0
            player.x_pos -= speed
        if self.world_y < SCREEN_HEIGHT - WORLD_HEIGHT:
            self.world_y = SCREEN_HEIGHT - WORLD_HEIGHT
            player.y_pos += speed
        if self.world_y > 0:
            self.world_y = 0
            player.y_pos -= speed

    def process_events(self, events):
        pass

    def update(self):
        pass



    def render(self):
        screen = pygame.display.get_surface()
        screen.blit(self.world, [self.world_x, self.world_y])
        screen.blit(player.surf, [player.x_pos, player.y_pos])
