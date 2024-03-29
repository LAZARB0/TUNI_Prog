#include <iostream>
#include <string>
#include <algorithm>
#include <random>

int main()
{
    // This is a random number generator that should be given as parameter to the
    // function of the algorithm library to shuffle letters
    std::minstd_rand generator;

    std::cout << "Enter some text. Quit by entering the word \"END\"." << std::endl;
    std::string word;

    while (std::cin >> word)
    {
        if (word == "END")
        {
            return EXIT_SUCCESS;
        }

        if (word.length() > 3)
        {
            std::string::iterator valin_eka = word.begin();
            std::string::iterator valin_vika = word.end();
            ++valin_eka;
            --valin_vika;
            std::shuffle(valin_eka, valin_vika, generator);
        }
	
        std::cout << word << std::endl;
    }
}
