"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def main():

    kuukausi = 3
    edellinen = 2.2
    edellinen_ero = 0.1
    isoin = 0.1
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
if __name__ == "__main__":
    main()
