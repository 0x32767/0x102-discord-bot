class hFor:
    def __init__(self, tokens) -> None:
        from lexer import jplToken

        self._tokens: list["jplToken"] = tokens
        self._updater: list["jplToken"] = []
        self._inner: list["jplToken"] = []
        self._while: list["jplToken"] = []
        self._counter: int = 0

        self.parse()

    def parse(self) -> None:
        from lexer import jplToken

        info: list["jplToken"] = []
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

        inner: list["jplToken"] = []
        nest: int = 0
        rec = False
        for token in self._tokens:
            if token.name == "lbrace":
                nest += 1
                rec = True

            elif token.name == "rbrace":
                nest -= 1

                if rec and nest == 0:
                    inner.append(token)
                    rec = False

            if rec:
                inner.append(token)

        self._inner = inner
        self.parse_inner(info)

    def parse_inner(self, info: list[any]) -> None:
        from lexer import jplToken

        section: list["jplToken"] = []
        for t in info:
            if t.name == "lparen":
                continue

            elif t.name == "rparen":
                self._updater = section
                return

            elif t.name == "semicolon":
                if not self._counter:
                    self._counter = section
                    section = []
                    continue

                elif not self._while:
                    self._while = section
                    section = []
                    continue

                elif not self._updater:
                    self._updater = section
                    section = []
                    continue

            section.append(t)

    def __repr__(self) -> str:
        return f"hFor(counter={self._counter}, updater={self._updater}, while={self._while}, inner=[{self._inner}])"

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
