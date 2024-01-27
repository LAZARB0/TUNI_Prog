"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""

def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    Funktio saa parametrina tiedoston nimen ja palauttaa paluu arvona tideostosta luodun data rakenteen
    """


    data = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            for genre in genres:
                if genre in data:
                    sarjat = data[genre]
                    sarjat.append(name)
                    data[genre] = sarjat
                else:
                    sarjat = []
                    sarjat.append(name)
                    data[genre] = sarjat



        file.close()
        return data

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    lista_aakkosina = sorted(genre_data)
    genret = ', '.join(lista_aakkosina)

    print(f"Available genres are: {genret}")

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        elif genre not in genre_data:
            pass

        try:
            sarjat_aakkosina = sorted(genre_data[genre])
            for sarja in sarjat_aakkosina:
                print(sarja)
        except KeyError:
            pass


if __name__ == "__main__":
    main()
