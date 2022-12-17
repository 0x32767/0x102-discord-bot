from discord import Interaction, app_commands, Object, Embed
from cogs._help_command_setup import record
from discord.ext import commands


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(TextAdventureCog(bot), guilds=[Object(id=938541999961833574)])


class TextAdventureCog(commands.Cog):
    def __init__(self: "TextAdventureCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
