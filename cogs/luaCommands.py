from cogs._luaTextModal import LuaTextEditorModal

from cache import cacheGet
from discord.ext import commands
from discord import (
    Interaction,
    app_commands,
    Object
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        LuaCog(bot),
        guilds=[Object(id=cacheGet("id"))]
    )


class LuaCog(commands.Cog):
    def __init__(self: "LuaCog", bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command()
    async def newcommand(self: "LuaCog", ctx: Interaction) -> None:
        await ctx.response.send_modal(LuaTextEditorModal())

    @app_commands.command()
    async def runcommand(self: "LuaCog", ctx: Interaction) -> None:
        ...
