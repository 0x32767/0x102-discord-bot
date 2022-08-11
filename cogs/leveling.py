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


from discord import Interaction, app_commands, Object, Embed, Message, User
from aiosqlite import connect, Connection
from discord.ext import commands
import cogs._helpCommandSetup
from cache import cacheGet


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(LevelingCog(bot), guilds=[Object(id=cacheGet("id"))])


class LevelingCog(commands.Cog):
    def __init__(self: "LevelingCog", bot: commands.Bot) -> None:
        self.con: Connection = connect("D:\\programing\\0x102-discord-bot\\assets\\leveling.db")
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_message(self: "LevelingCog", message: Message) -> None:
        if message.author.bot:
            return

        await self._update(message.author)

    async def _incrementLevel(self: "LevelingCog", user: User) -> None:
        async with self.con.cursor() as cur:
            await cur.execute("UPDATE leveling SET level = level + 1 WHERE id = ?", (user.id,))
            await self.con.commit()

    async def _incrementXP(self: "LevelingCog", user: User) -> None:
        async with self.con.cursor() as cur:
            await cur.execute("UPDATE leveling SET xp = xp + 5 WHERE id = ?", (user.id,))
            await self.con.commit()

    async def _getLevel(self: "LevelingCog", user: User) -> int:
        async with self.con.cursor() as cur:
            await cur.execute("SELECT level FROM leveling WHERE id = ?", (user.id,))
            return await cur.fetchone()[0]

    async def _getXP(self: "LevelingCog", user: User) -> int:
        async with self.con.cursor() as cur:
            await cur.execute("SELECT xp FROM leveling WHERE id = ?", (user.id,))
            return await cur.fetchone()[0]

    async def _resetXP(self: "LevelingCog", user: User) -> None:
        async with self.con.cursor() as cur:
            await cur.execute("UPDATE leveling SET xp = 0 WHERE id = ?", (user.id,))
            await self.con.commit()

    async def _update(self: "LevelingCog", user: User) -> None:
        level: int = await self._getLevel(user)
        xp: int = await self._getXP(user)

        if xp == level * 5:
            await self._incrementLevel(user)
            await self._resetXP(user)

        await self._incrementXP(user)

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="you can see your current level and xp")
    async def level(self: "LevelingCog", ctx: Interaction):
        level: int = await self._getLevel(ctx.author)
        xp: int = await self._getXP(ctx.author)

        await ctx.response.send_message(
            embed=Embed(title=f"{ctx.author.name}'s Level", description="see how much xp and level you have", color=0x00FF00)
            .add_field(name="Level", value=level, inline=True)
            .add_field(name="XP", value=xp, inline=True)
        )

    @cogs._helpCommandSetup.record()
    @app_commands.command(name="levelup", description="level up a user")
    @app_commands.describe(user="the user to level up")
    @app_commands.describe(amount="how many levels to level up the user")
    @app_commands.describe(reason="the reason for leveling up the user")
    async def level_up(self: "LevelingCog", ctx: Interaction, user: User, amount: int = 1, *, reason: str = "no reason"):
        for _ in range(amount):
            await self._incrementLevel(user)

        await ctx.response.send_message(
            embed=Embed(title=f"{user.name} has leveled up", description=f"{reason}", color=0x00FF00).add_field(
                name="Level", value=await self._getLevel(user), inline=True
            )
        )
