from typing import Iterable, Type, Any, Tuple, TypeVar
from rich.console import Console
from rich.progress import track
import json


class DebuggerMeta(type):
    def __new__(cls: Type["DebuggerMeta"], name: str, bases: Tuple[Type[str]], attrs: dict[str, Any]):
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
            attrs[f"print_{k}"] = DebuggerMeta.print_ln(v, attrs["console"])

        return type(name, bases, attrs)

    @staticmethod
    def print_ln(value: str, console: Type["Debugger"]):
        def inner(self: "Debugger", *args):
            st = value
            for idx, v in enumerate(args):
                # we replace the argX with a value that was passed into the function
                st = st.replace(f"{{arg{idx}}}", str(v))

            console.print(self, st)

        return inner


class Debugger(metaclass=DebuggerMeta):
    def __init__(self) -> None:
        self.debugger = Console()

    # The self.console is passed by the meta class
    def print(self, message: str) -> None:
        self.console.print(message)

    def close(self) -> None:
        self.console.clear()

    def progress(self, iterable: Iterable, description: str, total: int):
        return track(iterable, console=self.console, description=description, total=total)

    def __getattr__(self, __name: str):
        if value := self.__dict__.get(__name, None):
            return value

        return lambda x: print(f"{self.__class__.__name__}.{__name} does not exist, did you mean {self.props}")
