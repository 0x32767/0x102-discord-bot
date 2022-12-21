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


from discord import Interaction, app_commands, Object, User
from cogs._help_command_setup import record  # type: ignore
from discord.ext import commands  # type: ignore
from aiosqlite import connect


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ReputationCog(bot), guilds=[Object(id=938541999961833574)])


# TODO: make more advanced, give reputation, take away reputation, have a upvote and down vote system.


class ReputationCog(commands.Cog):
    def __init__(self: "ReputationCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @record()
    @app_commands.command(description="see how much reputation you have")
    async def reputation(self: "ReputationCog", ctx: Interaction):
        async with connect("discordbotdb.db") as db:
            async with db.execute("SELECT reputation FROM users WHERE id = ?", (ctx.user.id,)) as cursor:
                res = await cursor.fetchone()

                if res is None:
                    await ctx.response.send_message("you have no reputation")
                    return

                await ctx.response.send_message(f"you have {res[0]} reputation")

    @record()
    @app_commands.command(description="give someone reputation")
    @app_commands.describe(user="Who you want to give reputation to")
    @app_commands.describe(amount="how much reputation you want to give")
    @commands.has_permissions(administrator=True)
    async def give(self: "ReputationCog", ctx: Interaction, user: User, amount: int) -> None:
        async with connect("discordbotdb.db") as db:
            async with db.execute("SELECT reputation FROM users WHERE id = ?", (user.id,)) as cursor:
                res = await cursor.fetchone()

                if res is None:
                    await ctx.response.send_message("that user has no reputation")
                    return

                await db.execute("UPDATE users SET reputation = ? WHERE id = ?", (res[0] + amount, user.id))
                await ctx.response.send_message(
                    f"you have given {user.name} {amount} reputation, and they now have {res[0] + amount}"
                )
