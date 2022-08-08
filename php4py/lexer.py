from tokens import tokens
import re


code = """
echo "Hello World!";
"""


class phpToken:
    def __init__(self, raw: str, name: str, line: int, idx: int) -> None:
        self.name = name
        self.line = line
        self.raw = raw
        self.idx = idx

    def __repr__(self) -> str:
        return f"Token(name='{self.name}', line={self.line}, value='{self.raw}')"


class phpLexer:
    def __init__(self) -> None:
        self.tokens: list[phpToken] = []
        self.line: int = 0

    def tokenize(self, code: str) -> list:
        self.tokens = []
        self.line = 0

        wrd: str = ""
        sym: str = ""
        inSym: bool = False
        for idx, char in enumerate(code):
            # TODO: stop string splitting
            # ? when a string has a space in it (e.g. "Hello World!") it would split into two tokens, both are:
            # Token(name='string', line=0, value=World!')
            # But we want to have one token with the value "Hello World!"
            if char == "\n":
                self.line += 1
                wrd = ""

            elif char in [" ", "}", "]", ",", ";", "=", ":", "(", ")", "{", "[", "<", ">", "+", "-", "*", "/", "%", "!"]:
                self.tokens.append(self.identify(wrd, idx))

                if char in [">", "<", "=", "+", "-", "!"]:
                    if inSym:
                        sym += char
                        self.identify(sym, idx)
                        inSym = False

                    else:
                        sym = char
                        inSym = True

                self.tokens.append(self.identify(char, idx))
                wrd = ""

            else:
                wrd += char

        self.tokens.append(self.identify(wrd, idx))

        self.tokens = [t for t in self.tokens if t is not None]

        return self.tokens

    def identify(self, wrd: str, idx: int) -> phpToken:
        if wrd == " ":
            return None

        for rgx, name in tokens.items():
            if not not re.match(rgx, wrd):
                print(wrd, name)

            if re.match(rgx, wrd):
                return phpToken(wrd, name, self.line, idx)


if __name__ == "__main__":
    lexer: phpLexer = phpLexer()
    while True:
        for token in lexer.tokenize(input("php >>> ")):
            print(token)
