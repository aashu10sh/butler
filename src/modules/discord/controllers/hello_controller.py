from discord.message import Message


class HelloController:
    @staticmethod
    async def main(message: Message) -> None:
        await message.channel.send("pong")

