from discord.ui import View
import aiosqlite
import discord
from discord import (
    Interaction,
    Embed,
    Colour
)


class LuaCommandKeep(discord.ui.Button):
    def __init__(self: "LuaCommandKeep", cls) -> None:
        self.cls = cls
        super().__init__(label="save")

    async def callback(self: "LuaCommandKeep", ctx: Interaction) -> None:
        async with aiosqlite.connect("D:\\programing\\0x102-discord-bot\\commands.db") as db:
            async with db.cursor() as cursor:
                await cursor.execute("INSERT INTO commands VALUES (null, ?, ?)", (self.cls.name.value, self.cls.code.value))

            await db.commit()

        await ctx.response.send_message(
            embed=Embed(
                title="Command Added",
                description=f"{self.cls.name} has been added to the database.",
                colour=Colour.green()
            )
        )


class LuaCommandBin(discord.ui.Button):
    def __init__(self: "LuaCommandKeep", cls) -> None:
        self.cls = cls
        super().__init__(
            label="Bin",
        )

    async def callback(self: "LuaCommandKeep", ctx: Interaction) -> None:
        await ctx.send(
            embed=Embed(
                title="Command Added",
                description=f"{self.cls.name} does not exist in the database.",
                colour=Colour.red()
            )
        )


class LuaCommandView(View):
    def __init__(self: "LuaCommandView", cls) -> None:
        super().__init__()
        self.add_item(LuaCommandKeep(cls))
        self.add_item(LuaCommandBin(cls))
