from discord.ext import commands
from discord import Object, Interaction, app_commands
from cogs._crete_generic_help_command import record
from cache import cacheGet
from typing import Callable, Any


async def setup(bot: commands.Bot) -> None:
    await bot.load_cog(
        GenericCommandsCog(bot),
        guilds=[Object(id=000000000)]
    )


class GenericCommandsCogMeta(type):
    def __new__(cls, name: str, bases: tuple[str], attrs: dict[str, Callable[[Any], Any]]):
        ...


class GenericCommandsCog(mettaclass=GenericHelpCommandsCogMeta):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

