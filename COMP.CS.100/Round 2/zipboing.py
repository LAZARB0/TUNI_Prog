"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def main():
    luku = int(input("How many numbers would you like to have? "))
    zip = "zip"
    boing = "boing"
    repetation_counter = 1
    vuoro = 1
    while repetation_counter <= luku:
        if vuoro % 3 != 0 and vuoro % 7 != 0:
            print(vuoro)
            vuoro += 1
            repetation_counter += 1
        elif vuoro % 3 == 0 and vuoro % 7 == 0:
            print("zip boing")
            vuoro += 1
            repetation_counter += 1
        elif vuoro % 3 == 0 and vuoro % 7 != 0:
            print(zip)
            vuoro += 1
            repetation_counter += 1
        elif vuoro % 3 != 0 and vuoro % 7 == 0:
            print(boing)
            vuoro += 1
            repetation_counter += 1

if __name__ == "__main__":
    main()
