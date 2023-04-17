from typing import Callable, Optional
from pygame import Color
import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface


from enum import Enum


class Category(Enum):
    world = 0
    player = 1
    platform = 2
    enemy = 3
    # Add more categories as needed


class Command:
    def __init__(self, category, payload: Optional[Callable] = None) -> None:
        self.category = category
        self.payload = payload


class SceneNode:
    def __init__(self, category):
        self.category = category
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)

    def update_self(self, dt: float) -> None:
        # Implement logic for updating this SceneNode
        pass

    def draw_self(self, screen: Surface) -> None:
        # Implement logic for drawing this SceneNode on the screen
        pass

    def update(self, dt: float) -> None:
        self.update_self(dt)
        for child in self.children:
            child.update(dt)
        pass

    def draw(self, screen: Surface) -> None:
        self.draw_self(screen)
        for child in self.children:
            child.draw(screen)
        pass

    def handle_command(self, command: Command) -> None:
        if self.category == command.category:
            self.process_command(command)
        else:
            for child in self.children:
                child.handle_command(command)

    def process_command(self, command: Command) -> None:
        # Implement logic for processing commands for this SceneNode
        pass


class Entity(SceneNode):
    def __init__(
        self,
        category: Category,
        sprite: Sprite,
        color: Color,
        # x: float,
        # y: float,
        width: float,
        height: float,
        velocity_x: float = 0.0,
        velocity_y: float = 0.0,
    ):
        super().__init__(category)
        sprite = sprite
        image = Surface([width, height])
        image.fill(color)
        self.image = image
        self.rect = image.get_rect()
        # self.screen = pygame.display.get_surface()

        # self.color = color
        # self.rect: Rect = Rect(x, y, width, height)
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def draw(self, surface: Surface) -> None:
        # Render rect to the Surface with fill color as Entity's color
        # self.screen = pygame.display.get_surface()
        # screen = pygame.display.get_surface()
        # player.screen.blit(player.image, player.rect)

        surface.blit(self.image, self.rect)


if __name__ == "__main__":
    world = SceneNode(Category.world)
    world.add_child(Entity(Category.player, Sprite(), Color("red"), 100, 100))
    world.update(0.0)

    pygame.init()
    pygame.display.set_caption("mtv")

    surface = pygame.display.get_surface()
    world.draw(surface)
    # game = Game()
    # run_game(game)
