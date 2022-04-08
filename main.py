from discord.ext import commands
from os import listdir
import aiosqlite
import discord
from private_api_keys_go_away import TOKEN


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
                """
                 | Adds individual users to the `discordbotdb.db`
                 | database. This database is used to keep track
                 | of all the users attributes, e.g levels.
                """
                for user in server.members:
                    #! if the user does not exist in the database, add them
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

                    #! if the user does exist in the database, we add them to the database
                    #! the database is setup to have a default `false` value for the `whitelisted` column
                    await cur.execute(
                        'select * from whitelist where guild_id = {} and user_id = {}'.format(
                            server.id,
                            user.id
                        )
                    )
                    if not await cur.fetchall():
                        await cur.execute(
                            'INSERT INTO whitelist VALUES({}, {}, false)'.format(
                                server.id,
                                user.id
                            )
                        )

        await database.commit()


    async with aiosqlite.connect('stonks.db') as database:
        async with database.cursor() as cur:
            await cur.execute("SELECT guild_id FROM server_stonks")
            data = await cur.fetchall()

            #! by default the `data` variable is a list of tuples
            servers = [x[0] for x in data]
            for server in bot.guilds:
                """
                 | adds the guild to the `stonks.db` database,
                 | if it doesn't exist already. This database
                 | is used to keep track of the value o0f the
                 | currancy that has been assighned to the
                 | server.
                """
                if server.id not in servers:
                    await cur.execute(
                        'INSERT INTO server_stonks VALUES({}, "${}$", 1)'.format(
                            server.id,
                            server.name
                        )
                    )

        await database.commit()

    for cog in listdir('cogs'):
        if cog.endswith('.py') and not cog.startswith('_'):
            print('loading {}'.format(cog))
            await bot.load_extension(f"cogs.{cog[:-3]}")

    await bot.tree.sync(guild=TEST_GUILD)

    print('online')


bot.run(TOKEN)
