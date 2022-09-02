from discord import Interaction, app_commands, Object, Embed, Member, DMChannel, File
from cogs._help_command_setup import record
from discord.ext import commands
from asyncio import sleep
from cache import cacheGet


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(halloweenCog(bot), guilds=[Object(id=cacheGet("id"))])


class halloweenCog(commands.Cog):
    def __init__(self: "halloweenCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @record()
    @app_commands.command(description="scare someone")
    async def creepout(self: "halloweenCog", ctx: Interaction, person: Member):
        dm: DMChannel = await person.create_dm()
        await dm.send(person.mention)
        await sleep(0.5)
        await dm.send(file=File(""))
