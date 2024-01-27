"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def main():

    kuukausi = 1

    # Ensimmäisen kuukauden inflaatioprosentti

    syöte = input(f"Enter inflation rate for month {kuukausi}: ")
    kuukausi += 1
    if syöte == "":
        print("Error: at least 2 monthly inflation rates must be entered.")
    else:
        luku = float(syöte)
        edellinen = luku

    # Toisen kuukauden inflaatioprosentti ja eron laskeminen

    while kuukausi <= 2:
        syöte = input(f"Enter inflation rate for month {kuukausi}: ")
        if syöte == "":
            print("Error: at least 2 monthly inflation rates must be entered.")
            break
        else:
            luku = float(syöte)
            isoin = luku - edellinen
            edellinen = luku
            kuukausi += 1
    print(isoin)

    while kuukausi > 2:
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
                print("isoin", isoin)
                edellinen_ero = luku - edellinen
                edellinen = luku
                kuukausi += 1
                print(isoin)
    print(isoin)

if __name__ == "__main__":
    main()
