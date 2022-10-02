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
"""

from json import load as load_json
from discord.ext import commands  # type: ignore
from typing import Dict, List
from discord import Object
from random import choice


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GenericCommandsCog(bot), guilds=[Object(id=938541999961833574)])


def get_generics_aliases(name: str) -> list[str]:
    with open(name, "r") as f:
        d: dict[str, list[str]] = load_json(f)

    return list(d)  # will only return the dict keys so {a: 0, b: 1,} as a list would be [a, b,]


class GenericCommandsCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command(aliases=[get_generics_aliases("D:\\programing\\0x102-discord-bot\\cogs\\generics\\notable.json")])
    async def notable_generics(self, ctx: commands.Context) -> None:
        with open("D:\\programing\\0x102-discord-bot\\cogs\\generics\\notable.json", "r") as f:
            command_data: Dict[str, List[str]] = load_json(f)

        # if the aliases is not a key in the dict
        if not ctx.invoked_with in command_data:
            return await ctx.send(f"don`t use {ctx.invoked_with}, did you make a typo?")

        # will get the command aliases that was used and then find it in the dict,
        # the dict will return alist of strings, one of these strings is chosen at
        # random and then sent
        await ctx.send(choice(command_data[ctx.invoked_with]))

    @commands.command(aliases=[get_generics_aliases("D:\\programing\\0x102-discord-bot\\cogs\\generics\\notable.json")])
    async def XXXXX_generics(self, ctx: commands.Context) -> None:
        with open("D:\\programing\\0x102-discord-bot\\cogs\\generics\\notable.json", "r") as f:
            ...
