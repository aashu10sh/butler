from dataclasses import dataclass
from typing import Callable, Any


@dataclass
class Route:
    command: str
    function: Callable[[Any], None]
