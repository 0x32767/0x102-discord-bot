from discord.ext import commands
from os import listdir
import aiosqlite
import discord


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(
    command_prefix='~',
    intents=intents,
    application_id=937461852282167337
)

TEST_GUILD = discord.Object(938541999961833574)


@bot.event
async def on_ready():
    async with aiosqlite.connect('discordbotdb.db') as database:
        async with database.cursor() as cur:
            for server in bot.guilds:
                for user in server.members:
                    await cur.execute(
                        "select * from levels where guild_id = {} and user_id = {}".format(
                            user.id,
                            server.id
                        )
                    )
                    if not await cur.fetchall():
                        await cur.execute(
                            'INSERT INTO levels VALUES({}, {}, 0, 0)'.format(
                                server.id,
                                user.id
                            )
                        )

                    #if not not await cur.fetchall():
                    #    await cur.execute("insert into levels values({}, {}, 0, 0)".format(server.id, user.id))

        await database.commit()
    print('online')


@bot.event
async def setup_hook():
    for cog in listdir('cogs'):
        if not cog.endswith('.h.py') and cog.endswith('.py'):
            await bot.load_extension(f"cogs.{cog[:-3]}")

    await bot.tree.sync(guild=TEST_GUILD)


bot.run('OTM3NDYxODUyMjgyMTY3MzM3.YfcFYg.D_neAXuzaltzXhLPqp9QZEJn-bI')
