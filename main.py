from cogs._create_generic_help_command import create_file # type: ignore
from configparser import ConfigParser
from cache import cacheSet, cacheGet
from discord.ext import commands
from httpx import AsyncClient
from debug import Debugger
from os import listdir
import discord


intents: discord.Intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.members = True

bot = commands.Bot(command_prefix="%", intents=intents, application_id=937461852282167337)


setattr(bot, "httpx", AsyncClient())
setattr(bot, "console", Debugger())


conf: ConfigParser = ConfigParser()
conf.read("constants.conf")
cacheSet("id", conf["bot"]["serverId"])

# we don't want to store the token in the code or in the constants.conf file
conf.read("vars.ini")

TEST_GUILD: discord.Object = discord.Object(cacheGet("id"))


@bot.event
async def on_ready():
    cogs = listdir("./cogs")

    idl_cogs: int = 1

    for idx, cog in enumerate(bot.console.progress(cogs, "[bald][bright_red]Loading cogs...[/bright_red][/bald]", len(cogs))):
        if cog.endswith(".py") and not cog.startswith("_"):
            try:
                await bot.load_extension(f"cogs.{cog[:-3]}")
                bot.console.print_cog_loaded(str(idx).zfill(3), cog)

            except Exception as e:
                bot.console.print_cog_load_error(cog, e)

            finally:
                idl_cogs += 1

    bot.console.print(f"\nSuccessfully loaded [bald][dark_orange3][{len(cogs)}/{idl_cogs}][/dark_orange3][/bald] cogs")

    bot.console.print(f"[green]Logged in as: [/green][bright_yellow][underline]{bot.user.name}[/underline][/bright_yellow]")

    await bot.tree.sync(guild=TEST_GUILD)

    await create_help_command()


async def create_help_command() -> None:
    from cogs._help_command_setup import recorded_commands # type: ignore

    await create_file(".\\docs\\generic-help-cmd.md", recorded_commands)


if __name__ == "__main__":
    bot.run(conf["bot"]["token"])
