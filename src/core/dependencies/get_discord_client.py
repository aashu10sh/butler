from discord import Client, Intents


def get_discord_client() -> Client:
    intents = Intents.default()
    intents.message_content = True
    return Client(
        intents=intents,
    )
