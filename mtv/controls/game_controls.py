import pygame

from mtv.commands.move_hero import move_hero, stop_hero
from mtv.direction import Direction
from mtv.orientation import Orientation
from mtv.scene_node import SceneNode


def handle_keydown_event(key: int, world: SceneNode) -> None:
    if key == pygame.K_LEFT:
        world.handle_command(move_hero(direction=Direction.left))
    elif key == pygame.K_RIGHT:
        world.handle_command(move_hero(direction=Direction.right))
    elif key == pygame.K_UP:
        world.handle_command(move_hero(direction=Direction.up))
    elif key == pygame.K_DOWN:
        world.handle_command(move_hero(direction=Direction.down))


def handle_keyup_event(key: int, world: SceneNode) -> None:
    if key == pygame.K_LEFT:
        world.handle_command(stop_hero(orientation=Orientation.horizontal))
    if key == pygame.K_RIGHT:
        world.handle_command(stop_hero(orientation=Orientation.horizontal))
    if key == pygame.K_UP:
        world.handle_command(stop_hero(orientation=Orientation.vertical))
    if key == pygame.K_DOWN:
        world.handle_command(stop_hero(orientation=Orientation.vertical))
