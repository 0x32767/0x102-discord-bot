import discord
from discord.ext import commands
from cache import cacheGet
from discord import (
    Interaction,
    app_commands,
    Object,
    Message
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        ServerCleanupCog(bot),
        guilds=[Object(id=cacheGet("id"))]
    )


class ServerCleanupCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self: "ServerCleanupCog", msg: Message) -> None:
        if msg.author.bot: return

        ...
