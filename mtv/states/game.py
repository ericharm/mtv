import pygame
from pygame.color import Color
from pygame.event import Event
from pygame.surface import Surface

from mtv.category import Category
from mtv.command import EntityCommand
from mtv.controls import game_controls
from mtv.entities.hero import Hero
from mtv.entities.platform import Platform
from mtv.point import Point
from mtv.scene_node import SceneNode
from mtv.state import State


class Game(State):
    def __init__(self) -> None:
        self.done = False
        self.scene = SceneNode(categories=[Category.world])
        hero = Hero(position=Point(200, 90))
        platform = Platform(position=Point(100, 400), width=200, height=50)
        self.scene.add_child(hero)
        self.scene.add_child(platform)

    def draw(self, screen: Surface) -> None:
        screen.fill(Color("gray20"))
        self.scene.draw(screen)

    def update(self, deltatime: float) -> None:
        self.handle_collisions()
        self.scene.update(deltatime)

    def handle_events(self, events: list[Event]) -> None:
        for event in events:
            if event.type == pygame.QUIT:
                self.done = True

            if event.type == pygame.KEYDOWN:
                game_controls.handle_keydown_event(event.key, self.scene)

            if event.type == pygame.KEYUP:
                game_controls.handle_keyup_event(event.key, self.scene)

    def handle_collisions(self) -> None:
        collisions = self.find_collisions()
        for collision in collisions:
            if collision[0].has_category(Category.hero) and collision[1].has_category(
                Category.platform
            ):
                command = EntityCommand(
                    category=Category.hero,
                    action=(lambda hero: hero.set_on_ground(True)),
                )
                self.scene.handle_command(command)

    def find_collisions(self) -> list[tuple[SceneNode, SceneNode]]:
        collisions = []
        for child in self.scene.children:
            child_collisions = child.collisions_with_scene_node(self.scene)
            for collision in child_collisions:
                if not (collision, child) in collisions:
                    collisions.append((child, collision))
        # collisions.sort(key=lambda x: x[0].categories)
        return collisions
