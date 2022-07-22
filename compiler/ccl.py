import sys


stack: list[int] = [0 for _ in range(255)]
mem: list[int] = [0 for _ in range(255)]

global stkPrt

stkPrt = 0


def update():
    for c in mem:
        if c == 0:
            break

        else:
            print(chr(c), end="")

    print(mem)
    print(stack)
    print()


with open("compiler/test.cclab", "rb") as f:
    code = f.read()
    c = 0

    while code[c] != 15:
        print(c)

        match int(code[c]):
            case 00:
                stack[stkPrt - 1] = stack[stkPrt - 1] + stack[stkPrt]
                stkPrt -= 1
                c += 1

                update()

            case 1:
                stack[stkPrt - 1] = stack[stkPrt - 1] - stack[stkPrt]

                update()
                stkPrt -= 1
                c += 1

            case 2:
                stack[stkPrt - 1] = stack[stkPrt - 1] * stack[stkPrt]
                update()
                stkPrt -= 1
                c += 1

            case 3:
                stack[stkPrt - 1] = stack[stkPrt - 1] // stack[stkPrt]
                update()
                stkPrt -= 1
                c += 1

            case 4:
                stack[stkPrt - 1] = stack[stkPrt - 1] % stack[stkPrt]
                update()
                stkPrt -= 1
                c += 1

            case 5:
                if stack[stkPrt - 1] or stack[stkPrt]:
                    stack[stkPrt - 1] = 1
                else:
                    stack[stkPrt - 1] = 0

                update()
                stkPrt -= 1
                c += 1

            case 6:
                if stack[stkPrt - 1] and stack[stkPrt]:
                    stack[stkPrt - 1] = 1
                else:
                    stack[stkPrt - 1] = 0

                update()
                stkPrt -= 1
                c += 1

            case 7:
                if not stack[stkPrt]:
                    stack[stkPrt - 1] = 1
                else:
                    stack[stkPrt - 1] = 0

                update()
                stkPrt -= 1
                c += 1

            case 8:
                mem[stack[stkPrt]] = stack[stkPrt - 1]

                update()
                stkPrt -= 1
                c += 1

            case 9:
                mem[stack[stkPrt]] = 0

                update()
                stkPrt -= 1
                c += 1

            case 10:
                stack[stkPrt] = code[c + 1]

                update()
                stkPrt += 1
                c += 2

            case 11:
                stack[stkPrt] = 0

                update()
                c += 1

            case 12:
                mem[code[c + 1]] = stack[stkPrt]

                update()
                stkPrt -= 1
                c += 2

            case 13:
                stack[stkPrt] = mem[code[c + 1]]

                update()
                c += 2

            case 14:
                if stack[stkPrt] == 0:
                    c = code[c + 1]
                else:
                    c += 2

                update()

            case 15:
                sys.exit(0)

            case _:
                c += 1
