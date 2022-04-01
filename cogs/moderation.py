import discord
from discord.ext import commands
from discord import (
    Interaction,
    app_commands,
    Object,
    Member
)


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command()
    async def kick(self, interaction: Interaction, user: Member, *, reason: str = "You  have been naughty") -> None:
        try:
            await user.kick(reason=reason)
            await interaction.response.send_message(f"successfully kicked {user.name} for \"{reason}\"")

        except Exception as e:
            await interaction.response.send_message(f"error: {e}")

    @app_commands.command()
    async def ban(self, interaction: Interaction, user: Member, *, reason: str = "you have been naughty"):
        try:
            await user.ban(reason=reason)
            await interaction.response.send_message(f"successfully kicked {user.name} for \"{reason}\"")

        except Exception as e:
            await interaction.response.send_message(f"error: {e}")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Moderation(bot),
        guilds=[Object(id=938541999961833574)]
    )
