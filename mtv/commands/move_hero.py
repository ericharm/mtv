from mtv.category import Category
from mtv.command import Command
from mtv.direction import Direction
from mtv.orientation import Orientation


def move_hero(direction: Direction) -> Command:
    return Command(
        category=Category.hero,
        action=lambda hero: hero.set_moving(direction),
    )


def stop_hero(orientation: Orientation) -> Command:
    return Command(
        category=Category.hero,
        action=lambda hero: hero.stop_moving(orientation),
    )
