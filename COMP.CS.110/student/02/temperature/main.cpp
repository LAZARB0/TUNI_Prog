#include <iostream>

using namespace std;

int main()
{
    int temperature = 0;
    cout << "Enter a temperature: ";
    cin >> temperature;

    double kerroin = 1.8;

    cout << temperature << " degrees Celsius is " << temperature * kerroin + 32 << " degrees Fahrenheit" << endl;
    cout << temperature << " degrees Fahrenheit is " << (temperature - 32) / kerroin << " degrees Celsius" << endl;


    return 0;
}
