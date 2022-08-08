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


from discord import Interaction, Member, app_commands, Object, Embed
from cogs._profanity import check_raw
from discord.ext import commands
import cogs._helpCommandSetup
from cache import cacheGet


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ProfanityReport(bot), guilds=[Object(id=cacheGet("id"))])


class ProfanityReport(commands.Cog):
    def __init__(self: "ProfanityReport", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @cogs._helpCommandSetup.record("/report <message>")
    @app_commands.command(name="report", description="Report a profanity message.")
    @app_commands.describe(user="Who the message is from.")
    @app_commands.describe(message="The message to report.")
    async def report(self: "ProfanityReport", ctx: Interaction, user: Member, message: str) -> None:
        if check_raw(message):
            await ctx.send(
                Embed(
                    title="Profanity Report",
                    description=f"{user.mention} has reported a profanity message.",
                    color=0xFF0000,
                )
            )
        else:
            await ctx.send(
                Embed(
                    title="Profanity Report",
                    description=f"{user.mention} has reported a non-profanity message.",
                    color=0x00FF00,
                )
            )
