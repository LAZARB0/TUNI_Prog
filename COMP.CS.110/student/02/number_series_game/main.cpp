#include <iostream>

using namespace std;

int main()
{   int lukumaara = 0;
    cout << "How many numbers would you like to have? ";
    cin >> lukumaara;

    int lapikaydyt_luku = 1;

    while (lukumaara >= lapikaydyt_luku){

        if ( lapikaydyt_luku % 3 == 0 and lapikaydyt_luku % 7 == 0) {
            cout << "zip boing" << endl;
        }
        else if ( lapikaydyt_luku % 3 == 0) {
            cout << "zip" << endl;
        } else if ( lapikaydyt_luku % 7 == 0) {
            cout << "boing" << endl;
        } else {
        cout << lapikaydyt_luku << endl;
        }
        lapikaydyt_luku += 1;
    }
    return 0;
}
