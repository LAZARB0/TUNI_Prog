"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""

def create_an_acronym(nimi):

    """Palauttaa akronyymin funktiolle annetusta parametristä"""

    lyhenne = ""
    sanat = nimi.split(" ")
    for luku in range(0, len(sanat)):
        sana = sanat[luku]
        lyhenne = lyhenne + sana[0]
        lyhenne = lyhenne.upper()
    return lyhenne


def main():

    lyhenne = create_an_acronym("central intelligence agency")
    print(lyhenne)

if __name__ == "__main__":
    main()
