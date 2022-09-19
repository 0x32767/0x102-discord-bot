from rich.console import Console
from rich.progress import track
from typing import Iterable
import json


class DebuggerMeta(type):
    def __new__(cls: "DebuggerMeta", name: str, bases: tuple[str], attrs: dict[str, any]):
        data: dict[str, str] = json.load(open("assets\\debug.json", "r"))
        """
        ::basics::

        The data is a dict that includes the following format:
        {
            "abbreviation": "message"
        }
        We use a meta class to crete multiple functions from json ones.
        For example the example above would correspond to:
        Debugger.print_abbreviation()
        The output would be "message", and the rest follow this format.

        ::passing params::
        of corse you may want to print something like a variable. The
        only addition would need to be a format similar to the vscode
        snippets.

        {
            "vars": "{arg1} : {arg1} : {arg2}"
        }

        The output of this wold be:
        test : test : hi
        """

        attrs["console"] = Console()
        attrs["props"] = list(data.keys())

        for k, v in data.items():
            attrs[f"print_{k}"] = cls.print_ln(v, attrs["console"])

        return type(name, bases, attrs)

    def print_ln(value: str, console: "Debugger"):
        def inner(self: any, *args):
            st = value
            for idx, v in enumerate(args):
                # we replace the argX with a value that was passed into the function
                st = st.replace(f"{{arg{idx}}}", str(v))

            console.print(st)

        return inner


class Debugger(metaclass=DebuggerMeta):
    # The self.console is passed by the meta class
    def print(self: "Debugger", message: str) -> None:
        self.console.print(message)

    def close(self: "Debugger") -> None:
        self.console.clear()

    def progress(self: "Debugger", iterable: Iterable, description: str, total: int):
        return track(iterable, console=self.console, description=description, total=total)

    def __getattr__(self: "Debugger", __name: str):
        if value := self.__dict__.get(__name):
            return value

        return lambda x: print(f"{self.__class__.__name__}.{__name} does not exist, did you mean {self.props}")
