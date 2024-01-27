#include <iterator>
#include <vector>
#include <algorithm>

using namespace std;


/**
 * @brief duplicates even numbers in the vector, removes uneven numbers. Example: {1, 2, 3 4} -> {2, 2, 4, 4}
 *
 * @param vec vector to be handled
 */
void duplicateEvenRemoveUneven(std::vector<int>& vec) {

    std::vector<int> result;

    for (const int& num : vec) {
        if (num % 2 == 0) {
            result.push_back(num);
            result.push_back(num);
        }
    }

    vec = result;
}
