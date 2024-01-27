#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

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
    int rivi_numero = 1;
    map<string, int> count;
    map<string, vector<int>> found_at;
    while ( getline(input_file, rivi) ) {
        stringstream ss(rivi);
        string word;
        while (ss >> word) {
            if (find(found_at[word].begin(), found_at[word].end(), rivi_numero) == found_at[word].end()) {
                found_at[word].push_back(rivi_numero);
                count[word]++;
            }

        }
        rivi_numero++;
    }
    input_file.close();

    for (const auto& [sana, maara] : count) {
        cout << sana << " ";
        cout << maara << ": ";
        for (auto it = found_at[sana].begin(); it != found_at[sana].end(); ++it) {
            if (it != found_at[sana].begin()) {
                    cout << ", ";
                }
                cout << *it;
            }
        cout << endl;
        }

    return 0;
}
