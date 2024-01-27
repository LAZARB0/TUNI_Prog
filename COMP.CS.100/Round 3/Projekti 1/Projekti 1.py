"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def main():

    kuukausi = 1

    # Ensimmäisen kuukauden inflaatioprosenttin syöttö ja tallennus muuttujaksi

    syöte = input(f"Enter inflation rate for month {kuukausi}: ")
    if syöte == "":
        print("Error: at least 2 monthly inflation rates must be entered.")
    else:
        luku = float(syöte)
        edellinen = luku
        kuukausi += 1

    # Toisen kuukauden inflaatioprosenttin syöttö ja tallennus muuttujaksi sekä 1. ja 2. luvun eron laskeminen

    while kuukausi == 2:
        syöte = input(f"Enter inflation rate for month {kuukausi}: ")
        if syöte == "":
            print("Error: at least 2 monthly inflation rates must be entered.")
            break
        else:
            luku = float(syöte)
            isoin = luku - edellinen
            edellinen = luku
            kuukausi += 1

        # Jos käyttäjä syöttää kaksi sopivaa lukua, siirrytään kuukausiin 3->
        # Ensimmäisten kahden inflaatioprosentin ero tallennettuna muuttujaan, isoin

        while kuukausi > 2:
                syöte = input(f"Enter inflation rate for month {kuukausi}: ")
                if syöte == "":
                    break
                else:
                    luku = float(syöte)
                    nykyinen_ero = luku - edellinen
                    if nykyinen_ero < isoin:
                        isoin = isoin
                    else:
                        isoin = nykyinen_ero
                    edellinen_ero = luku - edellinen
                    edellinen = luku
                    kuukausi += 1

        # Kun käyttäjä painaa enter, silmukka katkeaa ja tulostetaan suurin inflatioprosenttiero

        print(f"Maximum inflation rate change was {isoin:.1f} points.")

if __name__ == "__main__":
    main()
