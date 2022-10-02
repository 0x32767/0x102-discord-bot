# The cogs folder

The `cogs` folder is where all the commands for the bot are. Cogs are a way to organize your commands in a neet and readable way.
However, cogs do come with a bit of boilerplate, which is duplicated code. A cog will follow this structure:
```py
from discord import app_commands, Interaction, Object
from cogs._help_command_setup import record
from discord.ext import commands


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        CogName(bot),
        guilds=[Object(id=938541999961833574)]
    )


class CogName(commands.Cog):
    def __int__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    # this is one command
    @record()
    @app_commands.command(description="this is a test command")
    @app_commands.describe(msg="what you want the bot to say")
    async def echo(self, ctx: Interaction, *, msg: str) -> None:
        await ctx.response.send_message(msg)

    # this is another command
    @record()
    @app_commands.command(description="this is a test command")
    async def hello(self, ctx: Interaction) -> None:
        await ctx.response.send_message("hello")
```
 The file shows the minimum work to get 2 commands working. When you create a command with `@app_commands.command()` you
need to pass a description of what the command does. e.g `@app_commands.command(description="This is the description for my cmd")`.
 
## My file does not have any commands in it

The way that cogs are sorted is that if the file starts with an `_` then it is ignored but if not then it is treated as if it was a cog, which could lead to errors.
For any file that is ignored you can put what you want in it. This feature will be removed when all files will be sorted into
folders depending on their content.
