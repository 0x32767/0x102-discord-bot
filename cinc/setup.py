def fn2bc(body) -> None:
    line = 1
    byte = 0
    varc = 0
    for item in body.block_items:
        match item.__class__.__name__:
            case "FuncCall":
                byte = handleFuncCall(item, line, byte)

            case "Return":
                byte = handelReturn(item, line, byte)

            case "Decl":
                varc, byte = handleDecl(item, line, byte, varc)

            case _:
                print(item)

        line += 1


def handleFuncCall(item, ln, byte) -> int:
    print(f"{str(ln).zfill(4)}   {str(byte*2).zfill(3)} LOAD_GLOBAL   0 ({item.name.name})"); byte += 1
    print(f"       {str(byte*2).zfill(3)} LOAD_CONST    1 ({item.args.exprs[0].value})"); byte += 1
    print(f"       {str(byte*2).zfill(3)} CALL_FUNCTION 1"); byte += 1
    print(f"       {str(byte*2).zfill(3)} POP_TOP"); byte += 1
    print()
    return byte


def handelReturn(item, ln, byte) -> int:
    print(f"{str(ln).zfill(3)}    {str(byte*2).zfill(3)} LOAD_CONST    0 ({item.expr.value})"); byte += 1
    print(f"       {str(byte*2).zfill(3)} RETURN_VALUE"); byte += 1
    print()
    return byte


def handleDecl(item, ln, byte, varc) -> int:
    match item.init.__class__.__name__:
        case "Constant":
            print(f"{str(ln).zfill(4)}   {str(byte*2).zfill(3)} LOAD_CONST    0 ({item.init.value})"); byte += 1
            print(f"       {str(byte*2).zfill(3)} STORE_FAST    0 ({item.type.declname})"); byte += 1
            print()

            return varc, byte

        case "BinaryOp":
            print(f"{str(ln).zfill(4)}   {str(byte).zfill(3)} {item.init.left.name}")
            print(item.init.op)
            print(item.init.right.name)
            print(item.type.declname)
            print()

            return varc, byte
