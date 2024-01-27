"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def main():

    numbers = []
    print("Give 5 numbers:")
    for _ in range(0,5):
        numero = input("Next number: ")
        numbers.append(numero)

    print("The numbers you entered that were greater than zero were:")
    for number in numbers:
        numero = int(number)
        if numero > 0:
            print(numero)

if __name__ == "__main__":
    main()
