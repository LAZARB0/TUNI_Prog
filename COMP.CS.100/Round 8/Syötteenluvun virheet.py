"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""

def print_box(width, height, mark):

    """Tulostaa välille nollasta käyttäjän antamaan korkeuteen valitulla merkillä käyttäjän valitseman levysisiä merkkejä"""

    for _ in range(0, height):
        print(width * mark)


def read_input(kysymys):

    """Kysyy ja tarkastaa käyttäjän syötteen"""

    luku = 0

    while luku <= 0:
        try:
            vastaus = input(kysymys)
            luku = int(vastaus)
        except ValueError:
            continue

    return luku


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print("")
    print_box(width, height, mark)


if __name__ == "__main__":
    main()