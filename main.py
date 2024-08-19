from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
from src.core.dependencies.get_discord_client import get_discord_client
from discord.message import Message

client = get_discord_client()


@client.event
async def on_ready():
    print(f"We have Logged in as ! {client.user}")


@client.event
async def on_message(message: Message):
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")


print(os.getenv("DISCORD_APPLICATION_ID"))

client.run(token=os.getenv("DISCORD_APP_TOKEN") or "")
