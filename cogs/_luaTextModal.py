from discord.ui.modal import Modal
from cogs._luaUi import LuaCommandView
import discord


class LuaTextEditorModal(Modal, title="Write Lua Here"):
    name = discord.ui.TextInput(
        label="Command name",
        placeholder="Command name"
    )
    code = discord.ui.TextInput(
        label="Lua Code",
        style=discord.TextStyle.long,
        placeholder="type your command here...",
        required=True,
        max_length=300,
    )

    async def on_submit(self: "LuaTextEditorModal", ctx: discord.Interaction) -> None:
        await ctx.response.send_message(
            embed=discord.Embed(
                title="Command Added",
                description=f"{self.name.value} has been added to the database.",
                colour=discord.Colour.green()
            ),
            view=LuaCommandView(self)
        )
