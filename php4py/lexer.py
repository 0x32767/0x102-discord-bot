from tokens import tokens as _tokens
from parser import jplParser
import re


class jplToken:
    def __init__(self, raw: str, name: str, line: int, idx: int) -> None:
        self.name = name
        self.line = line
        self.raw = raw
        self.idx = idx

    def __repr__(self) -> str:
        return f"Token(name='{self.name}', line={self.line}, value='{self.raw}')"


class jplLexer:
    def __init__(self) -> None:
        self.tokens: list[jplToken] = []
        self.line: int = 0

    def tokenize(self, code: str) -> list:
        self.tokens = []
        self.line = 0

        wrd: str = ""
        inStr: bool = False
        string: str = ""

        for idx, char in enumerate(code):
            # TODO: stop string splitting
            # ? when a string has a space in it (e.g. "Hello World!") it would split into two tokens, both are:
            # Token(name='string', line=0, value=World!')
            # But we want to have one token with the value "Hello World!"
            if char == "\n":
                self.line += 1
                wrd = ""

            elif char in ("'", '"') and not inStr:
                inStr = True
                string = char
                continue

            elif char in ("'", '"'):
                string += char
                self.tokens.append(jplToken(string, "string", self.line, idx))
                inStr = False
                string = ""
                continue

            elif inStr:
                string += char
                continue

            elif char in [" ", "}", "]", ",", ";", "=", ":", "(", ")", "{", "[", "<", ">", "+", "-", "*", "/", "%", "!"]:
                self.tokens.append(self.identify(wrd, idx))
                self.tokens.append(self.identify(char, idx))
                wrd = ""

            else:
                wrd += char

        self.tokens.append(self.identify(wrd, idx))

        self.tokens = self.clean()

        return self.tokens

    def clean(self) -> list[jplToken]:
        tok: list[jplToken] = []
        las: jplToken = None

        for token in self.tokens:
            if token is None:
                continue

            elif token.name == "eq":
                if las.raw == "=":
                    tok.pop()
                    tok.append(jplToken("==", "eqeq", self.line, token.idx))

                elif las.raw == "!":
                    tok.pop()
                    tok.append(jplToken("!=", "ne", self.line, token.idx))

                elif las.raw == ">":
                    tok.pop()
                    tok.append(jplToken(">=", "ge", self.line, token.idx))

                elif las.raw == "<":
                    tok.pop()
                    tok.append(jplToken("<=", "le", self.line, token.idx))

                continue

            las = token
            tok.append(token)

        return tok

    def identify(self, wrd: str, idx: int) -> jplToken:
        if wrd == " ":
            return None

        for rgx, name in _tokens.items():
            if re.match(rgx, wrd):
                return jplToken(wrd, name, self.line, idx)


if __name__ == "__main__":
    parser: jplParser = jplParser()
    lexer: jplLexer = jplLexer()
    while True:
        tokens = lexer.tokenize(input("jpl >>> "))
        parser.parse(tokens)
