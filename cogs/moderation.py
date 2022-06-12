from discord.ext import commands
from ._comand_chache import register_commands
import aiosqlite
from discord import (
    Interaction,
    app_commands,
    Object,
    Embed,
    Member
)


class Moderation(commands.Cog):
    def __init__(self: 'Moderation', bot: commands.Bot) -> None:
        register_commands(self)
        self.bot: commands.Bot = bot

    @app_commands.command()
    @app_commands.describe(user="The user you want to kick.")
    @app_commands.describe(reason="Why you want to kick the user.")
    async def kick(self: 'Moderation', ctx: Interaction, user: Member, *, reason: str = "You  have been naughty") -> None:
        """
        :param ctx:
        :param user:
        :param reason:
        :return:
        """
        try:
            await user.kick(reason=reason)
            await ctx.response.send_message(f"successfully kicked {user.name} for \"{reason}\"")

        except Exception as e:
            await ctx.response.send_message(f"error: {e}")

    @app_commands.command()
    @app_commands.describe(user="The user you want to ban.")
    @app_commands.describe(reason="Why you want to ban the user.")
    async def ban(self: 'Moderation', ctx: Interaction, user: Member, *, reason: str = "you have been naughty") -> None:
        try:
            await user.ban(reason=reason)
            await ctx.response.send_message(f"successfully kicked {user.name} for \"{reason}\"")

        except Exception as e:
            await ctx.response.send_message(f"error: {e}")

    @app_commands.command(name='stats', description='you can see server statistics')
    async def stats(self: 'Moderation', ctx: Interaction) -> None:
        async with ctx.channel.typing():
            embed: Embed = Embed(
                title=f'{ctx.guild.name}\'s stats',
                description='gives the stats of the server'
            )
            for key, stat in zip(
                    ['name', 'owner', 'members', 'region'],
                    [f'{ctx.guild.name}', f'{ctx.guild.owner.name}', f'{ctx.guild.member_count}', f'{ctx.guild.region}']
            ):
                embed.add_field(
                    name=key,
                    value=stat
                )

        await ctx.response.send('ok', embed=embed)

    @app_commands.command(description='whitelist a user and bots')
    @commands.is_owner()
    async def whitelist(self: 'Moderation', ctx: Interaction, member: Member) -> None:
        async with ctx.channel.typing():
            async with aiosqlite.connect('discordbotdb.db') as db:
                async with db.cursor() as curr:
                    await curr.execute(
                        f'update whitelist set whitelisted = True where guild_id = {ctx.guild.id} and user_id = {member.id}'
                    )

                await db.commit()

            await ctx.response.send_message(f'{ctx.user.mention} has now been whitelisted!!!')

    @app_commands.command(description='unwhitelist a user and bots')
    @commands.is_owner()
    async def unwhitelist(self: 'Moderation', ctx: Interaction, member: Member) -> None:
        async with ctx.channel.typing():
            async with aiosqlite.connect('discordbotdb.db') as db:
                async with db.cursor() as curr:
                    await curr.execute(
                        f'update whitelist set whitelisted = False where guild_id = {ctx.guild.id} and user_id = {member.id}'
                    )

            await db.commit()

            await ctx.response.send_message(f'{ctx.user.mention} has now been unwhitelisted!!!')

    @app_commands.command(description='check if a user is whitelisted')
    async def whitelisted(self: 'Moderation', ctx: Interaction, member: Member) -> None:
        async with ctx.channel.typing():
            async with aiosqlite.connect('discordbotdb.db') as db:
                async with db.cursor() as curr:
                    await curr.execute(
                        f'select whitelisted from whitelist where guild_id = {ctx.guild.id} and user_id = {member.id}'
                    )

                    whitelisted: tuple = await curr.fetchone()

            await db.commit()

            if whitelisted[0] == 1:
                await ctx.response.send_message(f'{member.mention} is whitelisted')
            else:
                await ctx.response.send_message(f'{member.mention} is not whitelisted')

    @app_commands.command(description='check if a user is banned')
    async def antiraid(self: 'Moderation', ctx: Interaction) -> None:
        async with ctx.channel.typing():
            async with aiosqlite.connect('discordbotdb.db') as db:
                async with db.cursor() as curr:
                    for member in ctx.guild.members:
                        await curr.execute(
                            f'select whitelisted from whitelist where guild_id = {ctx.guild.id} and user_id = {member.id}'
                        )

                        whitelisted: tuple = await curr.fetchone()
                        if whitelisted == 1:
                            continue

                        else:
                            await member.kick(reason=f'You are not whitelisted in the `{ctx.guild.name}` server')

            await ctx.response.send_message('ok, done')

    def __cog_docs__(self) -> str:
        return """
        This cog is used to moderate your server.
        You can use the commands:
            -kick
            -ban
            -stats
        """


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Moderation(bot),
        guilds=[Object(id=938541999961833574)]
    )
