# constants.py
import pygame
import os

# Вимкнути звук у CI
if os.getenv("CI") == "true":
    os.environ["SDL_AUDIODRIVER"] = "dummy"

pygame.init()



font = pygame.font.Font(None, 36)

# Constants
CELL_SIZE = 40
GRID_WIDTH = 15
GRID_HEIGHT = 15
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 650
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 192, 203)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
GRAY = (80, 80, 80)
VIOLET = (151, 89, 154)

HIGHSCORES_FILE = "highscores.txt"

# Delays for game mechanics
pacman_move_delay = 150  # Default value
ghost_move_delay = 400   # Default value
mouth_anim_delay = 500   # Default value