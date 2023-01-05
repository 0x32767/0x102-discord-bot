from cogs._create_generic_help_command import create_file  # type: ignore
from configparser import ConfigParser
from discord.ext import commands  # type: ignore
from httpx import AsyncClient
from debug import Debugger
from glob import glob
import discord


intents: discord.Intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix="%", intents=intents, application_id=937461852282167337)


setattr(bot, "httpx", AsyncClient())
setattr(bot, "console", Debugger())


conf: ConfigParser = ConfigParser()
conf.read("vars.ini")


@bot.event
async def on_ready():
    for file in glob("cogs/[!_]*.py"):
        await bot.load_extension(file[:-3].replace("\\", "."))
    # await bot.load_extension("cogs.config")

    await bot.tree.sync(guild=discord.Object(id=938541999961833574))

    # await create_help_command()


async def create_help_command() -> None:
    from cogs._help_command_setup import recorded_commands  # type: ignore

    await create_file(".\\docs\\generic-help-cmd.md", recorded_commands)


if __name__ == "__main__":
    bot.run(conf["bot"]["token"])
