from __future__ import annotations
from typing import final

from pygame.surface import Surface

from mtv.category import Category
from mtv.command import Command


class SceneNode:
    def __init__(self, categories: list[Category]) -> None:
        self.categories = categories
        self.children: list[SceneNode] = []
        self.rect = None

    @final
    def add_child(self, child: SceneNode) -> None:
        self.children.append(child)

    @final
    def remove_child(self, child: SceneNode) -> None:
        if child in self.children:
            self.children.remove(child)

    def update_self(self, _: float) -> None:
        pass

    def draw_self(self, _: Surface) -> None:
        pass

    @final
    def update(self, dt: float) -> None:
        self.update_self(dt)
        for child in self.children:
            child.update(dt)

    @final
    def draw(self, screen: Surface) -> None:
        self.draw_self(screen)
        for child in self.children:
            child.draw(screen)

    @final
    def handle_command(self, command: Command) -> None:
        if command.category in self.categories:
            command.action(self)
        else:
            for child in self.children:
                child.handle_command(command)

    @final
    def has_category(self, category: Category) -> bool:
        return category in self.categories

    @final
    def collides_with_scene_node(self, other: SceneNode) -> bool:
        if not self.rect or not other.rect:
            return False
        if self is other:
            return False
        return self.rect.colliderect(other.rect)

    @final
    def collisions_with_scene_node(self, other: SceneNode) -> list[SceneNode]:
        collisions = []
        if self.collides_with_scene_node(other):
            collisions.append(other)
        for child in other.children:
            if self.collides_with_scene_node(child):
                collisions.append(child)
        return collisions
