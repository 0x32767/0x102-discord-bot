#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <string>
#include <array>

enum instructions
{
    add = 0,
    sub = 1,
    mul = 2,
    div = 3,
    mod = 4,
    or_ = 5,
    nd_ = 6, // and
    nt_ = 7, // or
    all = 8,
    dea = 9,
    psh = 10,
    pop = 11,
    jez = 12,
    jnz = 13,
    qit = 14
};

int main()
{
    std::array<int, 1000> instruct;
    std::array<int, 999> memory;
    std::array<int, 100> stack;

    int stackSize = 0;

    int idx = 0;

    for (; idx <= 1000;)
    {
        switch (instruct[idx])
        {
        case add:
            stack[stackSize] = stack[stackSize] + stack[stackSize + 1];

            stack[stackSize + 1] = 0;
            stackSize--;
            break;

        case sub:
            stack[stackSize] = stack[stackSize] - stack[stackSize + 1];

            stack[stackSize + 1] = 0;
            stackSize--;
            break;

        case mul:
            stack[stackSize] = stack[stackSize] * stack[stackSize + 1];

            stack[stackSize + 1] = 0;
            stackSize--;
            break;

        case div:
            stack[stackSize] = stack[stackSize] / stack[stackSize + 1];

            stack[stackSize + 1] = 0;
            stackSize--;
            break;

        case mod:
            stack[stackSize] = stack[stackSize] % stack[stackSize + 1];

            stack[stackSize + 1] = 0;
            stackSize--;
            break;

        case or_:
            stack[stackSize] = stack[stackSize] | stack[stackSize + 1];

            stack[stackSize + 1] = 0;
            stackSize--;
            break;

        case nd_:
            stack[stackSize] = stack[stackSize] & stack[stackSize + 1];

            stack[stackSize + 1] = 0;
            stackSize--;
            break;

        case nt_:
            stack[stackSize] = stack[stackSize] != stack[stackSize + 1];

            stack[stackSize + 1] = 0;
            stackSize--;
            break;

        case all:
            memory[instruct[idx + 1]] = instruct[idx + 2];
            idx += 3;
            break;

        case dea:
            memory[instruct[idx + 1]] = 0;
            idx += 2;
            break;

        case psh:
            memory[instruct[idx + 1]] = stack[stackSize];
            stackSize++;
            idx += 2;
            break;

        case pop:
            stack[stackSize] = memory[instruct[idx + 1]];
            stackSize++;
            idx += 2;
            break;

        case jez:
            if (stack[stackSize] == 0)
            {
                idx = instruct[idx + 1];
                idx += 2;
            }

        case jnz:
            if (stack[stackSize] != 0)
            {
                idx = instruct[idx + 1];
                idx += 2;
            }
        case qit:
            return 0;
        }
    }
}
