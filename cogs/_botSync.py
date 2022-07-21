from configparser import ConfigParser
from aiosqlite import connect
from aiohttp import ClientSession
from json import loads


class botSync:
    def __init__(self: "botSync", file: str) -> None:
        self.session: ClientSession = ClientSession()
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
            # this is a list of guild ids [1, 2, 3, 4, 5]

            del txt

        async with connect(self.file) as conn:
            async with conn.curr() as curr:
                for guildId in guilds:
                    async with self.session.get(f"{self.baseUrl}items/{guildId}/") as res:
                        """
                        | The response from: http://XX.XXX.XXX.XX/items/{guildId}/
                        | would return a json object that looks like this:
                        |
                        | {
                        |  "id": 0,
                        |  "use_whitelisting": false,
                        |  "use_blacklisting": false,
                        |  "allow_links": false,
                        |  "spam_mod": false,
                        |  "auto_mod": false,
                        |  "logging": false,
                        |  "run_cc": false,
                        |  "reputation": false
                        | }
                        """
                        txt = await res.text()
                        guild: dict = loads(txt)
                        del txt

                        curr.execute(f"""
                            INSERT INTO settings VALUES(
                                ?, ?, ?, ?, ?, ?, ?, ?
                            );
                            """, (
                                guildId,
                                int(guild["use_whitelisting"]),
                                int(guild["use_blacklisting"]),
                                int(guild["allow_links"]),
                                int(guild["spam_mod"]),
                                int(guild["auto_mod"]),
                                int(guild["logging"]),
                                int(guild["run_cc"]),
                                int(guild["reputation"])
                            )
                        )

    @property
    def baseUrl(self: "botSync") -> str:
        return self.conf.get("api", "url")
