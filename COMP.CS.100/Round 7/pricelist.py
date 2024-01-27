"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():


    tuote = "w"
    while tuote != "":
        syöte = input("Enter product name: ")
        tuote = syöte.strip()
        if tuote in PRICES:
            print(f"The price of {tuote} is {PRICES[tuote]:.2f} e")
        elif tuote == "":
            print("Bye!")
        else:
            print(f"Error: {tuote} is unknown.")


if __name__ == "__main__":
    main()
