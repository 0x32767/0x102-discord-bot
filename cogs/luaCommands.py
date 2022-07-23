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


from discord.ext import commands
import cogs._helpCommandSetup
from hashlib import sha256
from cache import cacheGet
from cogs._lua import run
from random import random
import aiosqlite
from discord import (
    Interaction,
    app_commands,
    Object,
    Embed,
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(LuaCog(bot), guilds=[Object(id=cacheGet("id"))])


class LuaCog(commands.Cog):
    def __init__(self: "LuaCog", bot: commands.Bot) -> None:
        self.bot = bot

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Runs a Lua command.")
    @app_commands.describe(name="The name of the command you want to run.")
    async def runcommand(self: "LuaCog", ctx: Interaction, name: str = "echo") -> None:
        if not name:
            return await ctx.response.send_message("Please provide a command name.")

        async with aiosqlite.connect(
            "D:\\programing\\0x102-discord-bot\\commands.db"
        ) as db:
            async with db.cursor() as curr:
                await curr.execute(f'SELECT code FROM commands WHERE name = "{name}"')
                result = await curr.fetchone()
                await run(result[0], ctx)

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Lets you see the code of a command.")
    @app_commands.describe(name="The name of the command you want to inspect.")
    async def inspectcommand(
        self: "LuaCog", ctx: Interaction, name: str = "echo"
    ) -> None:
        async with aiosqlite.connect(
            "D:\\programing\\0x102-discord-bot\\commands.db"
        ) as db:
            async with db.cursor() as curr:
                await curr.execute(f'SELECT code FROM commands where name = "{name}"')
                result = await curr.fetchall()
                return await ctx.response.send_message(f"```lua\n{result[0][0]}\n```")

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Creates a new command.")
    @app_commands.describe(name="The name of the command you want to create.")
    async def newcommand(self: "LuaCog", ctx: Interaction, name: str) -> None:
        key: str = sha256(f"{random()}".encode("utf-8")).hexdigest()

        async for msg in ctx.channel.history(limit=10):
            if msg.author.id == ctx.user.id:
                async with aiosqlite.connect(
                    "D:\\programing\\0x102-discord-bot\\commands.db"
                ) as db:
                    async with db.cursor() as curr:
                        curr.execute(
                            "INSERT INTO waitingList VALUES(?, ?, ?, ?)",
                            (key, name, msg.id, msg.content),
                        )
                        await db.commit()
                await db.close()

        return await ctx.response.send_message(
            embed=Embed(
                title="Command added to waiting list",
                description="The command will be added to the waiting list when it is ready.",
                url="",
            ).add_field(
                name="id",
                value=key,
            )
        )
