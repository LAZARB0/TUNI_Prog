"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""

def print_box(width, height, mark):

    """Tulostaa välille nollasta käyttäjän antamaan korkeuteen valitulla merkillä käyttäjän valitseman levysisiä merkkejä"""
    for _ in range(0, height):
        print(width * mark)


def main():
    width = input("Enter the width of a frame: ")
    height = input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    width = int(width)
    height = int(height)

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
