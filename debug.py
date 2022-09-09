from configparser import ConfigParser
from rich.progress import progress
from rich.console import Console
from typing import Iterable
from json import load


class DebugerMetta(type):
    def __new__(cls, name: str, bases: tuple[str], attrs: dict[str, any]):
        conf = ConfigParser()
        conf.read(open("constants.conf"))
        data: dict[str, str] = load(conf["debugger"]["json"])
        """
        ::basics::

        The data is a dict that includes the folowing format:
        {
            "abreviation": "message"
        }
        We use a metta class to crete multiple functions from json ones.
        For example the axample above would corispond to:
        Debbuger.print_abreviation()
        The output would be "message", and the rest follow this format.

        ::passing params::
        of corse you may want to print something like a variable. The
        only adition would need to be a format similar to the vscode
        snippits.

        {
            "vars": "{arg1} : {arg1} : {arg2}"
        }

        The output of this wold be:
        test : test : hi
        """

        for k, v in data.items():
            attrs[k] = cls.print_ln(v, attrs["console"])

        return type(
            name,
            bases,
            attrs,
        )

    def print_ln(cls, value: str, console: "Debuger") -> function:
        def inner(*args):
            st = value
            for idx, v in enumerate(args):
                st = st.replace(f"{{arg{idx}}}", v)

            console.print(st)

        return inner


class Debuger(metta=DebugerMetta):
    def __init__(self) -> None:
        self.console: Console = Console()

    def debug(self, message: str) -> None:
        self.console.print(message)
        self.console.refresh()

    def close(self) -> None:
        self.console.clear()

    def progress(self, iterable: Iterable, description: str, total: int) -> function:
        return lambda : progress(
            iterable,
            console=self.console,
            description=description,
            total=total
        )
