import discord
import aiosqlite
from discord.ext import commands
from ._comand_chache import register_commands
from discord import (
    Interaction,
    app_commands,
    Object,
    Embed
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        LevelsCog(bot),
        guilds=[Object(id=938541999961833574)]
    )


class LevelsCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        register_commands(self)
        self.bot = bot

    @app_commands.command()
    @app_commands.describe()
    async def levleinfo(self, ctx: Interaction) -> None:
        async with aiosqlite.connect('discordbotdb.db') as data:
            async with data.cursor() as curr:
                await curr.execute(
                    "select * from levels where guild_id = {} and user_id = {}".format(ctx.user.id, ctx.guild.id))
                em = Embed(title=f'{ctx.user.name}\'s progress')
                # the `_` are the user and guild's ids, we don't need these in the mebed
                for val, key in zip(list(await curr.fetchall())[0], ['_', '_', 'levle', 'exp']):
                    if key == '_':
                        continue

                    em.add_field(name=key, value=val)

                await ctx.response.send_message(embed=em)

    """
     | The code below updates the user's levels
    """

    async def get_attr(self, guild_id, user_id, attr) -> int:
        async with aiosqlite.connect("discordbotdb.db") as database:
            async with database.cursor() as curr:
                await curr.execute(
                    'select * from levels where user_id = {} and guild_id = {}'.format(guild_id, user_id))
                data = await curr.fetchall()
                return int(data[0][attr])

    async def update_exp(self, guild_id, user_id, exp_g):
        async with aiosqlite.connect("discordbotdb.db") as database:
            async with database.cursor() as curr:
                await curr.execute(
                    'select * from levels where user_id = {} and guild_id = {}'.format(guild_id, user_id))
                data = await curr.fetchone()
                exp = data[3] + exp_g

                await curr.execute(
                    'update levels set exp = {} where user_id = {} and guild_id = {}'.format(exp, guild_id, user_id)
                )

            await database.commit()

            return exp

    async def reset_exp(self, guild_id, user_id):
        async with aiosqlite.connect("discordbotdb.db") as database:
            async with database.cursor() as curr:
                await curr.execute(
                    'update levels set exp = 0 where guild_id = {} and user_id = {}'.format(guild_id, user_id)
                )

            await database.commit()

    async def update_level(self, guild_id, user_id, lev_g):
        async with aiosqlite.connect("discordbotdb.db") as database:
            async with database.cursor() as curr:
                lev = await self.get_attr(guild_id, user_id, 2) + lev_g

                await curr.execute(
                    'update levels set level = {} where user_id = {} and guild_id = {}'.format(lev, guild_id, user_id)
                )

            await database.commit()

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return

        level = await self.get_attr(message.guild.id, message.author.id, 2)
        exp = await self.get_attr(message.guild.id, message.author.id, 3)

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

    def __cog_docs__(self) -> str:
        return """
        The Cog that adds exp and levels to your account.
        You can also see your current level and exp with:
        -`levleinfo`
        """
