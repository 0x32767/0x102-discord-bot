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


from discord import Interaction, app_commands, Object, Embed
from cogs._help_command_setup import record # type: ignore
from discord.ext import commands
from httpx import Response
from cache import cacheGet


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(StackOverflowCog(bot), guilds=[Object(id=938541999961833574)])


class StackOverflowCog(commands.Cog):
    def __init__(self: "StackOverflowCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @record()
    @app_commands.command(description="get a stack overflow answer")
    async def stackoverflow(self: "StackOverflowCog", ctx: Interaction, *, question: str) -> None:
        res: Response = self.bot.httpx.get(
            f"https://api.stackexchange.com/2.3/search?order=desc&sort=votes&intitle={question}&site=stackoverflow"
        )

        ans: dict[
            str,
            list[str] | str | int | dict[
                str,
                int | str
            ]
        ] = res.json()["items"][0]

        del res

        em: Embed = Embed(
            title=f"{ans['title']}",
            description=f"is this what you are looking for, with \"{question}\""
        )

        em.add_field(
            name="up votes",
            value=f"{ans['score']}"
        )

        em.url = f"{ans['ink']}#{ans['accepted_answer_id']}"

        await ctx.response.send_message(embed=em)
