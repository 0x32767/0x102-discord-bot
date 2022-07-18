import cogs._helpCommandSetup
from discord.ext import commands
from cache import cacheGet
from typing import List
from discord import Embed, Interaction, app_commands, Object


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

    @cogs._helpCommandSetup.record()
    @app_commands.command(
        name="decrypt", description="This command will decrypt a message."
    )
    @app_commands.describe(message="The message you want the bot to decrypt.")
    async def decrypt(self: "DecryptCog", ctx: Interaction, *, message: str) -> None:
        embeds: List[Embed] = []

        for method in [
            self.crackCieserCipher,
            self.crackHexEncode,
            self.crackBase2Encode,
        ]:

            # self.crackCieserCipher is a bruit force method and therefore needs to be itterated over all possibilities.
            if method == self.crackCieserCipher:
                em: Embed = Embed(
                    title="Caesar Cipher", description=f"{message}", color=0x00FF00
                )
                for i in range(1, 26):
                    em.add_field(
                        name=f"{i}",
                        value=f"{await method(message=message, offset=i)}",
                        inline=True,
                    )
                embeds.append(em)
                continue  # skip the rest of the loop.

            # some errors could be thrown it the encryption type is not supported
            try:
                # all other encodings are of type str
                embeds.append(
                    Embed(
                        title=f"Decrypted Message for {method.__name__}",
                        description="".join(await method(message)),
                        color=0x00FF00,
                    )
                )

            except Exception as e:
                embeds.append(Embed(title="Error", description=f"{e}", color=0xFF0000))

        await ctx.response.send_message(embeds=embeds, ephemeral=True)

    async def crackCieserCipher(self: "DecryptCog", message: str, offset: int) -> str:
        """
        | This function is given an offset and will return the decrypted message.
        """
        return "".join(
            self.chars[self.chars.index(char) - offset]
            if char in "abcdefghijklmnopqrstuvwxyz"
            else char
            for char in message
        )

    async def crackBase2Encode(self: "DecryptCog", message: str) -> str:
        """
        | This function will return one string because the base2
        | is the ascii character of the string in binary. this
        | will reconvert the binary to ascii and return the string.
        """
        return "".join(
            chr(int(message[i : i + 9], 2))
            for i in range(0, len(message), 9)
            if message[i : i + 9] != "0b"
        )

    async def crackHexEncode(self: "DecryptCog", message: str) -> str:
        """
        | This function will return one string because the hex
        | is the ascii character of the string in hexadecimal.
        | this will reconvert the hex to ascii and return the string.
        """
        return "".join(
            chr(int(message[i : i + 2], 16))
            for i in range(0, len(message), 2)
            if message[i : i + 2] != "0x"
        )
