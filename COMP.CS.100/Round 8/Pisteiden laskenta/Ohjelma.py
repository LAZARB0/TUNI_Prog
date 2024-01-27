"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
Email: lassi.cederlof@tuni.fi
"""


def main():

    filename = input("Enter the name of the score file: ")

    try:
        file = open(filename, mode="r")
    except OSError:
        print("There was an error in reading the file.")
        return


    tulokset = {}

    for rivi in file:

        rivi_alkiot = rivi.split()

        if len(rivi_alkiot) < 2:
            print("There was an erroneous line in the file:")
            print(rivi_alkiot[0])
            return
        else:
            if rivi_alkiot[0] in tulokset:
                nimi = rivi_alkiot[0]
                try:
                    pisteet = int(tulokset[nimi])
                    pisteet += int(rivi_alkiot[1])
                    tulokset[nimi] = pisteet
                except ValueError:
                    print("There was an erroneous score in the file:")
                    print(rivi_alkiot[1])
                    return

            else:
                try:
                    pisteet = int(rivi_alkiot[1])
                    nimi = rivi_alkiot[0]
                    tulokset[nimi] = pisteet
                except ValueError:
                    print("There was an erroneous score in the file:")
                    print(rivi_alkiot[1])
                    return

    print("Contestant score:")
    for nimi in sorted(tulokset):

        print(nimi,tulokset[nimi])



if __name__ == "__main__":
    main()
