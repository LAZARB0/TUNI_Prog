#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

const std::string HELP_TEXT = "S = store id1 i2\nP = print id\n"
                              "C = count id\nD = depth id\n";


std::vector<std::string> split(const std::string& s,
                               const char delimiter,
                               bool ignore_empty = false)
{
    std::vector<std::string> result;
    std::string tmp = s;

    while(tmp.find(delimiter) != std::string::npos)
    {
        std::string new_part = tmp.substr(0, tmp.find(delimiter));
        tmp = tmp.substr(tmp.find(delimiter) + 1, tmp.size());
        if(not (ignore_empty and new_part.empty()))
        {
            result.push_back(new_part);
        }
    }
    if(not (ignore_empty and tmp.empty()))
    {
        result.push_back(tmp);
    }
    return result;
}

void print_connections(std::map<std::string, std::vector<std::string>>& c, std::string n, int depth)
{

    if (c[n].size() == 0){
        return;
    } else {
        for (std::vector<std::string>::size_type i = 0; i < c[n].size(); i++) {
            std::string connection = c[n][i];
            std::cout << std::string(depth*2, '.') << connection << std::endl;
            print_connections(c, connection, depth+1);
        }
    }

}

int get_depth(std::map<std::string, std::vector<std::string>>& c, std::string n)
{
    int depth = 0;
    while (c.find(n) != c.end()) {
        n = c[n][0];
        depth++;
    }
    return depth;
}

int number_of_connections(std::map<std::string, std::vector<std::string>>& c, std::string n)
{
    int count = c[n].size();
    for (std::vector<std::string>::size_type i = 0; i < c[n].size(); i++) {
        count += number_of_connections(c, c[n][i]);
    }
    return count;
}

int main()
{
    std::map<std::string, std::vector<std::string>> connections;


    while(true)
    {
        std::string line;
        std::cout << "> ";
        getline(std::cin, line);
        std::vector<std::string> parts = split(line, ' ', true);

        // Allowing empty inputs
        if(parts.size() == 0)
        {
            continue;
        }

        std::string command = parts.at(0);

        if(command == "S" or command == "s")
        {
            if(parts.size() != 3)
            {
                std::cout << "Erroneous parameters!" << std::endl << HELP_TEXT;
                continue;
            }
            std::string id1 = parts.at(1);
            std::string id2 = parts.at(2);

            connections[id1].push_back(id2);

        }
        else if(command == "P" or command == "p")
        {
            if(parts.size() != 2)
            {
                std::cout << "Erroneous parameters!" << std::endl << HELP_TEXT;
                continue;
            }
            std::string id = parts.at(1);

            std::cout << id << std::endl;

            print_connections(connections, id, 1);

        }
        else if(command == "C" or command == "c")
        {
            if(parts.size() != 2)
            {
                std::cout << "Erroneous parameters!" << std::endl << HELP_TEXT;
                continue;
            }
            std::string id = parts.at(1);

            int count = number_of_connections(connections, id);
            std::cout << count << std::endl;

        }
        else if(command == "D" or command == "d")
        {
            if(parts.size() != 2)
            {
                std::cout << "Erroneous parameters!" << std::endl << HELP_TEXT;
                continue;
            }
            std::string id = parts.at(1);

            int depth = get_depth(connections, id);
            std::cout << depth + 1 << std::endl;

        }
        else if(command == "Q" or command == "q")
        {
           return EXIT_SUCCESS;
        }
        else
        {
            std::cout << "Erroneous command!" << std::endl << HELP_TEXT;
        }
    }
}
