import pygame
import Game

if __name__ == '__main__':
    game = Game.Game()
    
    game.start_pygame()
    game.load_assets()
    game.run()

    pygame.quit()
