from abc import ABC, abstractmethod

from attr import define
from pygame.event import Event
from pygame.surface import Surface


@define(auto_attribs=True)
class State(ABC):
    """
    A state is a layer of the application with its own rendering and input handling.
    """

    @abstractmethod
    def draw(self, screen: Surface) -> None:
        pass

    @abstractmethod
    def update(self, deltatime: float) -> None:
        pass

    @abstractmethod
    def handle_events(self, events: list[Event]) -> None:
        pass
