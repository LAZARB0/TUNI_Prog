/**
 * iteration3.cc
 *
 * Print beginning half of a list
 */

/**
 * DO NOT ADD ANY INCLUDES!!
 */

#include "iteration3.hh"
using namespace std;


void printHalf(const list<int>& lst)
{
    size_t half_size = lst.size() / 2;
        auto it = lst.begin();
        for (size_t i = 0; i < half_size; ++i, ++it) {
            cout << *it << ' ';
        }
        cout << endl;
}
