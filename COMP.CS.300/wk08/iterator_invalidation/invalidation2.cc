#include <iterator>
#include <vector>
#include <algorithm>

using namespace std;


/**
 * @brief Erases every second item from the vector. Example: {1, 2, 3, 4} -> {1, 3}
 *
 * @param vec vector where every second item is erased.
 */
void eraseEverySecond(std::vector<int>& vec) {
    std::vector<int> newVec;

    for (size_t i = 0; i < vec.size(); i++) {
        if (i % 2 == 0) {
            newVec.push_back(vec[i]);
        }
    }

    vec = newVec;
}
