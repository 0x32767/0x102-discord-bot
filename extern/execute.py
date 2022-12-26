from pprint import pprint
from astt import mk_ast


class RuntimeEnvironment:
    def __init__(self) -> None:
        self.environment = {}
        # we put all the ast s in one list, this is so that all
        # added scripts can be linked as add time
        self.asts = []

    def add_script(self, code: str) -> None:
        self.asts += mk_ast(code)
        # we add the ast instead of appending it, this is so that
        # the tuples are extracted into their elemets
        # [] + (1, 2, 3, 4, 5, 6, 7, 8, 9)
        # [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def execute_scripts(self, env: dict[str, str | int]) -> None:...
