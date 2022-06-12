import requests
from ._trivia_view import TriviaView
from discord.ext import commands
from discord import (
    Embed,
    Interaction,
    app_commands,
    Object
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        TriviaCog(bot),
        guilds=[Object(id=938541999961833574)]
    )


class TriviaCog(commands.Cog):
    def __init__(self: 'TriviaCog', bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name='trivia', description='starts a trivia game')
    async def trivia(self: 'TriviaCog', ctx: Interaction) -> None:
        """
         | `get_questions` is a coroutine that returns
         | `self` which is the class.
        """
        data: dict = requests.get('https://opentdb.com/api.php?amount=1').json()
        view: TriviaView = TriviaView(data['results'][0])

        await ctx.response.send_message(
            'ok',
            view=view,
            embed=Embed(
                title=f'Trivia: {data["results"][0]["question"]}',
                description='Select an answer',
                color=0x00ff00
            )
        )

    def __cog_docs__(self):
        return '''
        This cog is used to play trivia games.
        The commands are:
         - trivia
        '''
