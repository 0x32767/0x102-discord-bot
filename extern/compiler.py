from pprint import pprint
from typing import List
from astt import mk_ast


ast = mk_ast(
    """
let x = 1;
let y = 2;
print("{}, {}", x, y);
;
"""
)


def get_var_names(ast) -> List[str]:
    return [line[1] for line in ast if line[0] == "var"]


def push_reg(reg):
    return f"psh %{reg}"


def call_fnc(name, args, vars):
    f = []
    for i in args[-1:]:
        if i[0] == "str":
            f.append(f"psh ${i[1]}")

        else:
            f.append(push_reg(vars.index(i)))

    f.append(f"psh &{name}")
    f.append(f"cal")
    return "\n".join(f)


def create_binop(op, var, val) -> str:
    if op == "+":
        if val[0] == "num":
            return f"add {var}, {val[1]}"

    elif op == "-":
        if val[0] == "num":
            return f"sub {var}, {val[1]}"

    elif op == "/":
        if val[0] == "num":
            return f"div {var}, {val[1]}"

    elif op == "+":
        if val[0] == "num":
            return f"mul {var}, {val[1]}"


def create_var(var, initv):
    if initv[0] == "num":
        return f"iit %{var}, ${initv[1]}"


def kill_var(name) -> None:
    return f"dmp %{name}"


def jpl_compile(ast):
    instructions = []

    var_names = get_var_names(ast)

    for i in ast:
        if i[0] == "vari":
            instructions.append(create_binop(i[2], f"%{var_names.index(i[1])}", i[-1]))

        elif i[0] == "var":
            instructions.append(create_var(var_names.index(i[1]), i[-1]))

        elif i[0] == "cal":
            instructions.append(call_fnc(i[1], i[2], var_names))
            print(i)

        else:
            print(i[0])

    for idx in range(len(var_names)):
        instructions.append(kill_var(idx))

    return "\n".join(instructions)


# pprint(ast)
print(jpl_compile(ast))
