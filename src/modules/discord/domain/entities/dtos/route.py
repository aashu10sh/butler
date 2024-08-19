from dataclasses import dataclass
from typing import Callable
from discord.message import Message
from typing import Awaitable

ControllerFunctionType = Callable[[Message], Awaitable[None]]


@dataclass
class Route:
    command: str
    function: ControllerFunctionType
