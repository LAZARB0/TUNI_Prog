"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""

from math import sqrt


def area(a, b, c):


    """laskee käyttäjän antamilla arvoilla pinta-alan"""
    piiri = a + b + c
    s = piiri / 2
    aass = s - a
    bbss = s - b
    ccss = s - c
    ala = float(sqrt(s * aass * bbss * ccss))

    return ala


def main():
    line = input("Enter the length of the first side: ")
    eka = float(line)
    line = input("Enter the length of the second side: ")
    toka = float(line)
    line = input("Enter the length of the third side: ")
    kolmas = float(line)


    ala = area(eka, toka, kolmas)
    print(f"The triangle's area is {ala:.1f}")


if __name__ == "__main__":
    main()
