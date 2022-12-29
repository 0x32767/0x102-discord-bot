from discord import Interaction, app_commands, Object, Embed, Member
from db.api import give_item, give_item, get_item, get_all_items
from cogs._help_command_setup import record
from discord.ext import commands
from random import randint


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        ItemsCog(bot),
        guilds=[Object(id=938541999961833574)],
    )


class ItemsCog(commands.Cog):
    def __init__(self: "ItemsCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @record()
    @app_commands.command(description="dig for items")
    async def dig(self: "ItemsCog", ctx: Interaction) -> None:
        ...
        # await get_all_items(("", ""))
