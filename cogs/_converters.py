import discord
from discord.ext import commands
from discord.ext.commands import Converter
from discord import (
    Interaction,
    app_commands,
    Object,
    Embed
)


class BooleanConverter(Converter):
    async def convert(self, ctx: Interaction, argument: str) -> bool:
        if argument.lower() == "true":
            return True
        elif argument.lower() == "false":
            return False
        else:
            raise commands.BadArgument(f"{argument} is not a valid boolean.")
