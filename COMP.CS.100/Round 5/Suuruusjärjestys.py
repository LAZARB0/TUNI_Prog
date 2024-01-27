"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def is_the_list_in_order(lista):


    """Selvittää onko kaikki listan alkiot suuruusjärjestyksessä"""

    if lista == []:
        return True
    elif len(lista) == 1:
        return True
    else:
        edellinen = lista[0]
        for luku in lista:
            if luku >= edellinen:
                edellinen = luku
            else:
                return False

        return True
