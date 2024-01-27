"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""

from math import pi

def circumference_s(sivu):

    """Laskee käyttäjän valittua s, neliön piirin."""

    side = float(sivu)
    piiri = 4 * side
    return piiri

def surface_s(sivu):

    """Laskee käyttäjän valittua s, neliön pinta-alan."""

    side = float(sivu)
    ala = side * side
    return ala


def circumference_r(sivuyksi, sivukaksi):

    """Laskee käyttäjän valittua r, suorakulmion piirin."""

    side = float(sivuyksi)
    sivu = float(sivukaksi)
    piiri = 2 * side + 2 * sivu
    return piiri


def surface_r(sivuyksi, sivukaksi):

    """Laskee käyttäjän valittua r, suorakulmion pinta-alan."""

    side = float(sivuyksi)
    sivu = float(sivukaksi)
    ala = side * sivu
    return ala

def circumference_c(säde):

    """Laskee käyttäjän valittua c, ympyrän piirin."""

    radius = float(säde)
    piiri = 2 * pi * radius
    return piiri


def surface_c(säde):

    """Laskee käyttäjän valittua c, ympyrän pinta-alan."""

    radius = float(säde)
    ala = pi * radius ** 2
    return ala


def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            sivu = 0
            while sivu <= 0:
                sivu = input("Enter the length of the square's side: ")
                sivu = float(sivu)
            piiri = circumference_s(sivu)
            ala = surface_s(sivu)
            print(f"The circumference is {piiri:.2f}")
            print(f"The surface area is {ala:.2f}")

        elif answer == "r":
            sivu = 0
            side = 0
            while sivu <= 0:
                sivu = input("Enter the length of the rectangle's side 1: ")
                sivu = float(sivu)
            while side <= 0:
                side = input("Enter the length of the rectangle's side 2: ")
                side = float(side)
            piiri = circumference_r(sivu, side)
            ala = surface_r(sivu, side)
            print(f"The circumference is {piiri:.2f}")
            print(f"The surface area is {ala:.2f}")

        elif answer == "c":
            säde = 0
            while säde <= 0:
                säde = input("Enter the circle's radius: ")
                säde = float(säde)
            piiri = circumference_c(säde)
            ala = surface_c(säde)
            print(f"The circumference is {piiri:.2f}")
            print(f"The surface area is {ala:.2f}")


        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()


def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()
