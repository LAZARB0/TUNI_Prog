#include <iterator>
#include <vector>
#include <algorithm>

#include "test.hh" // NOT_FOUND constant

using namespace std;


/**
 * @brief Find the median value of a given vector, whose elements are in random
 *        order. Return NOT_FOUND if the size of the vector is zero.
 *
 * @param v unsorted vector
 * @return int calculated median of parameter vector
 */
int findMedian(std::vector<int>& v)
{
    if (v.empty())
    {
        return NOT_FOUND;
    }

    std::sort(v.begin(), v.end());

    if (v.size() % 2 == 0)
    {
        int middle1 = v[(v.size() - 1) / 2];
        int middle2 = v[v.size() / 2];
        return (middle1 + middle2) / 2;
    }
    else
    {
        return v[v.size() / 2];
    }
}

