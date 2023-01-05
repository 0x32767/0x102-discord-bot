from discord import Interaction, app_commands, Object, Embed, Member
from db.api import give_item, give_item, get_item, get_all_items
from cogs._help_command_setup import record
from cogs._types import Snowflake as flk
from discord.ext import commands
from random import uniform


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        ItemsCog(bot),
        guilds=[Object(id=938541999961833574)],
    )


class ItemsCog(commands.Cog):
    def __init__(self: "ItemsCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @record()
    @app_commands.command(description="dig for items")
    async def dig(self: "ItemsCog", ctx: Interaction) -> None:
        if uniform(0, 1) < 0.25:
            # The use found nothing
            await ctx.response.send_message("you found ||NOTHING||")

        # The for-else syntax can be fround apon byt is usefull for my case
        for item in await get_all_items((flk.ID, flk.RARITY, flk.NAME, flk.IMG)):
            if uniform(0, 1) > item[1]:
                # means the item was chosen
                await give_item(item[0])  # item[0] is the id
                await ctx.response.send_message(
                    embed=Embed(  # str(item[2]).lower()[0] gets the first character and makes it lowercase
                        title=(
                            f"You found an {str(item[2]).capitalize()}"
                            if str(item[2]).lower()[0] in "aeiou"
                            else f"You found a {str(item[2]).capitalize()}"
                        ),
                    )
                    .add_field(name="rarity", value=f"{item[1]} % chance from digging")
                    .set_image(url=item[3])
                )

        else:
            await ctx.response.send_message("you found ||NOTHING||")
