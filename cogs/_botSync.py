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

from configparser import ConfigParser
from aiosqlite import connect
from json import loads
import asyncio
import httpx

"""
The botSync module
==================

::CONTEXT::

The developer of the is bot is collaborating with the owner of a
series of other discord bots 'Arty Studios' to create an easy to
use collection of bots.

::use::
This is to sync the bot`s database with a local one. This is to
prevent accidental DDoS attacks, from frequent requests to the
remote db.
This also optimizes the bot`s performance.

::example::
If a server were to update its settings, the bot would edit the
local database and update a cache of servers who have changed
their settings, this is again to optimize the bot`s performance.
And that of other bots too.
"""


class botSync:
    def __init__(self: "botSync", file: str) -> None:
        self.conf: ConfigParser = ConfigParser()
        self.conf.read("vars.ini")
        self.file: str = file

    async def getCloud(self: "botSync") -> str:
        """
        | This function will get the guilds with the changed settings (for
        | optimization purposes) and will then iterate over all said guilds
        | and edit them in a local database.
        |
        | This function should
        """
        async with self.session.get(f"{self.baseUrl}edited/") as response:
            txt = await response.text()
            guilds: list[int] = loads(txt)

        async with httpx.AsyncClient() as client:
            tasks: list[asyncio.Task] = [asyncio.create_task(self.serverRequest(client, guild)) for guild in guilds]

        res: httpx.Response = await asyncio.gather(*tasks)
        return res

    async def serverRequest(self: "botSync", session: httpx.AsyncClient, gUid: int) -> None:
        await session.get(f"{self.baseUrl}server/{gUid}")
