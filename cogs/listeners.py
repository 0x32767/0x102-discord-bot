import discord
from discord.ext import commands
from discord.ext import tasks
from cache import cacheGet
from discord import (
    Interaction,
    app_commands,
    Object
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        CogListener(bot),
        guilds=[Object(id=cacheGet("id"))]
    )


class CogListener(commands.Cog):
    def __init__(self: "CogListener", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_message(self: "CogListener", message: discord.Message) -> None:...

    @tasks.loop(seconds=1)
    async def loop(self: "CogListener") -> None:
        for channel in self.bot.get_all_channels():
            if channel.type == discord.ChannelType.text:
                await self.check_channel(channel)

    async def check_channel(self: "CogListener", channel: discord.TextChannel) -> None:
        print(channel.history(limit=50).flatten())
