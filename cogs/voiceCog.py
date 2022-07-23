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


import cogs._helpCommandSetup
from discord.ext import commands
from cache import cacheGet
from discord import Interaction, app_commands, Object, VoiceChannel


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(VoiceCog(bot), guilds=[Object(id=cacheGet("id"))])


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
            await ctx.response.send_message(
                "you need to be in a vc for this command to work"
            )

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
