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

THE SOFTWARE IS PROVIDED "A0S IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from discord.ext import commands
from aiosqlite import connect as sql_conn
from discord import Object, Message, User
from asyncio import sleep as async_sleep
from random import randint


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DecryptCog(bot), guilds=[Object(id=938541999961833574)])


class DecryptCog(commands.Cog):
    def __init__(self: "DecryptCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message) -> None:
        # a 1 in 10,000 change
        if not randint(0, 10_000):
            message.add_reaction("")
            async_sleep(0.5)
            user = message.reactions[0].users[0] # the first person to react

            await message.channel.send(f"{user.mention} has found the easter egg")
            await self.reward_easter_egg(message.guild.id, user)

    async def reward_easter_egg(self, guild_id: int, user: User) -> None:
        async with sql_conn("") as conn:
            async with conn.currsor() as curr:
                await curr.execute("SELECT * FROM mod_channels WHERE guild_id = ?;", (guild_id,))
                (await curr.fetchone())
