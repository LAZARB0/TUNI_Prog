def keskiarvo(lista):

    """Funktio laskee sille parametrina annetusta listasta keskiarvon ja palauttaa sen"""

    summa = sum(lista)

    alkioiden_maara = len(lista)

    keskiarvo = summa / alkioiden_maara

    return keskiarvo


def varianssi(lista):

    """Funktio laskee sille parametrina annetusta listasta varianssin ja palauttaa sen"""


    summa = sum((lista - keskiarvo(lista)) ** 2)

    varianssi = (1 / (len(lista) - 1)) * summa

    return varianssi


def main():


    var = varianssi([123,456,789])
    print(var)

if __name__ == "__main__":
    main()