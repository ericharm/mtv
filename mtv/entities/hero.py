from pygame.color import Color
from pygame.surface import Surface

from mtv.category import Category
from mtv.direction import Direction
from mtv.entity import Entity
from mtv.orientation import Orientation
from mtv.point import Point

HERO_SIZE = 32
HERO_SPEED = 1


class Hero(Entity):
    def __init__(
        self,
        position: Point,
    ):
        super().__init__(
            categories=[Category.hero],
            color=Color("red"),
            position=position,
            width=HERO_SIZE,
            height=HERO_SIZE,
        )

    def set_moving(self, direction: Direction) -> None:
        if direction == Direction.left:
            self.velocity[0] = -HERO_SPEED
        elif direction == Direction.right:
            self.velocity[0] = HERO_SPEED
        elif direction == Direction.up:
            self.velocity[1] = -HERO_SPEED
        elif direction == Direction.down:
            self.velocity[1] = HERO_SPEED

    def stop_moving(self, orientation: Orientation) -> None:
        if orientation == Orientation.horizontal:
            self.velocity[0] = 0
        elif orientation == Orientation.vertical:
            self.velocity[1] = 0

    def draw_self(self, surface: Surface) -> None:
        self.draw_as_outline(surface)
