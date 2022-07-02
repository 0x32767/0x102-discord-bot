from discord import Interaction
from cogs._luaCtx import luaCtx
from lupa import LuaRuntime


class LuaDiscordRuntimeEnvironment:
    def __init__(self: "LuaDiscordRuntimeEnvironment") -> None:
        self.lua: LuaRuntime = LuaRuntime(unpack_returned_tuples=True)
        self.functions: dict[str, callable] = {}

    async def register_function(self: "LuaDiscordRuntimeEnvironment", name: str, function: callable) -> None:
        if not callable(function):
            raise TypeError("function must be callable")

        if name in self.functions:
            raise ValueError("function already registered")

        self.functions[name]: callable = self.lua.eval(function)

    async def invoke(self: "LuaDiscordRuntimeEnvironment", name: str, ctx: Interaction, args: dict) -> None:
        self.functions[name](luaCtx(ctx), args)
