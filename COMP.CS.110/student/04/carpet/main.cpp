/* Mysteerimatto
 *
 * Kuvaus:
 *   Ohjelma toteuttaa mysteerimaton, jossa sovelletaan mallintunnistusta
 * (pattern matching). Matto koostuu erivärisistä ruuduista ja samoin
 * malli, mutta mallin koko on aina 2 x 2, eli se koostuu neljästä
 * väriruudusta. Ohjelma etsii mallin esiintymiä matosta.
 *   Ohjelma kysyy ensin maton kokoa (leveys ja pituus). Käyttäjältä
 * kysytään myös, täytetäänkö matto (ruudukko) satunnaisesti arvottavilla
 * vai käyttäjän luettelemilla väreillä. Ensimmäisessä vaihtoehdossa
 * käyttäjältä kysytään satunnaislukugeneraattorin siemenlukua ja
 * jälkimmäisessä häntä pyydetään syöttämään niin monta väriä, kuin matossa
 * on ruutuja, jolloin luetellaan värien alkukirjaimet yhtenä pitkänä
 * merkkijonona.
 *   Joka kierroksella käyttäjältä kysytään etsittävää mallia (neljän
 * merkin/värin muodostamaa merkkijonoa). Ohjelma tulostaa, kuinka monta
 * mallin esiintymää matosta löytyi ja mistä kohdista ne löytyivät.
 *   Ohjelma tarkistaa, oliko käyttäjän antamat värikoodit hyväksyttäviä.
 * Ohjelma päättyy, kun käyttäjä antaa lopetuskomennon (merkki 'q' tai 'Q').
 *
 * Ohjelman kirjoittaja
 * Nimi: Lassi Cederlöf
 * Opiskelijanumero: 150351065
 * Käyttäjätunnus: tklace
 * E-Mail: lassi.cederlof@tuni.fi
 * */

#include <iostream>
#include <random>
#include <vector>
#include <string>

using namespace std;

enum Color {RED, GREEN, BLUE, YELLOW, WHITE, NUMBER_OF_COLORS};

// Värien hallinnointi. "enum Color"-määrittely määrittelee
// värit RED, GREEN, BLUE, YELLOW, WHITE ja NUMBER_OF_COLORS.
// struct ColorInfo, sisältää tiedon värin nimestä ja värin indeksistä.
// vektori "COLORS", sisältää infoa kaikista väreistä.

struct ColorInfo {
    string name;
    Color color_index;
};

const vector<ColorInfo> COLORS = {
    { "R", RED },
    { "G", GREEN },
    { "B", BLUE },
    { "Y", YELLOW },
    { "W", WHITE },
    { "5", NUMBER_OF_COLORS }
};

Color index_to_color(const string& name)
// ottaa vastaan värin nimen merkkijonona ja palauttaa vastaavan
// värin indeksin. Funktio käy läpi kaikki COLORS-vektorin alkiot
// ja vertaa jokaista nimeä parametrina saatuun merkkijonoon.
// Jos vastaava nimi löytyy, funktio palauttaa värin indeksin.
// Muutoin funktion palauttaa NUMBER_OF_COLORS-arvon.
{
    for(auto c : COLORS) {
            if(name == c.name){
                return c.color_index;
            }
        }
        return NUMBER_OF_COLORS;
}

void print_carpet(const vector<vector<string>> &carpet)
// Tuolstaa parametrina annetun matriisin sisällön
// muotoon alkio1 alkio2 alkio 3.....
//         ..........................
{
    for (const auto &row : carpet) {
        for (const auto &col : row) {
            cout << col << " ";
        }
        cout << endl;
    }
}

vector<vector<string>> fill_carpet(bool is_random, int width, int height, string input = "")
// Mikäli käyttäjä haluaa syöttää manuaalisesti muodon,
// käyttäjä antaa muodon merkkijonona.
// Mikäli käyttäjä haluaa satunnaisesti luodun muodon,
// funktio luo matriisin käyttäen "default_random_engine":ä.
{
    vector<vector<string>> carpet(height, vector<string>(width));
    if (is_random){
        default_random_engine rand_gen;
        int seed;
        cout << "Enter a seed value: ";
        cin >> seed;
        rand_gen.seed(seed);
        uniform_int_distribution<int> distribution(0, 4);
        for (auto &row : carpet) {
            for (auto &col : row) {
                col = COLORS[distribution(rand_gen) % COLORS.size()].name;
            }
        }
    } else {
        int index = 0;
        for (auto &row : carpet) {
            for (auto &col : row) {
                col = input[index++];
            }
        }
    }
    return carpet;
}


