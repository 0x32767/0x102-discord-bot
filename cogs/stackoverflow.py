from discord import Interaction, app_commands, Object
from cogs._help_command_setup import record
from discord.ext import commands
from httpx import Response
from cache import cacheGet


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(StackOverflowCog(bot), guilds=[Object(id=cacheGet("id"))])


class StackOverflowCog(commands.Cog):
    def __init__(self: "StackOverflowCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @record()
    @app_commands.command(description="get a stack overflow answer")
    async def stackoverflow(self: "StackOverflowCog", ctx: Interaction, *, question: str) -> None:
        # TODO: so something with the question
        res: Response = self.bot.httpx.get(
            f"https://api.stackexchange.com/2.3/search?order=desc&sort=votes&intitle={question}&site=stackoverflow"
        )
