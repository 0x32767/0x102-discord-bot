from discord.ext import commands
from discord import app_commands
import discord


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog()


class NSCog(commands.Cog):
    def __init__(self) -> None:
        super().__init__()
