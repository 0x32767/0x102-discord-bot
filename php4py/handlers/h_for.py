class hFor:
    def __init__(self, tokens) -> None:
        self._tokens: list = tokens
        self._inner: list = []
        self._counter: int = 0
        self._while: list[any] = []
        self._updater: list[any] = []

        self.parse()

    def parse(self) -> None:
        info: list[any] = []
        rec: bool = False

        # gets the tokens between a `lbrace` and `rbrace`
        for token in self._tokens:
            if token.name == "lbrace":
                rec = True

            elif token.name == "rbrace":
                rec = False

            if rec:
                info.append(token)

            info.append(token)

        self.parse_inner(info)

    def parse_inner(self, info: list[any]) -> None:
        # ($i = 0; $i < 10; $i++)
        # this is the part of the loop we are interested in
        for t in info:
            if t.name == "":
                ...

    @property
    def tokens(self) -> list:
        return self._tokens

    @property
    def inner(self) -> list:
        return self._inner

    @property
    def counter(self) -> int:
        return self._counter

    @property
    def while_(self) -> list:
        return self._while

    @property
    def updater(self) -> list:
        return self._updater
