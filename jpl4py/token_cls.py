class jplToken:
    def __init__(self, raw: str, name: str, line: int, idx: int) -> None:
        self.name = name
        self.line = line
        self.raw = raw
        self.idx = idx

    @property
    def value(self) -> str:
        return self.raw

    def __repr__(self) -> str:
        return f"Token(name='{self.name}', line={self.line}, value='{self.raw}')"
