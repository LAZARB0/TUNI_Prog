"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""

def count_abbas(merkkijono):

    """Laskee kuinka monta abbaa merkkijonossa on"""

    counter = 0
    tilanne = 0
    for kirjain in merkkijono:
        if tilanne == 0:
            if kirjain == "a":
                tilanne += 1
            else:
                tilanne = 0
        elif tilanne == 1:
            if kirjain == "b":
                tilanne += 1
            else:
                tilanne = 0
        elif tilanne == 2:
            if kirjain == "b":
                tilanne += 1
            else:
                tilanne == 0
        elif tilanne == 3:
            if kirjain == "a":
                counter += 1
                tilanne = 1
            else:
                tilanne == 0




    return counter



def main():

    määrä = count_abbas("abbabaaabbaaaaaabbbbbbbabababababaaabbbaabbabbaabbaabbaabbababababbabba")
    print(määrä)



if __name__ == "__main__":
    main()
