from discord.message import Message

from src.modules.discord.router.router import DiscordRouter

router = DiscordRouter()


async def run_application(message: Message) -> None:
    for route in await router.routes():
        if message.content.startswith(route.command):
            await route.function(message)
