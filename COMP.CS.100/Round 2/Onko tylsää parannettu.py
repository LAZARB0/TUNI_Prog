"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def main():
    tylsyys = True

    while tylsyys:
        tylsyys = input("Bored? (y/n) ")
        if tylsyys == "y" or tylsyys == "Y":
            tylsyys = False
        else:
            if tylsyys == "n" or tylsyys == "N":
                tylsyys = True
            else:
                print("Incorrect entry.")

    print("Well, let's stop this, then.")


if __name__ == "__main__":
    main()
