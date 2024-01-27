"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def main():

    luvut = int(input("How many numbers would you like to have? "))
    vuoro = 1
    for _ in range(1, luvut + 1):
        if vuoro % 3 != 0 and vuoro % 7 != 0:
            print(vuoro)
            vuoro += 1
        elif vuoro % 3 == 0 and vuoro % 7 == 0:
            print("zip boing")
            vuoro += 1
        elif vuoro % 3 == 0 and vuoro % 7 != 0:
            print("zip")
            vuoro += 1
        elif vuoro % 3 != 0 and vuoro % 7 == 0:
            print("boing")
            vuoro += 1


if __name__ == "__main__":
    main()
