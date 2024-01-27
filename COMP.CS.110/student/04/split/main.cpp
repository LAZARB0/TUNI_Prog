#include <iostream>
#include <string>
#include <vector>
#include <sstream>


std::vector<std::string> split(const std::string& s, char separator, bool ignore_empty = false) {
    std::vector<std::string> result;
    std::stringstream ss(s);
    std::string item;

    while (getline(ss, item, separator)) {
        if (ignore_empty && item.empty()) continue;
        result.push_back(item);
    }
    if (!ignore_empty && s.back() == separator) {
        result.push_back(" ");
    }

    return result;
}


int main()
{
    std::string line = "";
    std::cout << "Enter a string: ";
    getline(std::cin, line);
    std::cout << "Enter the separator character: ";
    char separator = getchar();

    std::vector< std::string > parts  = split(line, separator);
    std::cout << "Splitted string including empty parts: " << std::endl;
    for( auto part : parts ) {
        std::cout << part << std::endl;
    }

    std::vector< std::string > parts_no_empty  = split(line, separator, true);
    std::cout << "Splitted string ignoring empty parts: " << std::endl;
    for( auto part : parts_no_empty ) {
        std::cout << part << std::endl;
    }
}
