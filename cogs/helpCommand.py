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


from discord import Embed, Interaction, app_commands, Object
from cogs._help_command_setup import record
from discord.ext import commands
from cache import cacheGet


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(HelpCommand(bot), guilds=[Object(id=cacheGet("id"))])


class HelpCommand(commands.Cog):
    def __init__(self: "HelpCommand", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @record()
    @app_commands.command(description="gives the link to the help command")
    async def help(self: "HelpCommand", ctx: Interaction) -> None:
        """
         ::param:: ctx
          | The ctx param is passed by default when running a command.

         ::use::

        This command sends the link to the help command on github.
        """
        await ctx.response.send_message(
            embed=Embed(
                title="Help",
                description="This is the help command.",
                url="https://github.com/0x32767/0x102-discord-bot/blob/master/docs/help-cmd.md",
            )
        )
