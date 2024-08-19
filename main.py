import os

from dotenv import load_dotenv

load_dotenv()
from discord.message import Message

from src import run_application
from src.core.dependencies.get_discord_client import get_discord_client

client = get_discord_client()


@client.event
async def on_ready():
    print(f"We have Logged in as ! {client.user}")


@client.event
async def on_message(message: Message):
    await run_application(message=message)


client.run(token=os.getenv("DISCORD_APP_TOKEN") or "")
