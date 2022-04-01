import discord
from discord.ext import commands
from discord import (
    Interaction,
    app_commands,
    Object
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        VoiceCog(bot),
        guilds=[Object(id=938541999961833574)]
    )


class VoiceCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command()
    async def join(self, ctx: Interaction) -> None:
        if ctx.user.voice:
            channel = ctx.user.voice.channel
            await channel.connect()
            return

        await ctx.response.send_message('you need to be in a vc for this to work')
