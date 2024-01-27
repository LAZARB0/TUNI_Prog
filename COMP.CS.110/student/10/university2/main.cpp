/* Yliopisto
 *
 * Kuvaus:
 * Ohjelma luo käynnistyessään luokan unversity, pohjaksi
 * yliopoiston tietojärjestelmälle. Käyttäjä syöttää ohjelmalle
 * PROMPT komennon, jonka mukaan university luokka ajaa komennot.
 *
 * Komennot toteuttavat muiden luokkien (account, cli, course ja utils)
 * avulla halutut toiminnot ja tallentavat ne ohjelman tietorakenteisiin.
 * Ohjelman luokat käyttävät dynaamista muistinhallintaa.
 *
 * Lähes kaikki komennot vaativat komennon tunnisteen sekä parametrejä.
 * Komennot saadaan näkyviin komennolla HELP ja ohjelman voi sulkea
 * komennolla QUIT.
 *
 * Ohjelman kirjoittaja
 * Nimi: Lassi Cederlöf
 * Opiskelijanumero: 150351065
 * Käyttäjätunnus: tklace
 * E-Mail: lassi.cederlof@tuni.fi
 *
 * */


//#include "utils.hh"
#include "cli.hh"
#include "university.hh"
//#include <iostream>
//#include <string>
//#include <vector>
//#include <fstream>

const std::string PROMPT = "Uni> ";


int main()
{
    University* university = new University("tuni.fi");
    Cli cli(university, PROMPT);
    while ( cli.exec() ){}

    delete university;
    return EXIT_SUCCESS;
}

