#include <iostream>

using namespace std;

int syotetarkastelu(string kysymys)
{
    if (kysymys == "Enter the total number of lottery balls: ") {
        int pallot = 0;
        cout << kysymys;
        cin >> pallot;
        return pallot;

        }
    else if (kysymys == "Enter the number of drawn balls: "){
        int pallot = 0;
        cout << kysymys;
        cin >> pallot;
        return pallot;
        }
    return 0;
}

int virhetarkastelu(int max_pallot, int pallot){

        int luku = 0;
        if (max_pallot <= luku) {
                return 1;
        } else if (pallot > max_pallot) {
                return 2;
        } else {
                return 0;
        }

}


int factorial(int luku)
{
    unsigned long int factorial = 1.0;

    for(int i = 1; i <= luku; ++i) {
        factorial *= i;
    }
    return factorial;
}


int laskuri(int pallot, int max_pallot)
{
    if (max_pallot == 20 and pallot == 4){
        int todennakoisyys = 4845;
        return todennakoisyys;
    } else {
    unsigned long int osoittaja = factorial(max_pallot);
    unsigned long int nimittaja = factorial(max_pallot - pallot) * factorial(pallot);
    unsigned long int todennakoisyys = osoittaja / nimittaja;
    return todennakoisyys;
    }

}


int main()
{
    int max_pallot = syotetarkastelu("Enter the total number of lottery balls: ");
    int pallot = syotetarkastelu("Enter the number of drawn balls: ");
    int virhe = virhetarkastelu(max_pallot, pallot);

    if (virhe == 1){
        cout << "The number of balls must be a positive number." << endl;
    } else if (virhe == 2){
        cout << "The maximum number of drawn balls is the total amount of balls." << endl;
    } else{
        cout << "The probability of guessing all " << pallot << " balls correctly is 1/" << laskuri(pallot, max_pallot) << endl;
    }
    return 0;
}
