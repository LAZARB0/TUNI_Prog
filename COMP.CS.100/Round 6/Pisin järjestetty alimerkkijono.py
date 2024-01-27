"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def longest_substring_in_order(merkkijono):

    """Tutkii annettua merkkijonoa ja palauttaa pisimmän aakosjärjestyksessä olevan alimerkkijonon"""

    aakkoset = "abcdefghijklmnopqrstuvwxyzåäö"

    pisin = ""
    jono = ""
    for luku in range(0, len(merkkijono)):
        if jono == "":
            viimeisin = merkkijono[luku]
            jono += merkkijono[luku]
            pisin = merkkijono[luku]
        elif jono != "":
            indeksi = aakkoset.index(merkkijono[luku])
            viimeisin_indeksi = aakkoset.index(viimeisin)
            if indeksi > (viimeisin_indeksi):
                viimeisin = merkkijono[luku]
                jono += merkkijono[luku]
            else:
                jono = merkkijono[luku]
                viimeisin = merkkijono[luku]

        if len(jono) > len(pisin):
            pisin = jono
    return pisin


def main():

    pisin = longest_substring_in_order("acdkbarstyefgioprtyrtyx")
    print(pisin)
if __name__ == "__main__":
    main()
