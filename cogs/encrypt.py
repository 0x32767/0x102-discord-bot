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


from cogs.ui._encryption import EncryptionView  # type: ignore
from cogs._help_command_setup import record  # type: ignore
from discord import Object, app_commands, Interaction
from discord.ext import commands  # type: ignore


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(EncryptCog(bot), guilds=[Object(id=938541999961833574)])


class EncryptCog(commands.Cog):
    def __init__(self: "EncryptCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @record()
    @app_commands.describe(msg="The message you want to encrypt.")
    @app_commands.command(description="Encrypts a message.")
    async def encrypt(self: "EncryptCog", ctx: Interaction, *, msg: str) -> None:
        """
        ::param:: ctx
         | type: Interaction
         | This is passed by default by the discord.py bot and does not really need
         | to be changed.
         |
        ::param:: msg
         | type: str
         | This is the message that the user wants to encrypt, there is an `*`
         | before the msg so that discord.py knows to give all the words that the
         | user types into the message parameter. If the `*` was not there it we
         | would only get the first word.
         |

        +----------+--------------------+----------------------------+
        |          | the actual message | what the bot would give us |
        +----------+--------------------+----------------------------+
        | with `*` | hello world        | "hello world"              |
        | no '*'   | hello world        | "hello"                    |
        +----------+--------------------+----------------------------+
        """
        await ctx.response.send_message(view=EncryptionView(msg), ephemeral=True)
