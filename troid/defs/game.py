import pygame

from troid.defs.player import Player

WINDOW_TITLE = "double jump"
FPS = 40
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 800


class Game:
    done = False
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    fps_max = FPS
    player = Player()
    left_is_pressed = False
    right_is_pressed = False

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
