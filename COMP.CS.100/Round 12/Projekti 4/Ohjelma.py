"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Creator: Lassi Cederlöf
Student id number: 150351065
Email: lassi.cederlof@tuni.fi

Varastokirjanpitoa sisältävien tiedostojen
kesittelyyn toteutettu ohjelma
"""


LOW_STOCK_LIMIT = 30


class Product:
    """
    This class represent a product i.e. an item available for sale.
    """

    def __init__(self, code, name, category, price, stock):
        self.__code = code
        self.__name = name
        self.__category = category
        self.__original_price = price
        self.__price = price
        self.__stock = stock


    def __str__(self):
        """
        YOU SHOULD NOT MODIFY THIS METHOD or it will mess up
        the automated tests.
        """

        lines = [
            f"Code:     {self.__code}",
            f"Name:     {self.__name}",
            f"Category: {self.__category}",
            f"Price:    {self.__price:.2f}€",
            f"Stock:    {self.__stock} units",
        ]

        longest_line = len(max(lines, key=len))

        for i in range(len(lines)):
            lines[i] = f"| {lines[i]:{longest_line}} |"

        solid_line = "+" + "-" * (longest_line + 2) + "+"
        lines.insert(0, solid_line)
        lines.append(solid_line)

        return "\n".join(lines)

    def __eq__(self, other):
        """
        YOU SHOULD NOT MODIFY THIS METHOD or it will mess up
        the automated tests since the read_database function will
        stop working correctly.
        """

        return self.__code == other.__code and \
               self.__name == other.__name and \
               self.__category == other.__category and \
               self.__price == other.__price

    def modify_stock_size(self, amount):
        """
        YOU SHOULD NOT MODIFY THIS METHOD since read_database
        relies on its behavior and might stop working as a result.

        Allows the <amount> of items in stock to be modified.
        This is a very simple method: it does not check the
        value of <amount> which could possibly lead to
        a negative amount of items in stock. Caveat emptor.

        :param amount: int, how much to change the amount in stock.
                       Both positive and negative values are accepted:
                       positive value increases the stock and vice versa.
        """

        self.__stock += amount

    def get_stock(self):

        """
        Gets and returns the amount of stock the product has

        :return: int, amount of stock of the product
        """

        return self.__stock

    def get_category(self):

        """
        Gets and returns the category of the product

        :return: str, the category of the product
        """

        return self.__category


    def combine(self, product):

        """
        Examines if the two product can be combined, and combines them.
        Products can be combined if price and category is the same.

        :param product: second product that is wanted to be
        combined
        :return: None
        """

        if self.__category != product.__category:

            print(f"Error: combining items of different categories '{self.__category}' and '{product.__category}'.")

        elif self.__price != product.__price:

            print(f"Error: combining items with different prices {self.__price}€ and {product.__price}€.")

        else:

            stock = product.__stock
            self.modify_stock_size(stock)


    def set_sale_price(self, percentage):

        """
        Sets the new price for a product with the
        given percentage as param <percentage>

        :param percentage: float, precentage float
        that the price needs to be discounted with
        :return: None
        """

        if percentage == 0:
            self.__price = self.__original_price
        else:
            price = self.__original_price * ((100-percentage) / 100)
            self.__price = price


def _read_lines_until(fd, last_line):
    """
    YOU SHOULD NOT MODIFY THIS FUNCTION since read_database
    relies on its behavior and might stop working as a result.

    Reads lines from <fd> until the <last_line> is found.
    Returns a list of all the lines before the <last_line>
    which is not included in the list. Return None if
    file ends bofore <last_line> is found.
    Skips empty lines and comments (i.e. characeter '#'
    and everything after it on a line).

    You don't need to understand this function works as it is
    only used as a helper function for the read_database function.

    :param fd: file, file descriptor the input is read from.
    :param last_line: str, reads lines until <last_line> is found.
    :return: list[str] | None
    """

    lines = []

    while True:
        line = fd.readline()

        if line == "":
            return None

        hashtag_position = line.find("#")
        if hashtag_position != -1:
            line = line[:hashtag_position]

        line = line.strip()

        if line == "":
            continue

        elif line == last_line:
            return lines

        else:
            lines.append(line)


def read_database(filename):
    """
    YOU SHOULD NOT MODIFY THIS FUNCTION as it is ready.

    This function reads an input file which must be in the format
    explained in the assignment. Returns a dict containing
    the product code as the key and the corresponding Product
    object as the payload. If an error happens, the return value will be None.

    You don't necessarily need to understand how this function
    works as long as you understand what the return value is.
    You can probably learn something new though, if you examine the
    implementation.

    :param filename: str, name of the file to be read.
    :return: dict[int, Product] | None
    """

    data = {}

    try:
        with open(filename, mode="r", encoding="utf-8") as fd:

            while True:
                lines = _read_lines_until(fd, "BEGIN PRODUCT")
                if lines is None:
                    return data

                lines = _read_lines_until(fd, "END PRODUCT")
                if lines is None:
                    print(f"Error: premature end of file while reading '{filename}'.")
                    return None

                # print(f"TEST: {lines=}")

                collected_product_info = {}

                for line in lines:
                    keyword, value = line.split(maxsplit=1)  # ValueError possible

                    # print(f"TEST: {keyword=} {value=}")

                    if keyword in ("CODE", "STOCK"):
                        value = int(value)  # ValueError possible

                    elif keyword in ("NAME", "CATEGORY"):
                        pass  # No conversion is required for string values.

                    elif keyword == "PRICE":
                        value = float(value)  # ValueError possible

                    else:
                        print(f"Error: an unknown data identifier '{keyword}'.")
                        return None

                    collected_product_info[keyword] = value

                if len(collected_product_info) < 5:
                    print(f"Error: a product block is missing one or more data lines.")
                    return None

                product_code = collected_product_info["CODE"]
                product_name = collected_product_info["NAME"]
                product_category = collected_product_info["CATEGORY"]
                product_price = collected_product_info["PRICE"]
                product_stock = collected_product_info["STOCK"]

                product = Product(code=product_code,
                                  name=product_name,
                                  category=product_category,
                                  price=product_price,
                                  stock=product_stock)

                # print(product)

                if product_code in data:
                    if product == data[product_code]:
                        data[product_code].modify_stock_size(product_stock)

                    else:
                        print(f"Error: product code '{product_code}' conflicting data.")
                        return None

                else:
                    data[product_code] = product

    except OSError:
        print(f"Error: opening the file '{filename}' failed.")
        return None

    except ValueError:
        print(f"Error: something wrong on line '{line}'.")
        return None


def example_function_for_example_purposes(warehouse, parameters):
    """
    This function is an example of how to deal with the extra
    text user entered on the command line after the actual
    command word.

    :param warehouse: dict[int, Product], dict of all known products.
    :param parameters: str, all the text that the user entered after the command word.
    """

    try:
        # Let's try splitting the <parameters> string into two parts.
        # Raises ValueError if there are more or less than exactly two
        # values (in this case there should be one int and one float) in
        # the <parameters> string.
        code, number = parameters.split()

        # First parameter was supposed to be a products code i.e. an integer
        # and the second should be a float. If either of these assumptions fail
        # ValueError will be raised.
        code = int(code)
        number = float(number)

    except ValueError:
        print(f"Error: bad parameters '{parameters}' for example command.")
        return

    # <code> should be an existing product code in the <warehouse>.
    if code not in warehouse:
        print(f"Error: unknown product code '{code}'.")
        return

    # All the errors were checked above, so everything should be
    # smooth sailing from this point onward. Of course, the other
    # commands might require more or less error/sanity checks, this
    # is just a simple example.

    print("Seems like everything is good.")
    print(f"Parameters are: {code=} and {number=}.")


def main():
    filename = input("Enter database name: ")
    # filename = "products.txt"

    warehouse = read_database(filename)
    if warehouse is None:
        return

    while True:
        command_line = input("Enter command: ").strip()

        if command_line == "":
            return

        command, *parameters = command_line.split(maxsplit=1)

        command = command.lower()

        if len(parameters) == 0:
            parameters = ""
        else:
            parameters = parameters[0]

        # If you have trouble undestanding what the values
        # in the variables <command> and <parameters> are,
        # remove the '#' comment character from the next line.
        # print(f"TEST: {command=} {parameters=}")

        if "example".startswith(command) and parameters != "":
            """
            'Example' is not an actual command in the program. It is
            implemented only to allow you to get ideas how to handle
            the contents of the variable <parameters>.

            Example command expects user to enter two values after the
            command name: an integer and a float:

                Enter command: example 123456 1.23

            In this case the variable <parameters> would refer to
            the value "123456 1.23". In other words, everything that
            was entered after the actual command name as a single string.
            """

            example_function_for_example_purposes(warehouse, parameters)


        elif "print".startswith(command) and parameters == "":

            for code in sorted(warehouse):

                print(warehouse[code])


        elif "print".startswith(command) and parameters != "":

            try:
                print(warehouse[int(parameters)])

            except ValueError:
                print(f"Error: product '{parameters}' can not be printed as it does not exist.")

            except KeyError:
                print(f"Error: product '{parameters}' can not be printed as it does not exist.")


        elif "delete".startswith(command) and parameters != "":

            try:
                product = warehouse[int(parameters)]
                stock = product.get_stock()

                if stock <= 0:
                    warehouse.pop(int(parameters))

                elif stock > 0:
                    print(f"Error: product '{parameters}' can not be deleted as stock remains.")

            except KeyError:
                print(f"Error: product '{parameters}' can not be deleted as it does not exist.")
            except ValueError:
                print(f"Error: product '{parameters}' can not be deleted as it does not exist.")



        elif "change".startswith(command) and parameters != "":


            try:
                code, amount = parameters.split(" ")     # Jaetaan parameters muuttujan sisältö kahteen osaan ja
                product = warehouse[int(code)]           # kahteen uuteen muuttujaan. Jos tulee virhe, eli muuttujaa
                product.modify_stock_size(int(amount))   # parameters ei voida jakaa, tulee ValueError käydään
                                                         # virhekäsittely. Tätä keinoa käytetty muissakin kohdissa.
            except KeyError:
                print(f"Error: stock for '{code}' can not be changed as it does not exist.")
            except ValueError:
                print(f"Error: bad parameters '{parameters}' for change command.")


        elif "low".startswith(command) and parameters == "":

            for code in sorted(warehouse):
                if warehouse[int(code)].get_stock() < LOW_STOCK_LIMIT:
                    print(warehouse[int(code)])


        elif "combine".startswith(command) and parameters != "":

            try:
                code1, code2 = parameters.split(" ")

                if code1 == code2:
                    print(f"Error: bad parameters '{parameters}' for combine command.")
                else:

                    product1 = warehouse[int(code1)]
                    product2 = warehouse[int(code2)]

                    product1.combine(product2)
                    warehouse.pop(int(code2))

            except KeyError:
                print(f"Error: bad parameters '{parameters}' for combine command.")
            except ValueError:
                print(f"Error: bad parameters '{parameters}' for combine command.")


        elif "sale".startswith(command) and parameters != "":

            category, percentage = parameters.split(" ")

            try:
                category = category
                percentage = float(percentage)

                counter = 0

                for code in warehouse:
                    product = warehouse[int(code)]              # For loopilla käydään läpi kaikki kategoriaan
                                                                # kuuluvat tuotteet ja alennetaan niiden hinta.
                    if category == product.get_category():      # counteria käytetty laskemaan montako tuotetta
                        product.set_sale_price(percentage)      # alennettu

                        counter += 1
                    else:
                        continue
                print(f"Sale price set for {counter} items.")

            except ValueError:
                print(f"Error: bad parameters '{parameters}' for sale command.")


        else:
            print(f"Error: bad command line '{command_line}'.")


if __name__ == "__main__":
    main()
