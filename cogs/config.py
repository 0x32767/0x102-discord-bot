from discord import Interaction, app_commands, Object, Embed
from cogs._autocomplete import configuration_autocomplete
from aiosqlite import connect, Connection, Row
from cogs._help_command_setup import record
from typing import List, Dict, Union
from json import load as load_json
from discord.ext import commands  # type: ignore


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ConfigCog(bot), guilds=[Object(id=938541999961833574)])


# turns features of the bot on and off
class ConfigCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:

        self.conn: Connection = connect("...")
        self.onn.row_factory = Row
        # so that when we query a table we can treet the result as a python dict

        self.bot: commands.Bot = bot

    @record()
    @app_commands.command(description="change the bot's configuration settings")
    async def seeconfig(self, ctx: Interaction) -> None:
        em: Embed = Embed(title=f"Configuration settings for `{ctx.guild.name}`")

        async with self.conn.cursor() as curr:
            curr.execute("SELECT * FROM config WHERE server_id = ?", (ctx.guild.id,))

            name: str
            value: str
            # if we convert the input to a dict then we can get the name of the columns and the values in the following format
            # {"server_id": 1234567890, "name": "bobby der baum", ...}
            async for name, value in dict(await curr.fetchone()).keys():
                em.add_field(name=name, value=value, inline=True)

        await ctx.response.send_message(embed=em)

    @record()
    @app_commands.command(description="toggle settings on and off")
    @app_commands.describe(setting="What you want to inspect")
    @app_commands.choices(setting=configuration_autocomplete)
    async def info(self, ctx: Interaction, setting: app_commands.Choice[int]) -> None:
        em: Embed = Embed(title=setting.value, description=f"Learning about the {setting.value}")

        with open(".//generics//settings.json", "r") as f:
            settings: Dict[str, Dict[str, Union[str, int]]] = load_json(f)

        for k, v in settings[setting.value].items():
            em.add_field(name=k, value=v, inline=True)

        await ctx.response.send_message(embed=em)
