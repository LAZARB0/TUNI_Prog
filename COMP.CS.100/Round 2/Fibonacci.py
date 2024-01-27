"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def main():
    luku = int(input("How many Fibonacci numbers do you want? "))
    vuoro = 1
    for vuoro in range(1, luku + 1):
        if vuoro == 1:
            fib = 1
            print("1. 1")
        elif vuoro == 2:
            fib = 1
            print("2. 1")
            edellinen_vuoro = 1
            sitä_edellinen_vuoro = 1
        else:
            fib = edellinen_vuoro + sitä_edellinen_vuoro
            print(f"{vuoro}. {fib}")
            edellinen_vuoro = fib
            sitä_edellinen_vuoro = fib - sitä_edellinen_vuoro

if __name__ == "__main__":
    main()
