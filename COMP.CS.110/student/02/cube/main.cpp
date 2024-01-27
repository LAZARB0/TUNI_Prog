#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int numero = 0;
    cout << "Enter a number: ";
    cin >> numero;


    int kuutio = pow(numero, 3);
    if ( cbrt(kuutio) == numero ){
        cout << "The cube of " << numero << " is " << kuutio << "." << endl;
    } else {
        cout << "Error! The cube of " << numero << " is not " << kuutio << "." << endl;

    }


    return 0;
}
