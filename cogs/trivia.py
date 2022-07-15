import cogs._helpCommandSetup
from ._triviaView import TriviaView
from discord.ext import commands
from cache import cacheGet
import requests
from discord import (
    Embed,
    Interaction,
    app_commands,
    Object
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        TriviaCog(bot),
        guilds=[Object(id=cacheGet("id"))]
    )


class TriviaCog(commands.Cog):
    def __init__(self: "TriviaCog", bot: commands.Bot) -> None:
        self.bot = bot

    @cogs._helpCommandSetup.record()
    @app_commands.command(name="trivia", description="starts a trivia game")
    async def trivia(self: "TriviaCog", ctx: Interaction) -> None:
        """
         | `get_questions` is a coroutine that returns
         | `self` which is the class.
        """
        data: dict = requests.get("https://opentdb.com/api.php?amount=1").json()
        view: TriviaView = TriviaView(data["results"][0])

        await ctx.response.send_message(
            view=view,
            embed=Embed(
                title=f'Trivia: {data["results"][0]["question"]}',
                description="Select an answer",
                color=0x00ff00
            )
        )
