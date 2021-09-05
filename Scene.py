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

SCALED_SCREEN_WIDTH = 320
SCALED_SCREEN_HEIGHT = 240

SCREEN_CENTRE_X = SCREEN_WIDTH // 2
SCREEN_CENTRE_Y = SCREEN_HEIGHT // 2

PLAYER_CENTER_X = SCALED_SCREEN_WIDTH // 2
PLAYER_CENTRE_Y = SCALED_SCREEN_HEIGHT // 2

player = Player.Player()
player.x_pos = PLAYER_CENTER_X
player.y_pos = PLAYER_CENTRE_Y
speed = player.speed

class Scene():
    def __init__(self):
        self.next_scene = None

    def terminate_scene(self):
        self.next_scene = None

class PlayScene(Scene):
    def __init__(self, map=None):
        super().__init__()
        self.world = map
        self.width = self.world.get_width()
        self.height = self.world.get_height()
        self.world_x = SCREEN_WIDTH - self.width
        self.world_y = SCREEN_HEIGHT - self.height

    def controls(self, pressed_keys):
        if pressed_keys[K_DOWN] and player.y_pos >= PLAYER_CENTRE_Y:
            self.world_y -= speed
        elif pressed_keys[K_DOWN] and player.y_pos < PLAYER_CENTRE_Y:
            player.y_pos += speed

        if pressed_keys[K_UP] and player.y_pos <= PLAYER_CENTRE_Y:
            self.world_y += speed
        elif pressed_keys[K_UP] and player.y_pos > PLAYER_CENTRE_Y:
            player.y_pos -= speed 

        if pressed_keys[K_RIGHT] and player.x_pos >= PLAYER_CENTER_X:
            self.world_x -= speed
        elif pressed_keys[K_RIGHT] and player.x_pos < PLAYER_CENTER_X:
            player.x_pos += speed

        if pressed_keys[K_LEFT] and player.x_pos <= PLAYER_CENTER_X:
            self.world_x += speed
        elif pressed_keys[K_LEFT] and player.x_pos > PLAYER_CENTER_X:
            player.x_pos -= speed

        if self.world_x < -self.width + SCALED_SCREEN_WIDTH:
            self.world_x = -self.width + SCALED_SCREEN_WIDTH
            player.x_pos += speed
        if self.world_x > 0:
            self.world_x = 0
            player.x_pos -= speed
        if self.world_y < -self.height + SCALED_SCREEN_HEIGHT:
            self.world_y = -self.height + SCALED_SCREEN_HEIGHT
            player.y_pos += speed
        if self.world_y > 0:
            self.world_y = 0
            player.y_pos -= speed

    def process_events(self, events):
        pass

    def update(self):
        pass



    def render(self):
        scaled_screen = pygame.Surface((SCALED_SCREEN_WIDTH, SCALED_SCREEN_HEIGHT))
        scaled_screen.blit(self.world, [self.world_x, self.world_y])
        scaled_screen.blit(player.surf, [player.x_pos, player.y_pos])

        screen = pygame.display.get_surface()
        pygame.transform.scale(scaled_screen, (800, 600), screen)
        

