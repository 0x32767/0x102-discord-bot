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

from discord import Interaction, app_commands, Object, Message, User, Embed
from usefull.textDecorations import progressBar
from hashlib import sha256, sha1, md5
from discord.ext import commands
import cogs._helpCommandSetup
from typing import Generator
from cache import cacheGet
from json import load
import asyncio
import random


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DumbCommandsCog(bot), guilds=[Object(id=cacheGet("id"))])


class DumbCommandsCog(commands.Cog):
    def __init__(self: "DumbCommandsCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="shows the durp-score of someone")
    @app_commands.describe(user="who's durp-score you want to see")
    async def durpscore(self: "DumbCommandsCog", ctx: commands.Context, user: Interaction) -> None | Message:
        if user:
            await ctx.send(f"{user.mention} has a durp-score of `{user.id % 100}`")

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="get a users discord token")
    @app_commands.describe(user="who's token you want to see")
    async def hack(self: "DumbCommandsCog", ctx: Interaction, user: User) -> None:
        with open("D:\\programing\\0x102-discord-bot\\assets\\hackMessages.json", "r") as f:
            messages: dict[str, list[str]] = load(f)

        dec: Generator[str] = progressBar(messages["updates"], messages["errors"])
        msg: Message = await ctx.response.send_message()

        for msg in dec:
            await msg.edit(content=msg)
            await asyncio.sleep(0.1)
        msg.edit(content=f"{user.mention} has a token of `{await self._dummyHash(user)}`")

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="click the link")
    async def rr(self: "DumbCommandsCog", ctx: Interaction) -> Embed:
        return await ctx.response.send_message(embed=await self._getRickRoll())

    async def _dummyHash(self: "DumbCommandsCog", user: User) -> str:
        return f'{sha256(user.id.to_bytes(8, "big")).hexdigest()}.{sha1(user.id.to_bytes(8, "big")).hexdigest()}.{md5(user.id.to_bytes(8, "big")).hexdigest()}'

    async def _getRickRoll(self: "DumbCommandsCog") -> Embed:
        with open("D:\\programing\\0x102-discord-bot\\assets\\rickRolls.json", "r") as f:
            rickRolls: list[dict[str, str]] = load(f)

        rrInfo: dict[str, str] = random.choice(rickRolls)

        return Embed(title=rrInfo["Excuse"], url=rrInfo["Link"])
