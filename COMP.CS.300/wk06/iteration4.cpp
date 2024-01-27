/**
 * iteration4.cc
 *
 * Print all items of a list in a reverse order
 */

/**
 * DO NOT ADD ANY INCLUDES!!
 */

#include "iteration4.hh"
using namespace std;


void printReverse(const list<int>& lst)
{
    auto it = lst.end();
        while (it != lst.begin()) {
            --it;
            cout << *it << ' ';
        }
        cout << endl;
}
