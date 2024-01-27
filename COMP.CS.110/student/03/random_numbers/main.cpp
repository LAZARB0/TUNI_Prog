#include <iostream>
#include <random>
#include <string>

using namespace std;

void produce_random_numbers(unsigned int lower, unsigned int upper)
{
    unsigned int seed;
    cout << "Enter a seed value: ";
    cin >> seed;

    default_random_engine generator(seed);
    uniform_int_distribution<int> distribution(lower, upper);

    char input = 'c';

    while (input != 'q') {
        cout << "" << endl;
        int random_number = distribution(generator);
        cout << "Your drawn random number is " << random_number << std::endl;

        cout << "Press q to quit or any other key to continue: ";
        cin >> input;
    }
}

int main()
{
    unsigned int lower_bound, upper_bound;
    cout << "Enter a lower bound: ";
    cin >> lower_bound;
    cout << "Enter an upper bound: ";
    cin >> upper_bound;

    if(lower_bound >= upper_bound)
    {
        cout << "The upper bound must be strictly greater than the lower bound"
             << endl;
        return EXIT_FAILURE;
    }

    produce_random_numbers(lower_bound, upper_bound);

    return EXIT_SUCCESS;
}
