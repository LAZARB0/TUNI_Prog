"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def main():

    kerroin = 1
    repetition_counter = 1
    luku = int(input("Choose a number: "))
    while repetition_counter <= 10:
        vastaus = luku * kerroin
        print(kerroin,"*",luku,"=",vastaus)
        repetition_counter += 1
        kerroin += 1


if __name__ == "__main__":
    main()
