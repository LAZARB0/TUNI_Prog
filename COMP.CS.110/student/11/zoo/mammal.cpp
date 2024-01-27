#include "mammal.hh"

Mammal::Mammal()
{
    moving_noise_ = "Kip kop kip kop";
}

void Mammal::suckle(std::ostream &output) const
{
    output << "Mus mus" << std::endl;
}
