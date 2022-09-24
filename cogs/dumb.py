"""

Copyright <10/08/2022> Han P.B Manseck

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject
to the following conditions:

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


Credits:
 - https://github.com/GeoffreyWesthoff/Dank-Memer

Credit goes to GeoffreyWesthoff for the inspiration for most of the
commands.
"""

from typing import Union
from discord import Interaction, app_commands, Object, Message, User, Embed
from cogs._help_command_setup import record # type: ignore
from discord.ext import commands
from cache import cacheGet
from json import load
import random


"""
::dump.py file::

The dumb.py file is a file that has some DankMemer commands, these commands don't
really add a lot to my bot but they are thing that seemed to make DankMemer more
popular so maby it will work for my bot.

::status::

The dumb.py file has not changed much in the way of usefulness but will be updated
every once in a while.

::todos::
"""
# TODO: finish adding dank memer commands


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DumbCommandsCog(bot), guilds=[Object(id=cacheGet("id"))])


class DumbCommandsCog(commands.Cog):
    def __init__(self: "DumbCommandsCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @record()
    @app_commands.command(description="shows the durp-score of someone")
    @app_commands.describe(user="who's durp-score you want to see")
    async def durpscore(self: "DumbCommandsCog", ctx: Interaction, user: User) -> None:
        if user:
            return await ctx.response.send_message(f"{user.mention} has a durp-score of `{user.id % 100}`")

        # TODO: finish this command
        return None

    @record()
    @app_commands.command(description="click the link")
    async def rr(self: "DumbCommandsCog", ctx: Interaction) -> None:
        return await ctx.response.send_message(embed=await self._get_rick_roll())

    @staticmethod
    async def _get_rick_roll() -> Embed:
        with open("D:\\programing\\0x102-discord-bot\\assets\\rickRolls.json", "r") as f:
            rick_rolls: list[dict[str, str]] = load(f)

        rr_info: dict[str, str] = random.choice(rick_rolls)

        return Embed(title=rr_info["Excuse"], url=rr_info["Link"])
