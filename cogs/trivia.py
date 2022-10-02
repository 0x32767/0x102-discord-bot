"""
Copyright (C) 23/07/2022 - Han P.B Manseck.

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from discord import Embed, Interaction, app_commands, Object
from cogs._help_command_setup import record  # type: ignore
from cogs.ui._triviaView import TriviaView  # type: ignore
from aiohttp import ClientSession
from discord.ext import commands  # type: ignore


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(TriviaCog(bot), guilds=[Object(id=938541999961833574)])


class TriviaCog(commands.Cog):
    def __init__(self: "TriviaCog", bot: commands.Bot) -> None:
        self.cs: ClientSession = ClientSession()
        self.bot: commands.Bot = bot

    @record()
    @app_commands.command(name="trivia", description="starts a trivia game")
    async def trivia(self: "TriviaCog", ctx: Interaction) -> None:
        """
        | `get_questions` is a coroutine that returns
        | `self` which is the class.
        """
        req = await self.cs.get("https://opentdb.com/api.php?amount=1&type=multiple")
        data: dict = await req.json()

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
