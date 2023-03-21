import pygame
from troid.defs.player import Player

WINDOW_TITLE = "double jump"
FPS = 40
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 800

class Game(object):
    done = False

    def __init__(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
        pygame.init()
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.fps_max = FPS
        self.player = Player()
        self.left_is_pressed = False
        self.right_is_pressed = False
