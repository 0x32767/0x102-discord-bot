from discord import Interaction, app_commands, Object, Embed
from cogs._help_command_setup import record
from db.api import setting_off, setting_on
from discord.ext import commands  # type: ignore
from cogs._types import Shard
from typing import List


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ConfigCog(bot), guilds=[Object(id=938541999961833574)])


# turns features of the bot on and off
class ConfigCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @record()
    @app_commands.command(description="Togle a setting off")
    @app_commands.describe(setting="The setting you want to turn off")
    async def togleoff(self, ctx: Interaction, setting: str) -> None:
        await setting_on(setting, ctx.guild_id)
        await ctx.response.send_message(
            embed=Embed(
                title=f"{setting.capitalize()} has been turned off",
                color=0xDE1818,
            )
        )

    @record()
    @app_commands.command(description="")
    async def togleon(self, ctx: Interaction, setting: str) -> None:
        await setting_off(setting, ctx.guild_id)
        await ctx.response.send_message(
            embed=Embed(
                title=f"{setting.capitalize()} has been turned on",
                color=0x3DD932,
            )
        )

    @togleoff.autocomplete("setting")
    async def _settings_autocomplete(ctx: Interaction, current: str) -> List[app_commands.Choice[str]]:
        return [
            app_commands.Choice(
                name=i.lower(),
                value=i.lower(),
            )
            for i in Shard
            if current.lower() in i.lower()
        ]

    @togleon.autocomplete("setting")
    async def _settings_autocomplete(ctx: Interaction, current: str) -> List[app_commands.Choice[str]]:
        return [
            app_commands.Choice(
                name=i.lower(),
                value=i.lower(),
            )
            for i in Shard
            if current.lower() in i.lower()
        ]
