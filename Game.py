import pygame
import sys
from Scene import PlayScene

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

class Game():
    def __init__(self):
        self.active_scene = PlayScene()

    def start_pygame():
        global screen, clock

        pygame.init()
        screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.mixer.init()
        pygame.display.set_caption('a game')
        clock = pygame.time.Clock()

    def run(self):
        while self.active_scene != None:
            pressed_keys = pygame.key.get_pressed()
            filtered_events = []

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    filtered_events.append(event)

            self.active_scene.process_events(filtered_events)
            self.active_scene.controls(pressed_keys)
            self.active_scene.render()

            pygame.display.flip()
            clock.tick(FPS)
