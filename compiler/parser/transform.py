from sly import Lexer
from parse import parse


class CCLS(Lexer):
    tokens = {
        "NUMBER",
        "STRING",
        "IDENTIFIER",
        "KEYWORD",
        "OPERATOR",
        "SEPARATOR",
        "COMMENT",
        "WHITESPACE",
        "NEWLINE",
        "INDENT",
        "DEDENT",
        "EOF",
    }

    # Tokens
    NUMBER = r"\d+"
    STRING = r"\"[^\"]*\""
    IDENTIFIER = r"[a-zA-Z_][a-zA-Z0-9_]*"
    KEYWORD = r"(ifz|ifnz|ifn|ifnn|ifc|else|fnc|jmp|pop|push|pshpy|poppy|call|cpts|tmp)"
    OPERATOR = r"[+\-*/%<>=&|^!:]=|[+\-*/%<>&|^!:]"
    SEPARATOR = r"[\(\)\[\]\{\},;]"
    COMMENT = r"\>.*"
    WHITESPACE = r"\s+"
    NEWLINE = r"\n"
    INDENT = r"\t"
    DEDENT = r"\t"
    EOF = r"\n"

    # Ignored characters
    ignore = " \t"

    # Error handling
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.error_count = 0

    def t_error(self, t):
        self.error_count += 1
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)


if __name__ == "__main__":
    lex = CCLS()

    while True:
        parse(lex.tokenize(input("CCLS > ")))
