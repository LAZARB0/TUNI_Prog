#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main()
{
    string input_file_name = "";
    cout << "Input file: ";
    getline(cin, input_file_name);

    ifstream input_file(input_file_name);
    if ( not input_file ) {
        cout << "Error! The file " << input_file_name << " cannot be opened." << endl;
        return 1;
    }
    string rivi;
    map<string, int> pisteet;
    while ( getline(input_file, rivi) ) {
        size_t colonIndex = rivi.find(":");
        string name = rivi.substr(0, colonIndex);
        int points = stoi(rivi.substr(colonIndex + 1));
        pisteet[name] += points;
    }
    cout << "Final scores:" << endl;
    for (auto const& [name, points] : pisteet) {
        cout << name << ": " << points << endl;
    }
    return 0;
}
