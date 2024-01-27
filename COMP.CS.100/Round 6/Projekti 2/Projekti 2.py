"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
Email: lassi.cederlof@tuni.fi
"""


def mediaani(lista):

    """Funktio määrittää sille parametrina annetusta listasta mediaanin ja palauttaa sen"""

    lista_jarjestetty = sorted(lista)
    alkioiden_maara = len(lista)

    puolivali = alkioiden_maara / 2

    if puolivali % 1 != 0:      # Laskee mediaanin jos syötteitä on parillinen määrä
        mediaani_alkio = int(puolivali - 0.5)
        mediaani = lista_jarjestetty[mediaani_alkio]
    else:                       # Laskee mediaanin jos syötteitä on pariton määrä
        mediaani = (lista_jarjestetty[int(puolivali)] + lista_jarjestetty[int(puolivali - 1)]) / 2

    return mediaani

def keskiarvo(lista):

    """Funktio laskee sille parametrina annetusta listasta keskiarvon ja palauttaa sen"""

    summa = sum(lista)

    alkioiden_maara = len(lista)

    keskiarvo = summa / alkioiden_maara

    return keskiarvo


def varianssi(lista):

    """Funktio laskee sille parametrina annetusta listasta varianssin ja palauttaa sen"""

    # Sum funktiota ei pysty käyttämään listalle joten käytetään for rakennetta sekä summa muuttujaa
    summa = 0
    for luku in lista:

        summattava = (luku - keskiarvo(lista)) ** 2
        summa += summattava

    varianssi = (1 / (len(lista) - 1)) * summa

    return varianssi

def keskihajonta(lista):

    """Funktio laskee sille parametrina annetusta listasta keskihajonnan ja palauttaa sen"""

    var = varianssi(lista)

    keskihajonta = var ** 0.5

    return keskihajonta

def main():

    print("Enter seawater levels in centimeters one per line.")
    print("End by entering an empty line.")

    syotteet = []

    syote = " "

    # Syötteiden lukeminen ja tallentaminen syotteet listaan

    while syote != "":

        syote = input("")
        if syote != "":
            syote = float(syote)
            syotteet.append(syote)
        else:
            pass

    # Virheilmoitus jos alle kaksi syötettä

    if len(syotteet) < 2:
        print("Error: At least two measurements must be entered!")

    # Jos syötteitä kaksi tai enemmän ohjelma laskee funktioita käyttäen arvot ja tulostaa ne

    else:

        lista_jarjestyksessa = sorted(syotteet)
        pienin_syote = float(lista_jarjestyksessa[0])
        print(f"Minimum:   {pienin_syote:5.2f} cm")

        suurin_syote = float(lista_jarjestyksessa[len(syotteet) - 1])
        print(f"Maximum:   {suurin_syote:5.2f} cm")

        med = float(mediaani(syotteet))
        print(f"Median:    {med:5.2f} cm")

        keskia = float(keskiarvo(syotteet))
        print(f"Mean:      {keskia:5.2f} cm")

        keskih = float(keskihajonta(syotteet))
        print(f"Deviation: {keskih:5.2f} cm")

if __name__ == "__main__":
    main()
