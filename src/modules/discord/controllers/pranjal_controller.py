from discord.message import Message
class PranjalController:
    @staticmethod
    async def main(message : Message) -> None: 
        await message.channel.send("Pranjal My Goat")
        