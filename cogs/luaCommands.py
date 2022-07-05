from cache import cacheGet
from discord.ext import commands
import aiosqlite
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
    async def runcommand(self: "LuaCog", ctx: Interaction) -> None:
        async with aiosqlite.connect("D:\\programing\\0x102-discord-bot\\commands.db") as db:
            async with db.cursor() as curr:
                await curr.execute("SELECT ",)

    @app_commands.command()
    async def inspectcommand(self: "LuaCog", ctx: Interaction) -> None:...
