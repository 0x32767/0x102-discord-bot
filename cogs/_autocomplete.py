from discord.ext import commands
from discord import app_commands
from typing import List
import discord


async def configuration_autocomplete(
    interaction: discord.Interaction, current: str, namespace: app_commands.Namespace
) -> List[app_commands.Choice[str]]:
    config_options: List[str] = []
    return [
        app_commands.Choice(
            name=i.capitalize(),
            value=i.lower(),
        )  # This is the choice simmilar to a discord.ui element where the value is what the programmer sees and thename is what the user sees
        for i in config_options
        if current.lower() in i.lower()
    ]
