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
        self.__numerator = int(sievennys)
        sievennys = self.__denominator / divisor
        self.__denominator = int(sievennys)

    def __lt__(self, luku):

        """laventaa ja veratailee murtolukuja"""

        num1 = self.__numerator * luku.__denominator
        num2 = luku.__numerator * self.__denominator

        return num2 - num1 > 0

