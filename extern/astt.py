from sly import Lexer, Parser


class DisLexer(Lexer):
    tokens = {
        "LOB",
        "RCB",
        "LSB",
        "RSB",
        "CDL",
        "ARR",
        "NUM",
        "NME",
        "STR",
        "FNC",
        "LET",
        "FOR",
        "IF",
        "USING",
        "TYP",
        "DEF",
        "CAR",
        "EXT",
    }
    literals = {"=", ";", ",", "+", "-", "/", "*", "#"}

    ignore = " \n\t"

    LOB = r"\("
    RCB = r"\)"
    LSB = r"\["
    RSB = r"\]"
    NUM = r"\d+"

    STR = r"\".*?\""

    NME = r"[a-zA-Z_][a-zA-Z0-9_]*"
    # keywords
    NME["extern"] = EXT
    NME["using"] = USING
    NME["fnc"] = FNC
    NME["let"] = LET
    NME["for"] = FOR
    NME["if"] = IF


class DisParser(Parser):
    precedence = (("left", "+", "-", "/", "*"),)
    tokens = DisLexer.tokens
    start = "lines"

    # primitives
    @_("")
    def stmt(self, p):
        return p

    @_("STR")
    def prim(self, p):
        return "str", p.STR

    @_("NUM")
    def prim(self, p):
        return "num", int(p.NUM)

    @_(
        "prim '+' prim",
        "prim '-' prim",
        "prim '/' prim",
        "prim '*' prim",
        "NME '+' prim",
        "NME '-' prim",
        "NME '/' prim",
        "NME '*' prim",
        "prim '+' NME",
        "prim '-' NME",
        "prim '/' NME",
        "prim '*' NME",
        "NME '+' NME",
        "NME '-' NME",
        "NME '/' NME",
        "NME '*' NME",
    )
    def prim(self, p):
        return p[1], p[0], p[2]

    @_("EXT STR LSB args RSB")
    def extref(self, p):
        return "ext", p.STR, p.args

    @_(
        "prim ',' prim",
        "prim ',' args",
        "prim ',' NME",
        "args ',' prim",
        "args ',' NME",
        "args ',' args",
        "NME ',' prim",
        "NME ',' args",
        "NME ',' NME",
    )
    def args(self, p):
        lst = ["rgs"]
        lst += p[0]
        lst += p[2]
        return tuple(lst)

    @_("LET NME '=' prim")
    def var(self, p):
        return "var", p.NME, p.prim

    @_("NME '=' NME")
    def vari(self, p):
        return "vra", p.NME, p.NME

    @_("NME '=' fncc")
    def vari(self, p):
        return "vra", p.NME, p.fnc

    @_("'#' RCB NME LSB")
    def dec(self, p):
        return "dec", p.NME

    @_("NME LOB RCB", "NME LOB prim RCB", "NME LOB args RCB")
    def fncc(self, p):
        if hasattr(p, "EXT"):
            return "calx", p.NME, p[3]
        return "cal", p.NME, p[2]

    @_("IF LOB NME RCB LSB lines RSB", "IF LOB NME RCB LSB line RSB")
    def ifs(self, p):
        return "ifs", p.NME, p[5]

    @_("FOR LOB fncc RCB LSB lines RSB", "FOR LOB fncc RCB LSB line RSB")
    def forr(self, p):
        return "ifs", p.fncc, p[5]

    @_(
        "FNC NME LOB RCB LSB line RSB",
        "FNC NME LOB RCB LSB lines RSB",
        "FNC NME LOB NME RCB LSB lines RSB",
        "FNC NME LOB args RCB LSB lines RSB",
    )
    def fncd(self, p):
        if hasattr(p, "line"):
            return "fnc", [], p.NME, p.line

        return "fnc", [], p.NME, p.lines

    @_("USING STR")
    def importt(self, p):
        return "imp", p.STR

    @_("var", "fncc", "ifs", "forr", "importt", "fncd", "extref", "dec", "vari")
    def stmt(self, p):
        return p[0]

    @_("stmt ';'")
    def line(self, p):
        return (p.stmt,)

    @_("line line", "lines line", "line lines")
    def lines(self, p):
        lst = []
        lst += p[0]
        lst += p[1]
        return tuple(lst)


def mk_ast(code: str) -> tuple:
    par = DisParser()
    lex = DisLexer()
    return par.parse(lex.tokenize(code))
