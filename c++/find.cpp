#include <rapidjson/rapidjson.h>
#include <fstream>
#include <sstream>
#include <string>
#include <regex>

std::string get(std::string fn, std::string regex)
{
    std::ifstream file(fn);

    std::regex reg(regex);

    if (file.is_open())
    {
        std::string line;
        while (std::getline(file, line))
        {
            if (std::regex_match(line, reg))
            {
            }
        }
        file.close();
    }
    return 0;
}
