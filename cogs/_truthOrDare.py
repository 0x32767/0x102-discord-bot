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
                color=Color.green()
            ).add_field(
                name=f"@{ctx.user.name} has chosen...",
                value="TRUTH"
            )
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
                color=Color.red()
            ).add_field(
                name=f"@{ctx.user.name} has chosen...",
                value="DARE"
            )
        )


class TruthOrDareUi(View):
    def __init__(self: "TruthOrDareUi") -> None:
        super().__init__()
        self.add_item(TruthButton())
        self.add_item(DareButton())
