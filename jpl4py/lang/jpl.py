from ast import parse
from errors.lex_errors.iligal_character import IllegalCharacterError
from sly import Lexer, Parser


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
        "LE",
        "GE",
        "GE",
        "PP",
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

    def error(self, t):
        raise IllegalCharacterError(self.lineno, [t.value])


class jplParser(Parser):
    tokens = jplLexer.tokens

    def __init__(self):
        self.env = {}

    @_("NAME")
    def expr(self, p):
        return ("name", p.NAME)

    @_("VAR")
    def expr(self, p):
        return ("var", p.VAR)

    @_("NUMBER")
    def expr(self, p):
        return p.NUMBER

    @_("STRING")
    def expr(self, p):
        return p.STRING

    @_("expr EQEQ expr")
    def expr(self, p):
        return ("==", p.expr0, p.expr1)

    @_("expr GE expr")
    def expr(self, p):
        return ("GEEQ", p.expr0, p.expr1)

    @_("expr LE expr")
    def expr(self, p):
        return ("LTEQ", p.expr0, p.expr1)

    @_("expr NEQ expr")
    def expr(self, p):
        return ("NEQ", p.expr0, p.expr1)

    @_('expr ">" expr')
    def expr(self, p):
        return ("GT", p.expr0, p.expr1)

    @_('expr "<" expr')
    def expr(self, p):
        return ("LT", p.expr0, p.expr1)

    @_('expr "+" expr')
    def expr(self, p):
        return ("add", p.expr0, p.expr1)

    @_('expr "-" expr')
    def expr(self, p):
        return ("sub", p.expr0, p.expr1)

    @_('expr "*" expr')
    def expr(self, p):
        return ("mul", p.expr0, p.expr1)

    @_('expr "/" expr')
    def expr(self, p):
        return ("div", p.expr0, p.expr1)

    @_('expr "&" expr')
    def expr(self, p):
        return ("and", p.expr0, p.expr1)

    @_('expr "|" expr')
    def expr(self, p):
        return ("or", p.expr0, p.expr1)

    @_("expr PP")
    def expr(self, p):
        return ("inc", p.expr)

    @_('"(" expr ")"')
    def expr(self, p):
        return ("bracket", p.expr)

    @_('expr "+" "(" expr ")"')
    def expr(self, p):
        return ("add", p.expr0, p.expr1)

    @_('expr "-" "(" expr ")"')
    def expr(self, p):
        return ("sub", p.expr0, p.expr1)

    @_('expr "*" "(" expr ")"')
    def expr(self, p):
        return ("mul", p.expr0, p.expr1)

    @_('expr "/" "(" expr ")"')
    def expr(self, p):
        return ("div", p.expr0, p.expr1)

    @_(' NAME "(" expr ")"')
    def expr(self, p):
        return ("call", p.NAME, p.expr)

    @_('NAME "(" ")"')
    def expr(self, p):
        return ("call", p.NAME, [])

    @_('IF "(" expr ")" "{" expr "}" ELSE "{" expr "}" ')
    def expr(self, p):
        return ("if", p.expr0, p.expr1, p.expr2)

    @_('FOR "(" expr ";" expr ";" expr ")" "{" expr "}"')
    def expr(self, p):
        return ("for", p.expr0, p.expr1, p.expr2, p.expr3)

    @_('JFN NAME "(" expr ")" "{" expr "}"')
    def expr(self, p):
        return ("jfn", p.expr0, p.expr1)

    @_('JFN NAME "(" ")" "{" expr "}"')
    def expr(self, p):
        return ("fn", p.NAME, [], p.expr)

    @_('VAR "=" expr')
    def expr(self, p):
        return ("vardec", p.VAR, p.expr)

    @_('expr "," expr')
    def expr(self, p):
        return [p.expr0, p.expr1]

    @_('VAR "," VAR')
    def expr(self, p):
        return [p.VAR0, p.VAR1]

    @_("expr \n expr")
    def expr(self, p):
        return [p.expr0, p.expr1]


if __name__ == "__main__":
    lexer = jplLexer()
    parser = jplParser()

    while True:
        tokens = lexer.tokenize(input("> "))
        print(parser.parse(tokens))
