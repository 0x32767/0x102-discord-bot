from discord import Embed, Interaction, utils
from discord.ui import View, Modal, TextInput
from aiosqlite import connect


class TicketingModal(Modal, title="New Ticket"):
    summery: TextInput = TextInput(label="summery", placeholder="I want ...", required=True, max_length=300)

    description: TextInput = TextInput(
        label="say more",
        placeholder="My name is ... and I want ...",
    )

    async def on_submit(self: "TicketingModal", ctx: Interaction) -> None:
        async with connect("") as conn:
            async with conn.cursor() as curr:
                await curr.execute("SELECT * FROM mod_channels WHERE guild_id = ?;", (ctx.guild.id,))
                mod_channels: tuple[int] = await curr.fetchone()
                channel = utils.get(ctx.guild.channels, id=mod_channels[0])

            await conn.close()

        await channel.send(embed=Embed(title=self.summery.value, description=self.description.value))


class TicketingModalView(View):
    def __init__(self: "TicketingModalView") -> None:
        super().__init__()
        self.add_item(TicketingModal())
