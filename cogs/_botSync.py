from configparser import ConfigParser
from aiohttp import ClientSession
from aiosqlite import connect


class botSync:
    def __init__(self: "botSync", file: str) -> None:
        self.session: ClientSession = ClientSession()
        self.conf: ConfigParser = ConfigParser()
        self.conf.read("vars.ini")
        self.file: str = file

    async def syncLocal(self: "botSync") -> None:
        async with connect(self.file) as db:
            async with db.cursor() as curr:
                req = await self.self.session.get(
                    f"{self.conf['api']['href']}/updates/"
                )
                data = await req.json()
                del req

                for gId in data:
                    req = await self.session.get(f"{self.conf['api']['href']}/items/")
