"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
Email: lassi.cederlof@tuni.fi
"""

class Product:


    """
    This class defines a simplified product for sale in a store.
    """

    def __init__(self, name, initial_price):
        """
        A product object is initialized with the name and
        the initial price.

        :param name: str, the name of the product.
        :param initial_price: float, how much product will
        tcost at the point of creation.
        """

        self.__name = name
        self.__initial_price = initial_price
        self.__price = initial_price
        self.__sale = 0.00

    def printout(self):

        """
        When a product's data is needed to be printed on
        screen this method will handle it.  Also good
        for debugging and testing purposes.
        """


        print(self.__name)
        print("  price ", f"{self.__price:.2f}")
        print("  sale%:",self.__sale)

    def set_sale_percentage(self, percentage):

        kerroin = (100 - percentage) * 0.01

        self.__price = self.__initial_price * kerroin
        self.__sale = percentage


    def get_price(self):

        return self.__price


def main():


    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
