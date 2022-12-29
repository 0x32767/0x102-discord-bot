from cogs._types import user_id, guild_id, status, error, success, invalid, snowflakes
from typing import TypeVar, NewType, Union, Literal, Tuple, Iterable
from aiosqlite import connect, Connection, Cursor, Row
from debug import Debugger


async def get_coins(gid: guild_id, uid: user_id) -> status:
    with connect("./bank.sqlite3") as conn:
        with conn.cursor() as curr:
            await curr.execute(
                "SELECT coins FROM accounts WHERE gid = ? AND uid = ?",
                (gid, uid),
            )
            return await curr.selectone()[0]


async def transfer_to_account(gid: guild_id, uid: user_id, amount: int, dbgr: Debugger) -> status:
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
        return error

    return (success, "")


async def remove_from_account(gid: guild_id, uid: user_id, amount: int, dbgr: Debugger) -> status:
    # the success, true if the transaction was successfull, false otherwise
    # we also want to take the bot as a param so that we can access the debugger
    try:
        conn: Connection
        curr: Cursor
        with connect("./bank.sqlite3") as conn:
            with conn.cursor() as curr:
                if await get_coins(gid, uid) < amount:  # if the user has not got enough coins to be removed
                    return invalid, "not enough coins"

                await curr.execute(
                    "UPDATE accounts SET coins = coins - ? WHERE gid = ? AND uid = ?",
                    (amount, gid, uid),
                )

        await conn.commit()

    except Exception as err:
        dbgr.error(err)
        return error, "DB error"

    return success, ""


async def transfer_between_acccounts(from_: user_id, to: user_id, amount: int) -> status:
    # we only need one gid because users can only transfer coins in one guild (server)
    # and not between them
    if res1 := await remove_from_account(from_, amount)[0]:
        if res2 := await transfer_to_account(to, amount)[0]:
            return success

        else:
            return res2

    else:
        return res1


async def give_item(gid: guild_id, uid: user_id, iid: int, amount: int = 1) -> status:
    """
    The records are structured in a db efficiant way where every item has its own
    table with the records as the owner and amount.

    +---------------------+
    |        item_x       |
    +-----+-----+---------+
    | gid | uid | coppies |
    +-----+-----+---------+
    | 123 | 456 | 1       |
    +-----+-----+---------+

    There is also a master table where the name of items are stored, and other
    information.
    """
    with connect("./items.sqlite3") as conn:
        with conn.cursor() as curr:
            await curr.execute(
                "SELECT 1 WHERE uid = ?",
                (gid,),
            )
            if not await curr.fetchone():
                # the users has no open record of having the item, we make one
                await curr.execute(
                    f"INSERT INTO item_{iid} VALUES(?, ?)",
                    (uid, amount),
                )

            else:
                # the users acount already exists so we can update it
                await curr.execute(
                    f"UPDATE item_{iid} SET coppies = coppies + ? WHERE uid = ?",
                    (amount, uid),
                )

        await conn.commit()


async def remove_item(uid: user_id, iid: int, amount: int = 1) -> status:
    """
    The records are structured in a db efficiant way where every item has its own
    table with the records as the owner and amount.

    +---------------------+
    |        item_x       |
    +-----+-----+---------+
    | gid | uid | coppies |
    +-----+-----+---------+
    | 123 | 456 | 1       |
    +-----+-----+---------+

    There is also a master table where the name of items are stored, and other
    information.
    """
    with connect("./items.sqlite3") as conn:
        with conn.cursor() as curr:
            await curr.execute(
                "SELECT 1 WHERE gid = ? AND uid = ?",
                (uid,),
            )
            if not await curr.fetchone():
                # the users has no open record of having the item, we return a fail
                return error, "never owned item"

            else:
                # the users acount already exists so we can update it
                await curr.execute(
                    f"UPDATE item_{iid} SET coppies = coppies - ? WHERE gid = ? AND uid = ?",
                    (amount, uid),
                )

                # remove account if they own no coppies (saves space in the db)

                await curr.execute(
                    f"SELECT coppies FROM item_{iid} WHERE gid = ? AND uid = ?",
                    (uid),
                )

                if await curr.fetchone()[0] == 0:
                    await curr.execute(
                        f"DELETE FROM item_{iid} WHERE gid = ? AND uid = ?",
                        (uid,),
                    )

        await conn.commit()


async def get_item(snowflakes: snowflakes, iid: int, get_iid: bool = False) -> Tuple[status, Tuple[int | str]]:
    with connect("./items.sqlite3") as conn:
        with conn.cursor() as curr:
            if not get_iid:  # if we want to get some data with snowflakes
                await curr.execute(
                    "SELECT ? FROM items WHERE iid = ?",
                    (",".forat(snowflakes), iid),
                )
                return await curr.fetchone()[0]

            # if we want to get all the ids of the items
            await curr.execute("SELECT iid FROM items")
            return await curr.fetchall()


async def get_all_items(snowflakes: snowflakes) -> Iterable[Row]:
    conn: Connection
    curr: Cursor

    with connect("./items.sqlite3") as conn:
        with conn.cursor() as curr:
            await curr.execute(
                "SELECT ? FROM items",
                (",".forat(snowflakes),),
            )
            return await curr.fetchall()[0]
