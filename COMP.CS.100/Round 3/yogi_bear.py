"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""

def repeat_name(name, count):

    """Määrittää funktion repeat_name joka toistaa säkeistöissä rivejä 4-6"""
    for _ in range(0, count):
        print(f"{name}, {name} Bear")

def verse(line, nick):

    """Määrittää funktion verse joka toistaa säkeistöjä"""
    name = nick
    print(line)
    print(f"{nick}, {nick}")
    print(line)
    repeat_name(name, 3)
    print(line)
    repeat_name(name, 1)

def main():
    verse("I know someone you don't know", "Yogi")
    print("")
    verse("Yogi has a best friend too", "Boo Boo")
    print("")
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
