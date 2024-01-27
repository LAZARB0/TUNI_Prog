"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def capitalize_initial_letters(nimi):

    """Muuttaa lauseen sanojen ensimmäiset kirjaimet isoiksi ja muut pieniksi"""

    lause = ""
    sanat = nimi.split(" ")
    for luku in range(0, len(sanat)):
        sana = sanat[luku]
        sana = sana.capitalize()
        lause += sana + ' '
    lause = lause.rstrip()
    return lause

def main():

    lause = capitalize_initial_letters('Aatu beetu CEETU Deetu eETU Feetu geetu Heetu IITU jiitu')
    print(lause)
if __name__ == "__main__":
    main()
