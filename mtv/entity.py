from __future__ import annotations
from pygame.color import Color
from pygame.surface import Surface
import pygame

from mtv.category import Category
from mtv.point import Point
from mtv.scene_node import SceneNode

LINE_WIDTH = 1
LINE_SPACING = 6
GRAVITY = 0.5


class Entity(SceneNode):
    def __init__(
        self,
        categories: list[Category],
        color: Color,
        position: Point,
        width: float,
        height: float,
        gravity_enabled: bool = True,
        on_ground: bool = False,
    ):
        super().__init__(categories)
        self.color = color
        image = Surface([width, height])
        image.fill(self.color)
        self.image = image
        self.rect = image.get_rect()
        self.rect.move_ip(position.x, position.y)
        self.gravity_enabled = gravity_enabled
        self.on_ground = on_ground
        velocity_y = 0
        if self.gravity_enabled and not self.on_ground:
            velocity_y = GRAVITY
        self.velocity = [0, velocity_y]

    def update_self(self, dt: float) -> None:
        self.rect.move_ip(self.velocity[0] * dt, self.velocity[1] * dt)

    def set_on_ground(self, on_ground: bool) -> None:
        self.on_ground = on_ground
        self.velocity[1] = 0

    def draw_self(self, surface: Surface) -> None:
        self.draw_as_solid_rect(surface)

    def draw_as_solid_rect(self, surface: Surface) -> None:
        surface.blit(self.image, self.rect)

    def draw_as_outline(self, surface: Surface) -> None:
        pygame.draw.rect(surface, self.color, self.rect, LINE_WIDTH)
        pygame.draw.line(
            surface,
            self.color,
            (self.rect.left, self.rect.top),
            (self.rect.right, self.rect.bottom),
            LINE_WIDTH,
        )
