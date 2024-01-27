"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""

def main():
    vastausyksi = input("Player 1, enter your choice (R/P/S): ")
    vastauskaksi = input("Player 2, enter your choice (R/P/S): ")
    if vastausyksi == "P" and vastauskaksi == "R":
        print("Player 1 won!")
    elif vastausyksi == "R" and vastauskaksi == "S":
        print("Player 1 won!")
    elif vastausyksi == "S" and vastauskaksi == "P":
        print("Player 1 won!")
    elif vastausyksi == "R" and vastauskaksi == "P":
        print("Player 2 won!")
    elif vastausyksi == "P" and vastauskaksi == "S":
        print("Player 2 won!")
    elif vastausyksi == "S" and vastauskaksi == "R":
        print("Player 2 won!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
