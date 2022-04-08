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

    @tasks.loop(hours=1)
    async def update_stonks(self):
        async with aiosqlite.connect('stonks.db') as db:
            async with db.cursor() as curr:
                for guild in self.bot.guilds:
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
