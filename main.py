from discord.ext import commands
from os import listdir
import aiosqlite
import discord


intents = discord.Intents.default()
bot = commands.Bot(
    command_prefix='~',
    intents=intents,
    application_id=866344879070904380
)

TEST_GUILD = discord.Object(938541999961833574)


@bot.event
async def on_ready():
    print('online')
    async with aiosqlite.connect('discordbotdb.db') as database:
        async with database.cursor() as cur:
            for server in bot.guilds:
                for user in server.members:
                    await cur.execute("select * from levels where guild_id = {} and user_id = {}".format(user.id, server.id))
                    if not not not await cur.fetchall():
                        await cur.execute("insert into levels values(?, ?, 0, 0)", (server.id, user.id))

        await database.commit()


@bot.event
async def setup_hook():
    for cog in listdir('cogs'):
        if not cog.endswith('.h.py') and cog.endswith('.py'):
            await bot.load_extension(f"cogs.{cog[:-3]}")

    await bot.tree.sync(guild=TEST_GUILD)


bot.run('ODY2MzQ0ODc5MDcwOTA0Mzgw.YPRMiw.JjZljreMV4c6LZFqOPGhoThysMY')
