from discord import Interaction, app_commands, Object, Embed
from discord.ext import commands
import cogs._helpCommandSetup
from httpx import Response
from pyquery import PyQuery
from cache import cacheGet
from lxml import etree


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(StackOverflowCog(bot), guilds=[Object(id=cacheGet("id"))])


class StackOverflowCog(commands.Cog):
    def __init__(self: "StackOverflowCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="get a stack overflow answer")
    async def stackoverflow(self: "StackOverflowCog", ctx: Interaction, *, question: str) -> None:
        # TODO: so something with the question
        res: Response = self.bot.httpx.get(
            f"https://api.stackexchange.com/2.3/search?order=desc&sort=votes&intitle={question}&site=stackoverflow"
        )
