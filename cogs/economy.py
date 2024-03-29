from db.api import transfer_to_account, transfer_between_acccounts, remove_from_account
from discord import Interaction, app_commands, Object, Embed, Member
from cogs._types import guild_id, user_id, t_result
from cogs._help_command_setup import record
from discord.ext import commands
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

        res: t_result = transfer_to_account(ctx.user.id, amount, self.bot.console)

        if res[0] > 0:  # if it was a fail
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
        if not isinstance(amount, int):
            await ctx.response.send_message("The input needs to be a number (can't have decimals in it)")
            return

        res: t_result = transfer_between_acccounts(ctx.user.id, who.id, amount)

        if res[0] == 0:
            await ctx.response.send_message(
                embed=Embed(
                    title=f"Gave {who.display_name} {amount} coins",
                    description=f"{ctx.user.display_name} ran /give to give money to {who.display_name}",
                ),
            )

        elif res[0] == 1:
            await ctx.response.send_message(
                embed=Embed(
                    title=f"Woops, you could not give {who.display_name} some coins",
                    description=f"{res[1]}",
                ),
            )

        elif res[0] == 2:
            await ctx.response.send_message(f"Some error occured")

    @record()
    @app_commands.command(description="rob a person's bank")
    @app_commands.describe(who="Who you want to rob")
    async def rob(self, ctx: Interaction, who: Member) -> None:
        num: int = randint(1, 3)
        if num == 1:  # person was caught and got a fine for some coins
            if not transfer_between_acccounts(ctx.guild_id, ctx.user.id, who.id, 50):
                await ctx.response.send_message(
                    embed=Embed(title="Got caught!", description="You where caught in the act and got a fine of 50 coins")
                )
                return

            await ctx.response.send_message()
            return

        elif num == 2:  # person dropped money but still stole some
            if not remove_from_account(ctx.guild_id, who.id, randint(0.5, 25) * 10):
                await ctx.response.send_message()
                return

            await ctx.response.send_message()
            return

        else:  # person took money successfully
            amount: int = randint(0.5, 25) * 10
            if not transfer_between_acccounts(who.id, ctx.user.id, amount):
                await ctx.response.send_message()
                return

            await ctx.response.send_message(
                embed=Embed(
                    title=f"You successfully robed the bank, {amount} coins",
                    description=f"{ctx.user.display_name} used /rob to steal {amount} from {who.display_name}",
                )
            )
            return
