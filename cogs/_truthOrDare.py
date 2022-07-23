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


from random import choice as random_choice
from discord.ui import View, Button
from json import load
from discord import (
    Interaction,
    Embed,
    Color,
)


class TruthButton(Button):
    def __init__(self: "TruthButton") -> None:
        super().__init__(label="Truth")
        self.color = Color.green()

    async def callback(self: "TruthOrDareUi", ctx: Interaction) -> None:
        with open("./assets/truthDare.json") as f:
            data: dict[str, list[str]] = load(f)

        return await ctx.response.send_message(
            embed=Embed(
                title=random_choice(data["truth"]),
                description="Truth or Dare",
                color=Color.green(),
            ).add_field(name=f"@{ctx.user.name} has chosen...", value="TRUTH")
        )


class DareButton(Button):
    def __init__(self: "DareButton") -> None:
        super().__init__(label="Dare")
        self.color = Color.red()

    async def callback(self: "TruthOrDareUi", ctx: Interaction) -> None:
        with open("./assets/truthDare.json") as f:
            data: dict[str, list[str]] = load(f)

        return await ctx.response.send_message(
            embed=Embed(
                title=random_choice(data["dares"]),
                description="Truth or Dare",
                color=Color.red(),
            ).add_field(name=f"@{ctx.user.name} has chosen...", value="DARE")
        )


class TruthOrDareUi(View):
    def __init__(self: "TruthOrDareUi") -> None:
        super().__init__()
        self.add_item(TruthButton())
        self.add_item(DareButton())
