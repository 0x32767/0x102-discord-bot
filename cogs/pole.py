"""
Copyright (C) 23/07/2022 - Han P.B Manseck.

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import cogs._helpCommandSetup
from discord.ext import commands
from discord import Interaction, app_commands, Object, Embed, Color
from cache import cacheGet


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PoleCog(bot), guilds=[Object(id=cacheGet("id"))])


class PoleCog(commands.Cog):
    def __init__(self: commands.Bot, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot
        self.votes: commands.Bot = {}
        """
        :votes: format:
            {
                "channel_id" [int]: {
                    "question": "question_text" [str],
                    "options": {
                        "option_1_text [str]": votes [int],
                    },
                    "closed": True/False [bool],
                    "author": author_id [int]
                }
            }
        """

    @cogs._helpCommandSetup.record()
    @app_commands.command(name="newpoll", description="Creates a new poll.")
    @app_commands.describe(question="The question you want to ask.")
    async def new_poll(self: "PoleCog", ctx: Interaction, *, question: str) -> None:
        """
        :param ctx: The ctx param is passes by the discord.py libruary
        :param question: The question that is created by the user
        :return:
        """

        # checks if there is still a non-closed pole in the channel
        if (
            ctx.channel.id in self.votes
            and self.votes[ctx.channel.id]["closed"] is False
        ):
            await ctx.send("There is already a poll in this channel.")
            return

        self.votes[ctx.channel.id] = {
            "question": question,
            "options": {"yes": 0, "no": 0},
            "closed": False,
            "author": ctx.author.id,
        }

        await ctx.response.send_message(
            embed=Embed(
                title="Poll created",
                description="use `/newpole` to create a new poll in this channel",
                color=Color.green(),
            ).add_field(name="vote", value="`/vote yes` or `/vote no`")
        )

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Votes for the poll.")
    @app_commands.describe(vote="true: yes, false: no")
    async def vote(self: "PoleCog", ctx: Interaction, vote: bool) -> None:
        """
        :param ctx: The ctx param is passes by the discord.py libruary
        :param vote: The vote that is created by the user
        :return:
        """
        try:
            pole: dict = self.votes[ctx.channel.id]
        except KeyError:
            return await ctx.send("There is no poll in this channel.", ephemeral=True)

        if pole["closed"] is True:
            return await ctx.send(
                "The poll is closed, you can not vote in a colsed pole.", ephemeral=True
            )

        pole["options"]["yes"] += 1 if vote else 0
        pole["options"]["no"] += 0 if vote else 1

        await ctx.send("Your vote has been registered.", ephemeral=True)

    @cogs._helpCommandSetup.record()
    @app_commands.command(name="closepoll", description="Closes the poll.")
    @app_commands.describe(show="show the results of the poll")
    async def close_poll(self, ctx: Interaction, show: bool = False) -> None:
        """
        :param ctx: The ctx param is passes by the discord.py libruary
        :return:
        """
        try:
            pole: dict = self.votes[ctx.channel.id]
        except KeyError:
            return await ctx.send("There is no poll in this channel.", ephemeral=True)

        if pole["closed"] is True:
            return await ctx.send("The poll is already closed.", ephemeral=True)

        pole["closed"] = True

        await ctx.response.send_message(
            embed=Embed(
                title="The pole has been closed",
                description="The poll is closed, you can not vote anymore.",
                color=Color.red(),
            ),
            ephemeral=show,
        )

    @cogs._helpCommandSetup.record()
    @app_commands.command(name="showpoll", description="Shows the results of the poll.")
    @app_commands.describe(
        public="do you want the poll to be public (can be seen by everyone)"
    )
    async def show_poll(self, ctx: Interaction, public: bool = False) -> None:
        """
        :param ctx: The ctx param is passes by the discord.py libruary
        :return:
        """
        try:
            pole: dict = self.votes[ctx.channel.id]
        except KeyError:
            return await ctx.send("There is no poll in this channel.", ephemeral=True)

        if pole["closed"] is True:
            return await ctx.send("The poll is closed.", ephemeral=True)

        await ctx.send(
            embed=Embed(
                title=pole["question"],
                description=f'yes: {pole["options"]["yes"]}\nno: {pole["options"]["no"]}',
                color=Color.green(),
            )
            .add_field(
                name="yes",
                value=f'{pole["options"]["yes"] / (pole["options"]["yes"] + pole["options"]["no"]) * 100}%',
            )
            .add_field(
                name="no",
                value=f'{pole["options"]["no"] / (pole["options"]["yes"] + pole["options"]["no"]) * 100}%',
            ),
            ephemeral=public,
        )
