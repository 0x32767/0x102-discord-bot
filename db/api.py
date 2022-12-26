from aiosqlite import connect, Connection, Cursor
from typing import TypeVar, NewType, Union
from debug import Debugger


boolean = NewType("boolean", Union[True, False])
failiure = NewType("failiure", False)
guild_id = NewType("guild_id", int)
success = NewType("success", True)
user_id = NewType("user_id", int)


async def transfer_to_account(gid: guild_id, uid: user_id, amount: int, dbgr: Debugger) -> boolean:
    # the success, true if the transaction was successfull, false otherwise
    try:
        conn: Connection
        curr: Cursor
        with connect("./bank.sqlite3") as conn:
            with conn.cursor() as curr:
                await curr.execute(
                    "UPDATE accounts SET coins = coins + ? WHERE gid = ? AND uid = ?",
                    (amount, gid, uid),
                )

            await conn.commit()

    except Exception as err:
        dbgr.error(err)

    return success


async def remove_from_account(gid: guild_id, uid: user_id, amount: int, dbgr: Debugger) -> boolean:
    # the success, true if the transaction was successfull, false otherwise
    # we also want to take the bot as a param so that we can access the debugger
    try:
        conn: Connection
        curr: Cursor
        with connect("./bank.sqlite3") as conn:
            with conn.cursor() as curr:
                await curr.execute(
                    "UPDATE accounts SET coins = coins - ? WHERE gid = ? AND uid = ?",
                    (amount, gid, uid),
                )

        await conn.commit()

    except Exception as err:
        dbgr.error(err)

    return success


async def transfer_between_acccounts(gid: guild_id, from_: user_id, to: user_id, amount: int) -> boolean:
    # we only need one gid because users can only transfer coins in one guild (server)
    # and not between them
    if await remove_from_account(gid, from_, amount):
        if await transfer_to_account(gid, to, amount):
            return success

    return failiure
