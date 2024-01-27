"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
Email: lassi.cederlof@tuni.fi
"""


def mediaani(lista):

    lista_jarjestetty = sorted(lista)
    alkioiden_maara = len(lista)

    puolivali = alkioiden_maara / 2

    if puolivali % 1 != 0:
        mediaani_alkio = int(puolivali - 0.5)
        mediaani = lista_jarjestetty[mediaani_alkio]
    else:
        mediaani = (lista_jarjestetty[int(puolivali)] + lista_jarjestetty[int(puolivali - 1)]) / 2

    return mediaani