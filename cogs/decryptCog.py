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
from typing import List


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DecryptCog(bot), guilds=[Object(id=cacheGet("id"))])


class DecryptCog(commands.Cog):
    def __init__(self: "DecryptCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        self.chars: list[str] = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]

    @record()
    @app_commands.command(name="decrypt", description="This command will decrypt a message.")
    @app_commands.describe(message="The message you want the bot to decrypt.")
    async def decrypt(self: "DecryptCog", ctx: Interaction, *, message: str) -> None:
        embeds: List[Embed] = []

        # ceaser cipher cracking
        em: Embed = Embed(title="Caesar Cipher", description=f"{message}", color=0x00FF00)
        for i in range(1, 26):
            em.add_field(
                name=f"{i}",
                value=f"{await self.crack_cieser_cipher(message=message, offset=i)}",
                inline=True,
            )
            embeds.append(em)

        # hexadecimal encoding
        embeds.append(
            Embed(
                title=f"Decrypted Message for hexadecimal encoding",
                description="".join(await self.crack_hex_encode(message)),
                color=0x00FF00,
            )
        )

        await ctx.response.send_message(embeds=embeds, ephemeral=True)

    async def crack_cieser_cipher(self: "DecryptCog", message: str, offset: int) -> str:
        """
        | This function is given an offset and will return the decrypted message.
        """
        return "".join(
            self.chars[self.chars.index(char) - offset] if char in self.chars else char for char in message
        )

    @staticmethod
    async def crack_hex_encode(message: str) -> str:
        """
        | This function will return one string because the hex
        | is the ascii character of the string in hexadecimal.
        | this will reconvert the hex to ascii and return the string.
        """
        return "".join(chr(int(message[i: i + 2], 16)) for i in range(0, len(message), 2) if message[i: i + 2] != "0x")
