from dataclasses import dataclass
from typing import Callable

from mtv.category import Category


@dataclass
class Command:
    category: Category
    action: Callable


@dataclass
class EntityCommand(Command):
    category: Category
    action: Callable
