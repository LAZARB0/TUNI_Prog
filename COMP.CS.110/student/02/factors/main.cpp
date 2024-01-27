#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int luku;
    cout << "Enter a positive number: ";
    cin >> luku;

    int tekijat = 0;
    double p = sqrt(luku);
    int jakaja = round(p);

    while ( tekijat == 0) {
        if (luku <= 0) {
            cout << "Only positive numbers accepted" << endl;
            tekijat += 1;
        }
        else {
            if ( luku % jakaja == 0) {
                int jakaja_2 = luku / jakaja;
                if (jakaja < jakaja_2) {
                    cout << luku << " = " << jakaja << " * " << jakaja_2 << endl;
                } else {
                    cout << luku << " = " << jakaja_2 << " * " << jakaja << endl;
                }
                tekijat += 1;
            }
            else {
                jakaja -= 1;
            }
        }
    }

    return 0;
}
