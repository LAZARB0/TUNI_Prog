"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""

def main():
    tylsyys = True

    while tylsyys:
        tylsyys = input("Answer Y or N: ")
        if tylsyys == "y":
            print("You answered",tylsyys)
            tylsyys = False
        elif tylsyys == "Y":
            print("You answered", tylsyys)
            tylsyys = False
        elif tylsyys == "n":
            print("You answered", tylsyys)
            tylsyys = False
        elif tylsyys == "N":
            print("You answered", tylsyys)
            tylsyys = False
        else:
            print("Incorrect entry.")

if __name__ == "__main__":
    main()