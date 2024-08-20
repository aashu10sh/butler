from discord.message import Message


class SamratController:
    @staticmethod
    async def main(message: Message) -> None:
        print(await message.channel.send("Yo Samrat, What's up?"))
