from ._triviaView import TriviaView
from aiohttp import ClientSession
from discord.ext import commands
import cogs._helpCommandSetup
from cache import cacheGet
from discord import Embed, Interaction, app_commands, Object


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(TriviaCog(bot), guilds=[Object(id=cacheGet("id"))])


class TriviaCog(commands.Cog):
    def __init__(self: "TriviaCog", bot: commands.Bot) -> None:
        self.cs: ClientSession = ClientSession()
        self.bot: commands.Bot = bot

    @cogs._helpCommandSetup.record()
    @app_commands.command(name="trivia", description="starts a trivia game")
    async def trivia(self: "TriviaCog", ctx: Interaction) -> None:
        """
        | `get_questions` is a coroutine that returns
        | `self` which is the class.
        """
        req = await self.cs.get("https://opentdb.com/api.php?amount=1&type=multiple")
        data: dict = req.json()

        view: TriviaView = TriviaView(data["results"][0])

        await ctx.response.send_message(
            view=view,
            embed=Embed(
                title=f'Trivia: {data["results"][0]["question"]}',
                description="Select an answer",
                color=0x00FF00,
            ),
        )

        del req, data
