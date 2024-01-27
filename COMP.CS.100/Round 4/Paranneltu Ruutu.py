"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def print_box(width, height, border_mark="#", inner_mark=" "):

    """Tulostaa välille nollasta käyttäjän antamaan korkeuteen valitulla merkillä käyttäjän valitseman levysisiä merkkejä"""


    print(width * border_mark)
    for _ in range(0, height - 2):
        print(border_mark, end = '')
        print(inner_mark * (width - 2), end = '')
        print(border_mark)
    print(width * border_mark)
    print("")


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)



if __name__ == "__main__":
    main()
