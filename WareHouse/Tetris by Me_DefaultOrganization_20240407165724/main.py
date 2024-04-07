'''
This is the main file of the Tetris game. It initializes the game and starts the game loop.
'''
import pygame
from tetris import Tetris
def main():
    pygame.init()
    game = Tetris()
    game.run()
if __name__ == "__main__":
    main()