import discord
from ._comand_chache import commands
from discord.ext import commands
from discord import (
    Interaction,
    app_commands,
    Object
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        HelpComand(bot),
        guilds=[Object(id=938541999961833574)]
    )


class HelpComand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name='help', description='help command')
    async def help(self, ctx: Interaction, *, command: str = None) -> None:
        if command is None:
            embed = discord.Embed(
                title='Help',
                description='Use `/help` and then the name of the command to learn more about it.'
            )

            for cog in self.bot.cogs:
                embed.add_field(
                    name=f'{cog}',
                    value=f'{self.bot.cogs[cog].__cog_docs__()}',
                    inline=False
                )

            await ctx.response.send_message(embed=embed)

    def __cog_docs__(self) -> str:
        return '''
        This cog is used to help you with the bot.
        The commands are:
         -help
        '''
