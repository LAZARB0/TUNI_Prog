#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    string tiedoston_nimi = "";
    cout << "Input file: ";
    getline(cin, tiedoston_nimi);

    string kirjoitus_tiedosto = "";
    cout << "Output file: ";
    getline(cin, kirjoitus_tiedosto);

    ifstream tiedosto_olio(tiedoston_nimi);
    if ( not tiedosto_olio ) {
        cout << "Error! The file " << tiedoston_nimi << " cannot be opened." << endl;
        return 1;
    } else {
        ofstream tiedosto_olio_2(kirjoitus_tiedosto);
        string rivi;
        int luku = 1;
        while ( getline(tiedosto_olio, rivi) ) {
            tiedosto_olio_2 << luku << " " << rivi << endl;
            luku += 1;
        }
        tiedosto_olio.close();
        tiedosto_olio_2.close();
    }
    return 0;
}
