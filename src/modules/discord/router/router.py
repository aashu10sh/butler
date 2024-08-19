from typing import List

from src.modules.discord.controllers import HelloController
from src.modules.discord.domain.entities.dtos.route import Route


class DiscordRouter:
    async def routes(
        self,
    ) -> List[Route]:
        return [Route(command="/ping", function=HelloController.main)]
