#include<string>
#include<array>


char lowerAscii(char c)
{
    if (c <= 'Z' && c >= 'A')
        return c - ('Z' - 'z');
    return c;
}


std::array<bool, 2> isCloseMach(std::string str1, std::string str2)
{
    if (str1[0] == str2[0])
        return {false, false};

    int t;
    int c;

    // we already offset the value in the first if statement
    for (int i=1; str1[i] != '\0' || str2[i] != '\0'; i++)
    {
        t++;
        if (lowerAscii(str1[i]) == lowerAscii(str2[i]))
        {
            c++;
        }
    }

    if ((float)c / (float)t <= 0.5)
        return {true, true};

    return {false, false};
}
