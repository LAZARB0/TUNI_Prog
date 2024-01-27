"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
Email: lassi.cederlof@tuni.fi
"""



PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}
def hinta(tuote):

    """Palauttaa dict:in payloadin paluu arvona parametria vasten"""

    return PRICES[tuote]

def main():



    for tuote in sorted(PRICES, key=hinta):
        print(f"{tuote} {PRICES[tuote]:.2f}")



if __name__ == "__main__":
    main()
