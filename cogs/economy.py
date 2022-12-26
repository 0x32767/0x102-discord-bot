from discord import Interaction, app_commands, Object, Embed, Member
from db.api import transfer_to_account, transfer_between_acccounts
from ._help_command_setup import record
from discord.ext import commands
from cogs._mod import is_admin
from random import randint


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        EconomyCog(bot),
        guilds=[Object(id=938541999961833574)],
    )


class EconomyCog(commands.Cog):
    def __init__(self: "EconomyCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @record()
    @app_commands.command(description="gives you some money")
    async def beg(self, ctx: Interaction) -> None:
        amount: int = randint(0, randint(5, 20))
        if amount == 0:
            await ctx.response.send_message(
                embed=Embed(
                    title="No luck",
                    description="You go no extra coins, try again soon!",
                ),
            )
            return

        res = transfer_to_account(ctx.guild_id, ctx.user.id, amount, self.bot.console)

        if not res:
            await ctx.response.send_message(
                embed=Embed(
                    title="Got no extra coins",
                    description=f"Someone would have given you {amount} coins but didn't have enough",
                ),
            )
            return

        await ctx.response.send_message(
            embed=Embed(
                title=f"You got {amount} coins yay",
                description=f"{ctx.user.display_name.capitalize()} ran /{ctx.command.name} and got some money",
            ),
        )

    @record()
    @app_commands.command(description="give some money to someone")
    @app_commands.describe(who="Who you wnat to give some coins to")
    async def give(self, ctx: Interaction, who: Member, amount: int = 5) -> None:
        res = transfer_between_acccounts(ctx.guild_id, ctx.user.id, who.id, amount)

        if not res:
            await ctx.response.send_message(
                embed=Embed(
                    title=f"Woops, you could not give {who.display_name} some coins",
                    description="Some error occured while running this command",
                ),
            )
            return

        await ctx.response.send_message(
            embed=Embed(
                title=f"Gave {who.display_name} {amount} coins",
                description=f"{ctx.user.display_name} ran /give to give money to {who.display_name}",
            ),
        )

    @record()
    @app_commands.command(description="rob a person's bank")
    @app_commands.describe(who="Who you want to rob")
    async def rob(self, ctx: Interaction, who: Member) -> None:
        ...
