from src.modules.discord.domain.entities.dtos.route import Route
from src.modules.discord.controllers import HelloController
from typing import List


class DiscordRouter:
    async def routes(
        self,
    ) -> List[Route]:
        return [Route(command="/ping", function=HelloController.main)]
