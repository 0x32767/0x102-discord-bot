from cogs._types import user_id, t_status, error, success, invalid, t_snowflakes, t_shard, guild_id
from aiosqlite import connect, Connection, Cursor, Row
from typing import Tuple, Iterable, Optional, LiteralString
from debug import Debugger


async def get_coins(uid: user_id) -> t_status:
    with connect("./bank.sqlite3") as conn:
        with conn.cursor() as curr:
            await curr.execute(
                "SELECT coins FROM accounts WHERE uid = ?",
                (uid,),
            )
            return await curr.selectone()[0]


async def transfer_to_account(uid: user_id, amount: int, dbgr: Debugger) -> t_status:
    # the success, true if the transaction was successfull, false otherwise
    try:
        conn: Connection
        curr: Cursor
        with connect("./bank.sqlite3") as conn:
            with conn.cursor() as curr:
                await curr.execute(
                    "UPDATE accounts SET coins = coins + ? WHERE uid = ?",
                    (amount, uid),
                )

            await conn.commit()

    except Exception as err:
        dbgr.error(err)
        return error

    return (success, "")


async def remove_from_account(uid: user_id, amount: int, dbgr: Debugger) -> t_status:
    # the success, true if the transaction was successfull, false otherwise
    # we also want to take the bot as a param so that we can access the debugger
    try:
        conn: Connection
        curr: Cursor
        with connect("./bank.sqlite3") as conn:
            with conn.cursor() as curr:
                if await get_coins(uid) < amount:  # if the user has not got enough coins to be removed
                    return invalid, "not enough coins"

                await curr.execute(
                    "UPDATE accounts SET coins = coins - ? WHERE uid = ?",
                    (amount, uid),
                )

        await conn.commit()

    except Exception as err:
        dbgr.error(err)
        return error, "DB error"

    return success, ""


async def transfer_between_acccounts(from_: user_id, to: user_id, amount: int) -> t_status:
    # we only need one gid because users can only transfer coins in one guild (server)
    # and not between them
    if res1 := await remove_from_account(from_, amount)[0]:
        if res2 := await transfer_to_account(to, amount)[0]:
            return success

        else:
            return res2

    else:
        return res1


async def give_item(uid: user_id, iid: int, amount: Optional[int] = 1) -> t_status:
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
                (uid,),
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


async def remove_item(uid: user_id, iid: int, amount: Optional[int] = 1) -> t_status:
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
                (uid,),
            )
            if not await curr.fetchone():
                # the users has no open record of having the item, we return a fail
                return error, "never owned item"

            else:
                # the users acount already exists so we can update it
                await curr.execute(
                    f"UPDATE item_{iid} SET coppies = coppies - ? WHERE uid = ?",
                    (amount, uid),
                )

                # remove account if they own no coppies (saves space in the db)

                await curr.execute(
                    f"SELECT coppies FROM item_{iid} WHERE uid = ?",
                    (uid),
                )

                if await curr.fetchone()[0] == 0:
                    await curr.execute(
                        f"DELETE FROM item_{iid} WHERE uid = ?",
                        (uid,),
                    )

        await conn.commit()


async def get_item(snowflakes: t_snowflakes, iid: int, get_iid: Optional[bool] = False) -> Tuple[t_status, Tuple[int | str]]:
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


async def get_all_items(snowflakes: t_snowflakes) -> Iterable[Row]:
    conn: Connection
    curr: Cursor

    with connect("./items.sqlite3") as conn:
        with conn.cursor() as curr:
            await curr.execute(
                "SELECT ? FROM items",
                (",".join(snowflakes),),
            )
            return await curr.fetchall()[0]


async def setting_off(setting: t_shard, gid: guild_id) -> t_status:
    conn: Connection
    curr: Cursor

    with connect("./settings.sqlite3") as conn:
        with conn.cursor() as curr:
            curr.execute("UPDATE settings SET ? = 0 WHERE gid = ?", (setting, gid))

        conn.commit()


async def setting_on(setting: t_shard, gid: guild_id) -> t_status:
    conn: Connection
    curr: Cursor

    with connect("./settings.sqlite3") as conn:
        with conn.cursor() as curr:
            curr.execute("UPDATE settings SET ? = 1 WHERE gid = ?", (setting, gid))

        conn.commit()


async def get_temp_dat(table_name: LiteralString, vid: str, destroy_on_found: Optional[bool] = False) -> t_status:
    conn: Connection
    curr: Cursor

    with connect("./temp.sqite3") as conn:
        with conn.cursor() as curr:
            await curr.execute(f"SELECT * FROM ? WHERE id = ?", (table_name, vid))
            if (await curr.fetchall()): # If there are any valid keys then we return true
                if destroy_on_found:
                    await curr.execute("DELETE key FROM ? WHERE id = '?'", (table_name, vid))
                    await conn.commit()
                return 

async def create_temp_dat(table_na,e: LiteralString, vid: str,) -> None:
    conn: Connection
    curr: Cursor

    with connect("./temp.sqlite3") as conn:

