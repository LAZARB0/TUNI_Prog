/* Mysteerimatto
 *
 * Kuvaus:
 * Ohjelma lukee käynnistyessään kirjastojen kokoelmiin
 * liittyviä tietoja tiedostosta, tallentaa ne sopivaan
 * tietorakenteeseen ja antaa käyttäjälle mahdollisuuden
 * tehdä hakuja kyseiseen tietorakenteeseen.
 *
 * Ohjelma kysyy aluksi käyttäjältä tiedoston nimeä, jota
 * luetaan. Tämän jälkeen käyttäjä voi syöttää komentoja
 * erilaisia toimintoja varten. Ohjelma käyttää annettuja
 * parametrejä tietojen hakemiseen tietorakenteesta ja
 * tulostaa ne käyttäjän nähtäväksi. Lopuksi ohjelman voi
 * sulkea syöttämällä komento <quit>.
 *
 * Ohjelman kirjoittaja
 * Nimi: Lassi Cederlöf
 * Opiskelijanumero: 150351065
 * Käyttäjätunnus: tklace
 * E-Mail: lassi.cederlof@tuni.fi
 *
 * */

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

struct Book
{
    string author;
    string title;
    int reservations;
};

vector<string> split(string str)
// Split funktio jakaa käyttäjän syötteen osiin
// jotta syötettä voidaan lukea osissa: <komento>
// <parametrit>
{
    vector<string> tokens;
    stringstream ss(str);
    string token;

    while (getline(ss, token, ' ')) {
        tokens.push_back(token);
    }

    return tokens;
}

map<string, vector<Book>> read_file()
// read_file funktiota käytetään ohjelman alussa lukemaan
// tiedostroa ja tallentamaan tideoston sisältä tietorakenteeseen
// Tietorakenne on muotoa: map<string, vector<Book>>. Funktio
// palauttaa paluuarvona tietorakenteen, jossa on tiedoston
// sisältö.
{
    map<string, vector<Book>> books;

    string input_file_name = "";
    cout << "Input file: ";
    getline(cin, input_file_name);
    ifstream input_file(input_file_name);
    if ( not input_file ) {
        cout << "Error: input file cannot be opened" << endl;
        return {};
    } else {
        string line;
        while (getline(input_file, line)) {
            stringstream ss(line);

            string library, author, title, reservations_str;
            getline(ss, library, ';');
            getline(ss, author, ';');
            getline(ss, title, ';');
            getline(ss, reservations_str);
            if (library.length() == 0 || author.length() == 0 || title.length() == 0) {
                cout << "Error: empty field" << endl;
                break;
            }
            try {
                int reservations = 0;
                if (reservations_str != "on-the-shelf") {
                    reservations = stoi(reservations_str);
                    }
                if (books.find(library) == books.end()) {
                    vector<Book> new_books = {{author, title, reservations}};
                    books[library] = new_books;
                } else {
                    books[library].push_back({author, title, reservations});
                }
            } catch (const invalid_argument& e){
                cout << "Error: empty field" << endl;
                break;
            }
        }
    }
    input_file.close();
    return books;
}

void reservable(const map<string, vector<Book>>& books, const string& title)
// Komennon reservable toteutus funktiona, jotta main funktio pysyy siistimpänä.
// Funktio ottaa parametrinä tietorakenteen sekä kirjan nimen, jota tarkastellaan.
// Funktiolla ei ole paluuarvoa vaan se suorittaa tulostuksen itsenäisesti.
// Funktio käy läpi kaikki tietorakenteen kirjat ja tarkastaa löytyykö
// parametria vastaava kirja rakenteesta. Mikäli kirja löytyy funktio tallentaa
// tiedon kirjan varausluvusta ja myöhemmin vertaa uusia osumia tähän lukuun.
// Lopuksi funktio tulostaa kaikki kirjastot, joista kirja löytyy pienimmällä
// varausluvulla.
{
    vector<pair<string, int>> reservation_counts;
    for (auto& [library, book_list] : books) {
        for (auto& book : book_list) {
            if (book.title == title) {
                reservation_counts.push_back({library, book.reservations});
            }
        }
    }
    if (reservation_counts.empty()) {
        cout << "Book is not a library book" << endl;
        return;
    }
    sort(reservation_counts.begin(), reservation_counts.end(), [](const auto& a, const auto& b) {
        return a.second < b.second;
    });
    int lowest_reservation_count = reservation_counts.front().second;
    if (lowest_reservation_count >= 100) {
            cout << "Book is not reservable from any library" << endl;
            return;
    } else {
        if (lowest_reservation_count == 0) {
            cout << "on the shelf" << endl;
        } else {
        cout << lowest_reservation_count << " reservations" << endl;
        }
        for (auto& [library, reservations] : reservation_counts) {
            if (reservations == lowest_reservation_count) {
                cout << "--- " << library << endl;
            } else {
                break;
            }
        }
    }
}

int main()
{
    map<string, vector<Book>> books = read_file();
    if (books.empty()) {
        return EXIT_FAILURE;
    }

    while(true)
    {
        string line;
        cout << "lib> ";
        getline(cin, line);
        vector<string> parts = split(line);

        // Hyväksytään tyhjät syötteet
        if(parts.size() == 0)
        {
            continue;
        }
        string command = parts.at(0);


        if(command == "libraries")
        {
        for (auto& [library, book_list] : books) {
                cout << library << endl;
            }
        }


        else if(command == "material")
        {

        if (parts.size() != 2){
            cout << "Error: wrong number of parameters" << endl;
        } else if (books.count(parts.at(1)) == 0) {
            cout << "Error: unknown library" << endl;
        } else {
            vector<Book> book_list = books[parts.at(1)];
            sort(book_list.begin(), book_list.end(), [](const Book& a, const Book& b) { return a.author < b.author; });
            for (auto& book : book_list) {
                cout <<book.author << ": " << book.title << endl;
            }

        }
        }


        else if(command == "books")
        {
            if (parts.size() != 3) {
                cout << "Error: wrong number of parameters" << endl;
            } else if (books.count(parts.at(1)) == 0) {
                cout << "Error: unknown library" << endl;
            } else {
                vector<Book> book_list = books[parts.at(1)];
                sort(book_list.begin(), book_list.end(), [](const Book& a, const Book& b) { return a.author < b.author; });
                int author_found = 0;
                for (auto& book : book_list) {
                    if (book.author == parts.at(2)){
                        author_found = 1;
                        if (book.reservations == 0) {
                            cout << book.title << " --- on the shelf" << endl;
                        } else {
                            cout << book.title << " --- " << book.reservations << " reservations" << endl;
                        }
                    }
                }
                if (author_found != 1) {
                    cout << "Error: unknown author" << endl;
                }
            }
        }


        else if(command == "reservable")
        {
            if (parts.size() < 3) {
                cout << "Error: wrong number of parameters" << endl;
            } else {
                string title = "";

                for (size_t i = 2; i < parts.size(); i++) {
                    title += parts[i];
                    if (i != parts.size() - 1) {
                        title += " ";
                    }
                }
                if (title[0] == '"'){
                    string new_title = title.substr(1, title.length() - 2);
                    title = new_title;
            }
            reservable(books, title);
            }
        }


        else if (command == "loanable") {
            if (parts.size() != 1) {
                cout << "Error: wrong number of parameters" << endl;
            } else {
                vector<Book> loanable_books;
                for (auto& [library, book_list] : books) {
                    for (auto& book : book_list) {
                        if (book.reservations == 0) {
                            bool already_in_loanable = false;
                            for (auto& loanable_book : loanable_books) {
                                if (loanable_book.title == book.title && loanable_book.author == book.author) {
                                    already_in_loanable = true;
                                    break;
                                }
                            }
                            if (!already_in_loanable) {
                                loanable_books.push_back(book);
                            }
                        }
                    }
                }
                if (loanable_books.empty()) {
                    cout << "No loanable books found." << endl;
                } else {
                    sort(loanable_books.begin(), loanable_books.end(), [](const Book& a, const Book& b) {
                        if (a.author == b.author) {
                            return a.title < b.title;
                        }
                        return a.author < b.author;
                    });
                    for (auto& book : loanable_books) {
                        cout << book.author << ": " << book.title << endl;
                    }
                }
            }
        }


        else if(command == "quit")
        {
           return EXIT_SUCCESS;
        }


        else
        {
            cout << "Error: unknown command" << endl;
        }
    }
}
