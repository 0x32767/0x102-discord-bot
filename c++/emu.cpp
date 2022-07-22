#include <array>

int emulate(std::array<int, 512> tape, std::array<int, 255> stk, std::array<int, 255> mem, int stkPtr);
void update(std::array<int, 512> tape, std::array<int, 255> stk, std::array<int, 255> mem, int stkPtr);

int main()
{
    std::array<int, 255> stk;
    std::array<int, 512> tape;
    std::array<int, 255> mem;
    int stackPtr = 0;

    return emulate(tape, stk, mem, stackPtr);
}

int emulate(std::array<int, 512> tape, std::array<int, 255> stk, std::array<int, 255> mem, int stkPtr)
{
    int c = 0;
    while (c <= 512 || tape[c] != 15)
    {
        switch (tape[c])
        {
        case 0:
            stk[stkPtr - 1] = stk[stkPtr - 1] + stk[stkPtr];
            stkPtr -= 1;
            c += 1;
            update(tape, stk, mem, stkPtr);

        case 1:
            stk[stkPtr - 1] = stk[stkPtr - 1] - stk[stkPtr];

            stkPtr -= 1;
            c += 1;
            update(tape, stk, mem, stkPtr);

        case 2:
            stk[stkPtr - 1] = stk[stkPtr - 1] * stk[stkPtr];
            stkPtr -= 1;
            c += 1;
            update(tape, stk, mem, stkPtr);

        case 3:
            stk[stkPtr - 1] = stk[stkPtr - 1];
            stkPtr -= 1;
            c += 1;
            update(tape, stk, mem, stkPtr);

        case 4:
            stk[stkPtr - 1] = stk[stkPtr - 1] % stk[stkPtr];
            stkPtr -= 1;
            c += 1;
            update(tape, stk, mem, stkPtr);

        case 5:
            if (stk[stkPtr - 1] || stk[stkPtr])
            {
                stk[stkPtr - 1] = 1;
            }
            else
            {
                stk[stkPtr - 1] = 0;
            }

            stkPtr -= 1;
            c += 1;
            update(tape, stk, mem, stkPtr);

        case 6:
            if (stk[stkPtr - 1] && stk[stkPtr])
            {
                stk[stkPtr - 1] = 1;
            }
            else
            {
                stk[stkPtr - 1] = 0;
            }

            stkPtr -= 1;
            c += 1;
            update(tape, stk, mem, stkPtr);

        case 7:
            if (not stk[stkPtr])
            {
                stk[stkPtr - 1] = 1;
            }
            else
            {
                stk[stkPtr - 1] = 0;
            }

            stkPtr -= 1;
            c += 1;
            update(tape, stk, mem, stkPtr);

        case 8:
            mem[stk[stkPtr]] = stk[stkPtr - 1];

            stkPtr -= 1;
            c += 1;
            update(tape, stk, mem, stkPtr);

        case 9:
            mem[stk[stkPtr]] = 0;

            stkPtr -= 1;
            c += 1;
            update(tape, stk, mem, stkPtr);

        case 10:
            stk[stkPtr] = tape[c + 1];

            stkPtr += 1;
            c += 2;
            update(tape, stk, mem, stkPtr);

        case 11:
            stk[stkPtr] = 0;

            c += 1;
            update(tape, stk, mem, stkPtr);

        case 12:
            mem[tape[c + 1]] = stk[stkPtr];

            stkPtr -= 1;
            c += 2;
            update(tape, stk, mem, stkPtr);

        case 13:
            stk[stkPtr] = mem[tape[c + 1]];

            c += 2;
            update(tape, stk, mem, stkPtr);

        case 14:
            if (stk[stkPtr] == 0)
            {
                c = tape[c + 1];
            }
            else
            {
                c += 2;
            }

            update(tape, stk, mem, stkPtr);

        case 15:
            break;
        }
    }

    return 0;
}

void update(std::array<int, 512> tape, std::array<int, 255> stk, std::array<int, 255> mem, int stkPtr)
{
}

extern "C"
{
    int emulate(std::array<int, 512> tape, std::array<int, 255> stk, std::array<int, 255> mem, int stkPtr)
    {
        return emulate(tape, stk, mem, stkPtr);
    }
}
