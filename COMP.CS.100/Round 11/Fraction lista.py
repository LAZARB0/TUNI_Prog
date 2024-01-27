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

    def __str__(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

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

def main():

    print("Enter fractions in the format integer/integer.")
    print("One fraction per line. Stop by entering an empty line.")
    inputs = []
    syöte = "s"
    while syöte != "":
        syöte = input("")
        if syöte != "":
            luvut = syöte.split("/")
            inputs.append(Fraction(int(luvut[0]), int(luvut[1])))
        else:
            break

    print("The given fractions in their simplified form:")
    for luku in range(0, len(inputs)):
        murtoluku = inputs[luku]
        print(f"{murtoluku} = {murtoluku.simplify()}")




if __name__ == "__main__":
    main()
