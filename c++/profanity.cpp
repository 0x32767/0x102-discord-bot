#include<string>
#include<array>


char lowerAscii(char c)
{
    if (c <= 'Z' && c >= 'A')
        return c - ('Z' - 'z');
    return c;
}


bool isCloseMach(std::string str1, std::string str2)
{
    if (str1[0] != str2[0])
        return false;

    int t;
    int c;

    // we already offset the value in the first if statement
    for (int i=1; str1[i] != '\0' || str2[i] != '\0'; i++)
    {
        t++;
        if (lowerAscii(str1[i]) == lowerAscii(str2[i]))
            c++;
    }

    if ((float)c / (float)t <= 0.5)
        return true;

    return false;
}


bool isProfanity(std::array<std::string, 50> profanity, std::string str)
{
    for (int i=0; i<profanity.size(); i++)
    {
        // if the first character is not the same then we continue
        if (str[0] != profanity[i][0])
            continue;

        if(isCloseMach(str, profanity[i]))
            return true;
    }
    return false;
}


extern "C" {
    char lowerChar(char c)
    {
        return lowerAscii(c);
    }

    bool isCloseMach(char* str1, char* str2)
    {
        return isCloseMach(std::string(str1), std::string(str2));
    }

    bool isProfanity(char* profanity[], char* str)
    {
        std::array<std::string, 50> arr;
        for (int i=0; i<50; i++)
            arr[i] = std::string(profanity[i]);
        return isProfanity(arr, std::string(str));
    }
}
