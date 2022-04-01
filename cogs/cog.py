import discord
from discord import app_commands
from discord.ext import commands


class OgCOG(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command()
    async def ping(self, ctx: discord.Interaction) -> None:
        await ctx.response.send_message('pong')


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        OgCOG(bot),
        guilds=[discord.Object(id=938541999961833574)]
    )
