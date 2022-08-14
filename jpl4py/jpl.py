from sly import Lexer, Parser
from pprint import pprint


def _():
    ...


class jplLexer(Lexer):
    tokens = {
        "NAME",
        "NUMBER",
        "STRING",
        "IF",
        "ELSE",
        "FOR",
        "JFN",
        "EQEQ",
        "NE",
        "LE",
        "GE",
        "GE",
        "PP",
        "EQ",
        "NEQ",
        "VAR",
    }
    ignore = "\t "

    literals = {
        "=",
        "+",
        "-",
        "/",
        "*",
        "(",
        ")",
        ",",
        ";",
        "{",
        "}",
        "[",
        "]",
        ">",
        "<",
    }

    # Define tokens
    IF = r"if"
    ELSE = r"else"
    FOR = r"for"
    JFN = r"jfn"
    NAME = r"[a-zA-Z_][a-zA-Z0-9_]*"
    VAR = r"\$[a-zA-Z_][a-zA-Z0-9_]*"
    STRING = r"\".*?\""

    EQEQ = r"=="
    LE = r"\<\="
    GE = r"\>\="
    PP = r"\+\+"

    @_(r"\d+")
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r"#.*")
    def COMMENT(self, t):
        pass

    @_(r"\n+")
    def newline(self, t):
        self.lineno = t.value.count("\n")


class jplParser(Parser):
    tokens = jplLexer.tokens

    def __init__(self):
        self.env = {}

    @_("NAME")
    def expr(self, p):
        return ["name", p.NAME]

    @_("VAR")
    def expr(self, p):
        return ["var", p.VAR]

    @_("NUMBER")
    def expr(self, p):
        return ["num", p.NUMBER]

    @_("STRING")
    def expr(self, p):
        return ["str", p.STRING]

    @_("expr EQEQ expr")
    def expr(self, p):
        return [p.expr0, "==", p.expr1]

    @_("expr GE expr")
    def expr(self, p):
        return [p.expr0, ">=", p.expr1]

    @_("expr LE expr")
    def expr(self, p):
        return [p.expr0, "<=", p.expr1]

    @_('expr ">" expr')
    def expr(self, p):
        return [p.expr0, ">", p.expr1]

    @_('expr "<" expr')
    def expr(self, p):
        return [p.expr0, "<", p.expr1]

    @_('expr "+" expr')
    def expr(self, p):
        return [p.expr0, "+", p.expr1]

    @_('expr "-" expr')
    def expr(self, p):
        return [p.expr0, "-", p.expr1]

    @_('expr "*" expr')
    def expr(self, p):
        return [p.expr0, "*", p.expr1]

    @_('expr "/" expr')
    def expr(self, p):
        return [p.expr0, "/", p.expr1]

    @_('expr "&" expr')
    def expr(self, p):
        return [p.expr0, "&", p.expr1]

    @_('expr "|" expr')
    def expr(self, p):
        return [p.expr0, "|", p.expr1]

    @_("expr PP")
    def expr(self, p):
        return ["inc", p.expr]

    @_('"(" expr ")"')
    def expr(self, p):
        return [p.expr]

    @_('expr "+" "(" expr ")"')
    def expr(self, p):
        return [p.expr0, "+", p.expr1]

    @_('expr "-" "(" expr ")"')
    def expr(self, p):
        return [p.expr0, "-", p.expr1]

    @_('expr "*" "(" expr ")"')
    def expr(self, p):
        return [p.expr0, "*", p.expr1]

    @_('expr "/" "(" expr ")"')
    def expr(self, p):
        return [p.expr0, "/", p.expr1]

    @_(' expr "(" expr ")"')
    def expr(self, p):
        return ["call", p.expr0, p.expr1]

    @_('IF "(" expr ")" "{" expr "}" ELSE "{" expr "}" ')
    def expr(self, p):
        return ["if", p.expr0, p.expr1, "else", p.expr2]

    @_('FOR "(" expr ";" expr ";" expr ")" "{" expr "}"')
    def expr(self, p):
        return ["for", p.expr0, p.expr1, p.expr2, p.expr3]

    @_('JFN "(" expr ")" "{" expr "}"')
    def expr(self, p):
        return ["jfn", p.expr0, p.expr1]

    @_('VAR "=" expr')
    def expr(self, p):
        return ["var", p.VAR, p.expr]

    @_('expr "," expr')
    def expr(self, p):
        return [p.expr0, p.expr1]


if __name__ == "__main__":
    lexer = jplLexer()
    parser = jplParser()
    env = {}
    while True:
        try:
            text = input("basic > ")
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            pprint(tree)
