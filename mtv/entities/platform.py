from pygame.color import Color
from pygame.surface import Surface
from mtv.category import Category

from mtv.entity import Entity
from mtv.point import Point


class Platform(Entity):
    def __init__(self, position: Point, width: int, height: int):
        super().__init__(
            categories=[Category.platform],
            color=Color("white"),
            position=position,
            width=width,
            height=height,
            gravity_enabled=False,
        )

    def draw_self(self, surface: Surface) -> None:
        self.draw_as_outline(surface)
