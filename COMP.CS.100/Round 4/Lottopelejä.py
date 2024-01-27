"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def main():

    kaikki = input("Enter the total number of lottery balls: ")
    arvotut = input("Enter the number of the drawn balls: ")

    pallot = virhetarkastelu(kaikki)
    vedetty = virhetarkastelu(arvotut)

    if pallot != None and vedetty != None:
        pallojen_maara(pallot, vedetty)

        tulos = pallojen_maara(pallot, vedetty)

        if tulos != None:
            print(f"The probability of guessing all {vedetty} balls correctly is 1/{tulos:.0f}")
        else:
            print("At most the total number of balls can be drawn.")

    else:
        print("The number of balls must be a positive number.")


def virhetarkastelu(luku):

    """Tarkistaa onko molemmat syötetyt luvut positiivisia"""

    luku = int(luku)

    if luku > 0:
        return luku
    else:
        return None

    pallot = int(kaikki)
    vedetty = int(arvotut)



def pallojen_maara(pallot, vedetty):

    """Laskee todennäköisyyden ja palauttaa sen takaisin pääohjelmalle"""

    if vedetty > pallot:
        return None
    else:
        result = 1
        for luku in range(1, pallot + 1):
            result = luku * result
        kertoma_pallot = result

        result = 1
        for luku in range(1, vedetty + 1):
            result = luku * result
        kertoma_vedetty = result

        result = 1
        erotus = pallot - vedetty
        if erotus == 0:
            kertoma_erotus = 1
        else:
            for luku in range(1, erotus + 1):
                result = luku * result
            kertoma_erotus = result


        alarivi = kertoma_erotus * kertoma_vedetty

        return kertoma_pallot / alarivi

if __name__ == "__main__":
    main()
