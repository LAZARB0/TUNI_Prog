#ifndef BOOK_HH
#define BOOK_HH

#include <string>
#include "date.hh"


class Book
{
public:

    Book(std::string author, std::string title);

    void loan(class Date);

    void renew();

    void print();

    void give_back();

private:

    std::string author_;

    std::string title_;

    class Date loan_date_;

    class Date return_date_;

    bool is_available_;
};

#endif // BOOK_HH
