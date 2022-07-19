import dis


def unpack_op(bytecode):
    extended_arg = 0
    for i in range(0, len(bytecode), 2):
        opcode = bytecode[i]
        if opcode >= dis.HAVE_ARGUMENT:
            oparg = bytecode[i + 1] | extended_arg
            extended_arg = (oparg << 8) if opcode == dis.EXTENDED_ARG else 0
        else:
            oparg = None
        yield (i, opcode, oparg)


def assemble(code: list[tuple(int, int or None)]):
    bl = []
    for opcode, oparg in code:
        bl += [opcode, oparg or 0]

    return bytes(bl)
