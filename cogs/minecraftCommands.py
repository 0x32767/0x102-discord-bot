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


import cogs._helpCommandSetup
from discord.ext import commands
from cache import cacheGet
import random
import json
from discord import Interaction, app_commands, Object, Member


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MinecrtaftCog(bot), guilds=[Object(id=cacheGet("id"))])


class MinecrtaftCog(commands.Cog):
    def __init__(self: "MinecrtaftCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Kill a user or yourself.")
    @app_commands.describe(player="The member you want to kill.")
    async def kill(self: "MinecrtaftCog", ctx: Interaction, player: Member = None) -> None:
        """
        :param ctx: The ctx param is passes by the discord.py libruary
        :param player: The player that is killed
        :return:
        """
        with open("assets/deathMessages.json", "r") as f:
            data: dict[str, list[str]] = json.load(f)

        if player is None:
            await ctx.response.send_message(random.choice(data["self"]).replace("{player}", ctx.user.mention))

        else:
            await ctx.response.send_message(
                random.choice(data["other"]).replace("{player}", player.mention).replace("{killer}", ctx.user.mention)
            )

        del data
