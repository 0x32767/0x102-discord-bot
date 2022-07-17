import discord
import aiosqlite
from discord.ext import commands
from cache import cacheGet
import cogs._helpCommandSetup
from discord import (
    Interaction,
    app_commands,
    Object,
    Embed
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        LevelsCog(bot),
        guilds=[Object(id=cacheGet("id"))]
    )


class LevelsCog(commands.Cog):
    def __init__(self: "LevelsCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Gets your current level.")
    async def levleinfo(self: "LevelsCog", ctx: Interaction) -> None:
        async with aiosqlite.connect("discordbotdb.db") as data:
            async with data.cursor() as curr:
                await curr.execute(f"select * from levels where guild_id = {ctx.user.id} and user_id = {ctx.guild.id}")

                em: Embed = Embed(title=f"{ctx.user.name}\'s progress")
                # the `_` are the user and guild's ids, we don't need these in the mebed
                for val, key in zip(list(await curr.fetchall())[0], ["_", "_", "levle", "exp"]):
                    if key == "_":
                        continue

                    em.add_field(name=key, value=val)

                await ctx.response.send_message(embed=em)

    """
     | The code below updates the user's levels
    """

    async def get_attr(self: "LevelsCog", guild_id: int, user_id: int, attr: int) -> int:
        async with aiosqlite.connect("discordbotdb.db") as database:
            async with database.cursor() as curr:
                await curr.execute(f"select * from levels where user_id = {guild_id} and guild_id = {user_id}")

                data: list[tuple] = await curr.fetchall()
                return int(data[0][attr])

    async def update_exp(self: "LevelsCog", guild_id: int, user_id: int, exp_g: int) -> int:
        async with aiosqlite.connect("discordbotdb.db") as database:
            async with database.cursor() as curr:
                await curr.execute(f"select * from levels where user_id = {guild_id} and guild_id = {user_id}")

                data: tuple = await curr.fetchone()
                exp: int = data[3] + exp_g

                await curr.execute(f"update levels set exp = {exp} where user_id = {guild_id} and guild_id = {user_id}")

            await database.commit()

            return exp

    async def reset_exp(self: "LevelsCog", guild_id: int, user_id: int) -> None:
        async with aiosqlite.connect("discordbotdb.db") as database:
            async with database.cursor() as curr:
                await curr.execute(f"update levels set exp = 0 where guild_id = {guild_id} and user_id = {user_id}")

            await database.commit()

    async def update_level(self: "LevelsCog", guild_id: int, user_id: int, lev_g: int) -> None:
        async with aiosqlite.connect("discordbotdb.db") as database:
            async with database.cursor() as curr:
                lev: int = await self.get_attr(guild_id, user_id, 2) + lev_g
                await curr.execute(f"update levels set level = {lev} where user_id = {guild_id} and guild_id = {user_id}")

            await database.commit()

    @commands.Cog.listener()
    async def on_message(self: "LevelsCog", message: discord.Message):
        if message.author == self.bot.user:
            return

        level: int = await self.get_attr(message.guild.id, message.author.id, 2)
        exp: int = await self.get_attr(message.guild.id, message.author.id, 3)

        if level * 4 <= exp:
            await self.reset_exp(message.guild.id, message.author.id)
            await self.update_level(
                guild_id=message.guild.id,
                user_id=message.author.id,
                # increments the level by 1
                lev_g=level + 1
            )

        else:
            await self.update_exp(message.guild.id, message.author.id, 5)
            await self.update_level(message.guild.id, message.author.id, 0)
