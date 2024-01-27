"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def input_to_list(montako):

    """Lisää käyttäjän antaman luvun verran käyttäjän antamia lukuja listaan"""

    luvut = []
    määrä = int(montako)
    print(f"Enter {määrä} numbers:")
    for _ in range(0, määrä):
        luku = input("")
        luvut.append(luku)
    return luvut

def main():

    montako = input("How many numbers do you want to process: ")
    luvut = input_to_list(montako)
    haettu = input("Enter the number to be searched: ")
    haettu = int(haettu)

    counter = 0
    for luku in luvut:
        if int(luku) == haettu:
            counter += 1

    if counter == 0:
        print(f"{haettu} is not among the numbers you have entered.")
    else:
        print(f"{haettu} shows up {counter} times among the numbers you have entered.")

if __name__ == "__main__":
    main()
