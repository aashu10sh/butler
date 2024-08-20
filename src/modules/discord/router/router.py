from typing import List

from src.modules.discord.controllers import HelloController
from src.modules.discord.controllers import SamratController
from src.modules.discord.controllers import PranjalController
from src.modules.discord.domain.entities.dtos.route import Route


class DiscordRouter:
    async def routes(
        self,
    ) -> List[Route]:
        return [
            Route(
                command="/ping",
                function=HelloController.main,
            ),
            Route(
                command="/samrat",
                function=SamratController.main
            ),
            Route(
                command="/pranjal",
                function=PranjalController.main
            )
        ]
