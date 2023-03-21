from typing import Optional

import pygame
from pygame.locals import Color
from pygame.sprite import Sprite
from pygame.surface import Surface

GRAVITY = 8
MAX_JUMP_SPEED = 50
MAX_JUMP_HEIGHT = 200
MAX_RUN_SPEED = 20

PLAYER_WIDTH = 30
PLAYER_HEIGHT = 30


class Player(Sprite):
    FILL_COLOR = Color("gray100")

    def __init__(self):
        Sprite.__init__(self)
        self.image = Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.image.fill(self.FILL_COLOR)
        self.rect = self.image.get_rect()
        self.screen = pygame.display.get_surface()

        self.rect.midbottom = self.screen.get_rect().midbottom

        self.velx, self.vely = 0.0, 0.0

        self.jump_height = 0
        self.is_jumping = False
        self.can_jump = True
        self.height_when_doublejumped: Optional[int] = None
        self.can_doublejump = True

    @property
    def on_ground(self):
        return self.rect.bottom > self.screen.get_rect().bottom

    @property
    def is_doublejumping(self):
        return self.is_jumping and not self.can_doublejump

    @property
    def at_max_height(self):
        bottom = self.height_when_doublejumped or 0
        return self.jump_height >= MAX_JUMP_HEIGHT + bottom
