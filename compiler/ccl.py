import sys


def update(mem):
    print("\n")
    for c in mem:
        if c == 0:
            print(" ", end="")

        else:
            print(chr(c), end="")


def emulate():
    stack: list[int] = [0 for _ in range(255)]
    mem: list[int] = [0 for _ in range(255)]

    global stkPrt

    stkPrt = 0

    with open(r"D:\programing\0x102-discord-bot\compiler\test.cclab", "rb") as f:
        code = f.read()
        c = 0

        while code[c] != 15:
            match int(code[c]):
                case 00:
                    stack[stkPrt - 1] = stack[stkPrt - 1] + stack[stkPrt]
                    stkPrt -= 1
                    c += 1

                    update(mem)

                case 1:
                    stack[stkPrt - 1] = stack[stkPrt - 1] - stack[stkPrt]

                    update(mem)
                    stkPrt -= 1
                    c += 1

                case 2:
                    stack[stkPrt - 1] = stack[stkPrt - 1] * stack[stkPrt]
                    update(mem)
                    stkPrt -= 1
                    c += 1

                case 3:
                    stack[stkPrt - 1] = stack[stkPrt - 1] // stack[stkPrt]
                    update(mem)
                    stkPrt -= 1
                    c += 1

                case 4:
                    stack[stkPrt - 1] = stack[stkPrt - 1] % stack[stkPrt]
                    update(mem)
                    stkPrt -= 1
                    c += 1

                case 5:
                    if stack[stkPrt - 1] or stack[stkPrt]:
                        stack[stkPrt - 1] = 1
                    else:
                        stack[stkPrt - 1] = 0

                    update(mem)
                    stkPrt -= 1
                    c += 1

                case 6:
                    if stack[stkPrt - 1] and stack[stkPrt]:
                        stack[stkPrt - 1] = 1
                    else:
                        stack[stkPrt - 1] = 0

                    update(mem)
                    stkPrt -= 1
                    c += 1

                case 7:
                    if not stack[stkPrt]:
                        stack[stkPrt - 1] = 1
                    else:
                        stack[stkPrt - 1] = 0

                    update(mem)
                    stkPrt -= 1
                    c += 1

                case 8:
                    mem[stack[stkPrt]] = stack[stkPrt - 1]

                    update(mem)
                    stkPrt -= 1
                    c += 2

                case 9:
                    mem[stack[stkPrt]] = 0

                    update(mem)
                    stkPrt -= 1
                    c += 1

                case 10:
                    stack[stkPrt] = code[c + 1]

                    update(mem)
                    stkPrt += 1
                    c += 2

                case 11:
                    stack[stkPrt] = 0

                    update(mem)
                    c += 1

                case 12:
                    mem[code[c + 1]] = stack[stkPrt]

                    update(mem)
                    stkPrt -= 1
                    c += 2

                case 13:
                    stack[stkPrt] = mem[code[c + 1]]

                    update(mem)
                    c += 2

                case 14:
                    if stack[stkPrt] == 0:
                        c = code[c + 1]
                    else:
                        c += 2

                    update(mem)

                case 15:
                    sys.exit(0)

                case _:
                    c += 1

    return mem


if __name__ == "__main__":
    print(emulate())
