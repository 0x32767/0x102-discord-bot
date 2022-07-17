import cogs._helpCommandSetup
from discord.ext import commands
from cache import cacheGet
from discord import (
    Interaction,
    app_commands,
    Object,
    VoiceChannel
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        VoiceCog(bot),
        guilds=[Object(id=cacheGet("id"))]
    )


class VoiceCog(commands.Cog):
    def __init__(self: "VoiceCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Joins the voice channel of the user.")
    async def join(self: "VoiceCog", ctx: Interaction) -> None:
        if ctx.user.voice:
            channel: VoiceChannel = ctx.user.voice.channel
            await channel.connect()
            await ctx.response.send_message("connected successfully!!!")

        else:
            await ctx.response.send_message("you need to be in a vc for this command to work")

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="leaves a voice channel")
    async def leave(self: "VoiceCog", ctx: Interaction):
        try:
            await ctx.guild.voice_client.disconnect(force=True)
            await ctx.response.send_message("left vc")

        except Exception as er:
            if isinstance(er, AttributeError):
                await ctx.response.send_message("I am not in a voice channel")

            else:
                await ctx.response.send_message(str(er))
