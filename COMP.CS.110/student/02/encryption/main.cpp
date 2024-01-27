#include <iostream>
#include <string>
#include <stdexcept>

using namespace std;

int virhetarkastelu(string salausavain)
{
    if (salausavain.length() != 26) {
        cout << "Error! The encryption key must contain 26 characters." << endl;
        return 0;
    } else {
        for (int i = 0; i <= 25; i = i + 1) {
            if (islower(salausavain[i])){
                continue;
            } else {
                cout << "Error! The encryption key must contain only lower case characters." << endl;
                return 0;
            } }
        string alphabet = "abcdefghijklmnopqrstuvwxyz";
        for (int i = 0; i <= 25; i = i + 1) {
            if (salausavain.find(alphabet[i])<salausavain.length()){
                continue;
            } else {
                    cout << "Error! The encryption key must contain all alphabets a-z." << endl;
                    return 0;
            } }
        return 1;
    }
}


int main()
{
    string salausavain = "";
    cout << "Enter the encryption key: ";
    cin >> salausavain;

    int avain = virhetarkastelu(salausavain);
    if (avain == 0) {
        return 1;
    } else {
        string teksti = "";
        cout << "Enter the text to be encrypted: ";
        cin >> teksti;

        int luku = teksti.length() - 1;
        for (int i = 0; i <= luku; i = i + 1) {
            if (islower(teksti[i])){
                ;
            }
            else {
                cout << "Error! The text to be encrypted must contain only lower case characters." << endl;
                return 1;
            } }

        string salattu_teksti = "";
        string alphabet = "abcdefghijklmnopqrstuvwxyz";
        for (int i = 0; i <= luku; i = i + 1) {
            int index = alphabet.find(teksti[i]);
            char kirjain = salausavain[index];
            salattu_teksti += kirjain;
        }
        cout << "Encrypted text: " << salattu_teksti << endl;
    }

    return 0;
}