string color_input(int width, int height)
// Lukee käyttäjän syötämän merkkijonon manuaalista muotoa varten.
// Suorittaa merkkijonolle virhetarkastelun ja palauttaa merkkijonon,
// mikäli virheitä ei löydy. Muutoin palauttaa tyhjän merkkijonon,
// Joka käsitellään erikseen main-funktiossa.
{
    string colors_input;
    cout << "Input: ";
    cin >> colors_input;
    int length = colors_input.length();
    if (length != width * height) {
        cout << " Error: Wrong amount of colors." << endl;
        return "";
    } else {
        for(char c : colors_input) {
            Color color = index_to_color(string(1, toupper(c)));
                if (color != NUMBER_OF_COLORS) {
                continue;
                } else {
                    cout << " Error: Unknown color." << endl;
                    return "";
                    break;
                }
        }
    }
    return colors_input;
}

string pattern_to_find()
// Funktio kysyy käyttäjältä syötettä, minkälaista väri muodostelmaa
// ohjelman tulee etsiä matosta. Suorittaa virhetarkastelun syötteelle,
// Mikäli virhe löytyy funktio pysyy while-loopissa ja ilmoittaa virheen,
// sekä kysyy uutta syötettä. Muutoin looppi katkeaa ja merkkijono palautuu.
{
    string colors_to_find;
    int no_errors = 1;
    while (no_errors == 1) {
        cout << "Enter 4 colors, or q to quit: ";
        cin >> colors_to_find;
        if (colors_to_find == "q" || colors_to_find == "Q") {
            return colors_to_find;
        }
        bool error_found = false;


        for(char c : colors_to_find) {
            Color color = index_to_color(string(1, toupper(c)));
                if (colors_to_find.length() != 4) {
                    cout << " Error: Wrong amount of colors." << endl;
                    break;
                }
                else if (color != NUMBER_OF_COLORS) {
                    error_found = true;
                    continue;
                } else {
                    cout << " Error: Unknown color." << endl;
                    error_found = false;
                    break;
            }
        }
        if (error_found) {
            no_errors = 0;
        }
    }
    int length = colors_to_find.length();
    for (int i = 0; i < length; i++) {
        colors_to_find[i] = toupper(colors_to_find[i]);
    }
    return colors_to_find;
}

bool find_pattern(vector<vector<string>> &carpet, string colors_to_find)
// Ottaa parametrina vastaan matriisin sekä merkkijonon joka sisältää
// värien tiedot joita tulee etsiä matriisista. Käy matriisin läpi ja ilmoittaa,
// jos muoto löytyy, samalla lisäten tiedon "total_found" muuttujaan.
{
    int total_found = 0;

    if (colors_to_find == "q" || colors_to_find == "Q") {
        return true;
    } else {
        for (auto i = 0u; i < carpet.size() - 1; i++) {
            for (auto k = 0u; k < carpet[i].size() - 1; k++) {
                if (carpet.at(i).at(k)[0] == colors_to_find[0]) {
                    if (carpet.at(i).at(k + 1)[0] == colors_to_find[1]){
                        if (carpet.at(i + 1).at(k)[0] == colors_to_find[2]){
                            if (carpet.at(i + 1).at(k + 1)[0] == colors_to_find[3]){
                                cout << " - Found at (" << k + 1 << ", " << i + 1 << ")" << endl;
                                total_found += 1;
                            }
                        }
                    }
                }
            }

        }
        cout << " = Matches found: " << total_found << endl;
        return false;
    }
}

int main()
{
    int width;
    int height;
    cout << "Enter carpet's width and height: ";
    cin >> width >> height;

    if (width < 2 || height < 2) {
        cout << " Error: Carpet cannot be smaller than pattern." << endl;
        return 1;
    }

    vector<vector<string>> carpet;
    int start_index = 0;
    string start_type;
    while (start_index == 0) {
        cout << "Select start (R for random, I for input): ";
        cin >> start_type;
        if (start_type == "i" || start_type == "I") {
            string colors = color_input(width, height);
            if (colors != ""){
                carpet = fill_carpet(false, width, height, colors);
                print_carpet(carpet);
                start_index = 1;
            }

        } else if (start_type == "r" || start_type == "R") {
            carpet = fill_carpet(true, width, height);
            print_carpet(carpet);
            start_index = 1;
        }
    }

    bool find_loop = true;
    while (find_loop) {
        string pattern = pattern_to_find();
        if (find_pattern(carpet, pattern)){
            find_loop = false;
        } else{
            ;
        }
    }

    return 0;
}
