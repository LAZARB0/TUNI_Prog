"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
Email: lassi.cederlof@tuni.fi
"""


def varianssi(lista):

    valilista = []
    for luku in lista:

        valivaihe = (luku - keskiarvo(lista)) ** 2
        valilista.append(valivaihe)

    summa = sum(valilista)

    varianssi = (1 / (8 - 1)) * summa

    return varianssi
