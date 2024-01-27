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

    print("The numbers you entered, in reverse order:")
    for number in range(len(numbers), 0, -1):
        numero = numbers[number - 1]
        numero = int(numero)
        print(numero)

if __name__ == "__main__":
    main()
