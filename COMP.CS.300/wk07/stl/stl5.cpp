#include <iterator>
#include <vector>
#include <algorithm>

#include "test.hh"

using namespace std;


/**
 * @brief Arrange vector in three subsequent sections:
 *        - those divisible by three (asc order)
 *        - those whose reminder is 1 (asc order)
 *        - those whose reminder is 2 (asc order)
 * @param v vector to be sorted
 * @return int EXIT_SUCCESS if everything went OK, EXIT_FAILURE otherwise
 */
int sortMod3(std::vector<int>& v)
{
    auto bound_1 = std::partition(v.begin(), v.end(), [](int a) {return a % 3 == 0;});
    auto bound_2 = std::partition(bound_1, v.end(), [](int a) {return a % 3 == 1;});

    std::sort(v.begin(), bound_1);
    std::sort(bound_1, bound_2);
    std::sort(bound_2, v.end());

    return EXIT_SUCCESS;
}

