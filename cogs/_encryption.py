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

from random import randint
from discord import Interaction, SelectOption, Embed
from discord.ui import Select, View


class EncryptionView(View):
    def __init__(self: "EncryptionView", msg: str) -> None:
        super().__init__()
        self.add_item(EncryptionDropdown(msg))


class EncryptionDropdown(Select):
    def __init__(self: "EncryptionDropdown", msg: str):
        super().__init__(
            max_values=1,
            min_values=1,
            options=[
                SelectOption(
                    label="hexadecimal encode",
                    value="hexadecimal encode",
                    description="hexadecimal encode",
                ),
                SelectOption(
                    label="caesar cipher",
                    value="caesar cipher",
                    description="caesar cipher",
                ),
                SelectOption(
                    label="binary encode",
                    value="binary encode",
                    description="binary encode",
                ),
                # SelectOption(label="base32 encode", value="base32 encode", description="base32 encode"),
            ],
        )
        self.msg: str = msg
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

    async def callback(self: "EncryptionDropdown", ctx: Interaction) -> None:
        match self.values[0]:
            case "caesar cipher":
                msg = await self.createCeaserCipher()

            case "binary encode":
                msg = await self.createBase2Encode()

            case "hexadecimal encode":
                msg = await self.createHexEncode()

            case "base32 encode":
                msg = await self.createBase32Encode()

        await ctx.response.send_message(embed=Embed(title="Encrypted Message", description=msg), ephemeral=True)

    async def createCeaserCipher(self: "EncryptionDropdown") -> str:
        offset: int = randint(1, 25)

        """
         | A ceaser cipher is the offset alphabet one.
         | A B C D E F G H I J K L N N O P Q R S T U V W X Y Z
         | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
         |
         | In the table above the alphabet is offset by one.
        """
        res: str = ""

        for char in self.msg:
            try:
                res += self.chars[self.chars.index(char) + offset]

            except ValueError:
                # I have not included all of the ascii characters
                res += char

            except IndexError:
                # a ceaser cipher will wrap around, this is to do that
                res += self.chars[self.chars.index(char) + offset - 26]

        return res

    async def createHexEncode(self: "EncryptionDropdown") -> str:
        """
        | Hex is a base 16, which is a base that is used to represent
        | numbers in a way that is easier to read.
        """
        return "".join(hex(ord(char)) for char in self.msg)

    async def createBase2Encode(self: "EncryptionDropdown") -> str:
        """
        | Base 2 is one of the most hard-to-read bases (that is
        | commonly used) and that is why i have used it to encrypt
        | a message, this works by getting the ascii number of a
        | character and convertig it into base 2. I then use one of
        | python's most underated features (.zfill(v)) to padd the
        | binary with 8 zeros.
        """
        return "".join(bin(ord(char)).zfill(8) for char in self.msg)

    async def createBase32Encode(self: "EncryptionDropdown") -> str:
        """
        | Base64 is an actual base like binary (base2), octal (base
        | 8), hex (base 16)... Becaue all bases besides 2, and 10 are
        | almost unknown of it makes for a rather convincing cipher.
        | I am assuming that 0x7E 127 is as far as anyone will try
        | to type.
        """
        return "%".join(int(ord(char), base=32) for char in self.msg)
