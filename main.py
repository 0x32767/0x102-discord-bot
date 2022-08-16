from cogs._createGenericHelpCommand import createFile
from cache import cacheSet, cacheGet
from configparser import ConfigParser
from rich.console import Console
from discord.ext import commands
from rich.progress import track
from os import listdir
import discord
from cache import cacheSet, cacheGet


intents: discord.Intents = discord.Intents.default()
intents.members = True

bot: commands.Bot = commands.Bot(command_prefix="~", intents=intents, application_id=937461852282167337)

console: Console = Console()

conf: ConfigParser = ConfigParser()
conf.read("constants.conf")
cacheSet("id", conf["bot"]["serverId"])

# we don't want to store the token in the code or in the constants.conf file
conf.read("vars.ini")

TEST_GUILD: discord.Object = discord.Object(cacheGet("id"))


@bot.event
async def on_ready():
    # console.clear()
    num_cogs: int = 0
    idl_cogs: int = 0

    for cog in track(
        listdir("cogs"),
        console=console,
        description="[bald][bright_red]Loading cogs...[/bright_red][/bald]",
        total=len(listdir("cogs")),
    ):
        if cog.endswith(".py") and not cog.startswith("_"):
            #            try:
            await bot.load_extension(f"cogs.{cog[:-3]}")
            console.print(f"  [green]Successfully loaded: [/green][bright_yellow][underline]{cog}[/underline][/bright_yellow]")
            num_cogs += 1

            #            except Exception as e:
            #                console.print(f"[red]Failed loading  cog: [/red][orange_red1]{cog}[/orange_red1] [{e}]")

            #            finally:
            idl_cogs += 1

    console.print(f"\nSuccessfully loaded [bald][dark_orange3][{num_cogs}/{idl_cogs}][/dark_orange3][/bald] cogs")

    #    await bot.tree.sync(guild=TEST_GUILD)

    console.print(f"[green]Logged in as: [/green][bright_yellow][underline]{bot.user.name}[/underline][/bright_yellow]")

    await createHelpCommand()


async def createHelpCommand() -> None:
    from cogs._helpCommandSetup import recorded_commands

    createFile(".\\docs\\generic-help-cmd.md", recorded_commands)


if __name__ == "__main__":
    bot.run(conf["bot"]["token"])
