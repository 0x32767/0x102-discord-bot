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

from discord.ext import commands  # type: ignore
from typing import Callable, Any


recorded_commands: list[commands.Command] = []


"""
::NOTE::
========
This is a setup function for the help command.
"""


def record(usage: str = "/") -> Callable[[Any], Any]:
    def wrapper(func: commands.Command) -> commands.Command:
        if usage == "/":
            recorded_commands.append({"f": func, "u": f"/{func.name}"})

        else:
            recorded_commands.append({"f": func, "u": usage})

        return func

    return wrapper
