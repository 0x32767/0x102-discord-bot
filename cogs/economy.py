import discord
import aiosqlite
from random import uniform
from discord.ext import commands, tasks
from discord import (
    Embed,
    Interaction,
    app_commands,
    Object
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        EconomeyCog(bot),
        guilds=[Object(id=938541999961833574)]
    )


class EconomeyCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name='stonks', description='shows the value of the server an your account')
    async def stonks(self, ctx: Interaction) -> None:
        async with aiosqlite.connect('stonks.db') as db:
            async with db.cursor() as curr:
                em = Embed(
                    title='Stonks',
                    description='Use `/stonks` and then the name of the command to learn more about it.'
                )

                await curr.execute(
                    'SELECT * FROM server_stonks WHERE guild_id = {}'.format(
                        ctx.guild.id
                    )
                )
                data = await curr.fetchone()

                em.add_field(
                    name='Server Currency',
                    value=data[1]
                )
                em.add_field(
                    name='worth',
                    value=f"{data[2]}"
                )
                em.add_field(
                    name='Your Stonks',
                    value=0
                )

                await ctx.response.send_message(embed=em)
    
    @app_commands.command(name='topstonks', description='shows the top 20 stonks')
    async def topstonks(self, ctx: Interaction) -> None:
        async with aiosqlite.connect('stonks.db') as db:
            async with db.cursor() as curr:
                em = Embed(
                    title='Top Stonks',
                    description='Use `/stonks` and then the name of the command to learn more about it.'
                )

                await curr.execute(
                    'SELECT guild_id, name, value FROM server_stonks ORDER BY value DESC LIMIT 20'
                )
                data = await curr.fetchall()
                
                for top_stonk in data:
                    em.add_field(
                        name=top_stonk[1],
                        value=f'is worth {top_stonk[2]} $'
                    )

                await ctx.response.send_message(embed=em)

    @app_commands.command(name='botttomstonks', description='shows the bottom 20 stonks')
    async def botttomstonks(self, ctx: Interaction) -> None:
        async with aiosqlite.connect('stonks.db') as db:
            async with db.cursor() as curr:
                em = Embed(
                    title='Bottom Stonks',
                    description='Use `/stonks` and then the name of the command to learn more about it.'
                )

                await curr.execute(
                    'SELECT guild_id, name, value FROM server_stonks ORDER BY value ASC LIMIT 20'
                )
                data = await curr.fetchall()
                
                for botttom_stonk in data:
                    em.add_field(
                        name=botttom_stonk[1],
                        value=f'is worth {botttom_stonk[2]} $'
                    )

                await ctx.response.send_message(embed=em)

    @tasks.loop(hours=1)
    async def update_stonks(self):
        async with aiosqlite.connect('stonks.db') as db:
            async with db.cursor() as curr:
                for guild in self.bot.guilds:
                    """My server value should always stay at 1.00"""
                    if guild.id == 938541999961833574:
                        continue

                    await curr.execute(
                        'SELECT * FROM server_stonks WHERE guild_id = {}'.format(
                            guild.id
                        )
                    )
                    data = await curr.fetchone()

                    await curr.execute(
                        'UPDATE server_stonks SET stonks = {} WHERE guild_id = {}'.format(
                            data[2] * round(uniform(0.1, 1.5)),
                            guild.id
                        )
                    )

            await db.commit()
    
    def __cog_docs__(self) -> str:
        return '''
        This cog is used to manage the economy of the server.
        The commands are:
         - stonks
         - topstonks
         - botttomstonks
        '''
