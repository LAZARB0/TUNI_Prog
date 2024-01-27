"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def reverse_name(nimi):

    """Muuttaa nimen oikeaan muotoon"""

    nimet = nimi.split(",")
    if len(nimet) == 2:
        etunimi = nimet[1].strip()
        sukunimi = nimet[0].strip()
        if etunimi == "":
            return sukunimi
        elif sukunimi == "":
            return etunimi
        else:
            nimi = f"{etunimi} {sukunimi}"
            return nimi
    elif len(nimet) == 1:
        return nimi
    else:
        return ""

def main():

    nimet = input("nimet: ")
    nimi = reverse_name(nimet)
    print(nimi)

if __name__ == "__main__":
    main()
