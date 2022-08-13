from handlers.h_while import hWhile
from handlers.h_else import hElse
from handlers.h_for import hFor
from handlers.h_fnc import hFnc
from handlers.h_if import hIf


class jplParser:
    def __init__(self) -> None:
        self.tokens: list = []
        self.tree: list[any] = []

    def parse(self, tokens_: list) -> None:
        self.tokens = tokens_

        for idx, token in enumerate(self.tokens):
            if token.name == "for":
                print(self.get_nested_content(self.tokens[idx:], hFor))

            elif token.name in ["jfn", "cfn", "pfn"]:
                print(self.get_nested_content(self.tokens[idx:], hFnc))

            elif token.name == "if":
                print(self.get_nested_content(self.tokens[idx:], hIf))

            elif token.name == "else":
                print(self.get_nested_content(self.tokens[idx:], hElse))

            elif token.name == "while":
                print(self.get_nested_content(self.tokens[idx:], hWhile))

    def get_nested_content(self, tokens: list, cls: object) -> None:
        nest_level: int = 0
        inner: list = []

        for t in tokens:
            if t.name == "lbrace":
                nest_level += 1

            elif t.name == "rbrace":
                nest_level -= 1
                if nest_level == 0:
                    inner.append(t)
                    break

            inner.append(t)

        return cls(inner)
