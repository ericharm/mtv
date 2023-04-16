from typing import List

import pygame

from mtv.defs.platform import Platform
from mtv.defs.player import Player

WINDOW_TITLE = "mtv"
FPS = 40
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 800


class Game:
    done = False
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    fps_max = FPS
    player = Player()
    platforms: List[Platform] = []
    left_is_pressed = False
    right_is_pressed = False

    def __init__(self) -> None:
        self.platforms = [Platform(20, 20, 100, 100)]
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
