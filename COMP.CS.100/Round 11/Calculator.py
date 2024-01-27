"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
Email: lassi.cederlof@tuni.fi
"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):

        """
        Simplifies the values on self.__numerator and self.__senominator
        :return: -
        """

        divisor = greatest_common_divisor(self.__numerator, self.__denominator)

        sievennys = self.__numerator / divisor
        num = int(sievennys)
        sievennys = self.__denominator / divisor
        denom = int(sievennys)

        return Fraction(num, denom)

    def complement(self):

        """Palauttaa murtoluvunluvun käänteisluvun"""

        if self.__numerator * self.__denominator < 0:
            num = abs(self.__numerator)
            denom = abs(self.__denominator)
        else:
            num = abs(self.__numerator) - 2 * abs(self.__numerator)
            denom = abs(self.__denominator)
        return Fraction(num, denom)

    def reciprocal(self):

        """Palauttaa murtoluvunluvun vastaluvun"""

        alkionum = self.__numerator
        alkiodenom = self.__denominator

        if self.__numerator * self.__denominator < 0:
            num = - abs(alkiodenom)
            denom = abs(alkionum)
        else:
            num = abs(alkiodenom)
            denom = abs(alkionum)
        return Fraction(num, denom)

    def multiply(self, luku):

        """Palauttaa luvun ja parametrina annetun murtoluvunluvun tulon"""

        kerroinnum = luku.__numerator
        kerroindenom = luku.__denominator
        num = self.__numerator * kerroinnum
        denom = self.__denominator * kerroindenom
        return Fraction(num, denom)

    def divide(self, luku):

        """Palauttaa luvun ja parametrina annetun murtoluvunluvun osamäärän"""

        reci = self.reciprocal()

        tulos = luku.multiply(reci)

        return tulos.reciprocal()

    def add(self, luku):

        """Palauttaa luvun ja parametrina annetun murtoluvunluvun summan"""

        denom = self.__denominator * luku.__denominator

        num1 = self.__numerator * luku.__denominator
        num2 = luku.__numerator * self.__denominator

        numer = num1 + num2

        return Fraction(numer, denom)

    def deduct(self, luku):

        """Palauttaa luvun ja parametrina annetun murtoluvunluvun erotuksen"""

        denom = self.__denominator * luku.__denominator

        num1 = self.__numerator * luku.__denominator
        num2 = luku.__numerator * self.__denominator

        numer = num1 - num2

        return Fraction(numer, denom)

    def __str__(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

    def __lt__(self, luku):

        """laventaa ja veratailee murtolukuja"""

        num1 = self.__numerator * luku.__denominator
        num2 = luku.__numerator * self.__denominator

        return num2 - num1 > 0


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a


def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    Funktio saa parametrina tiedoston nimen ja palauttaa paluu arvona tideostosta luodun data rakenteen
    """


    data = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            nimi, luvut = row.rstrip().split("=")

            luvut = row.rstrip().split("/")

            Fractions[nimi] = Fraction(int(luvut[0]), int(luvut[1]))


        file.close()
        return data

    except ValueError:
        print("Error: the file cannot be read.")
        return None

    except IOError:
        print("Error: the file cannot be read.")
        return None


def main():

    Fractions = {}

    input_command = ""

    while input_command != "quit":

        input_command = input("> ")

        if input_command == "add":


            input_fraction = input("Enter a fraction in the form integer/integer: ")
            input_name = input("Enter a name: ")

            luvut = input_fraction.split("/")

            Fractions[input_name] = Fraction(int(luvut[0]), int(luvut[1]))

        elif input_command == "print":

            input_name = input("Enter a name: ")

            try:
                print(f"{input_name} = {Fractions[input_name].return_string()}")
            except KeyError:
                print(f"Name {input_name} was not found")

        elif input_command == "list":

            keys = Fractions.keys()

            for key in sorted(keys):

                print(f"{key} = {Fractions[key].return_string()}")


        elif input_command == "*":

            name_1 = input("1st operand: ")
            if name_1 not in Fractions:
                print(f"Name {name_1} was not found")
            else:
                name_2 = input("2nd operand: ")

                if name_2 not in Fractions:
                    print(f"Name {name_2} was not found")
                else:

                    result = Fractions[name_1].multiply(Fractions[name_2])

                    print(f"{Fractions[name_1].return_string()} * {Fractions[name_2].return_string()} = {result.return_string()}")

                    simplified = result.simplify()

                    print(f"simplified {simplified.return_string()}")


        elif input_command == "file":

            filename = input("Enter the name of the file: ")

            read_file(filename)

        elif input_command == "quit":

            print("Bye bye!")
            break

        else:
            print("Unknown command!")

if __name__ == "__main__":
    main()
