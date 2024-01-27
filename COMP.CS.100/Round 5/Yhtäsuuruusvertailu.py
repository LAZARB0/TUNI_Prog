"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""

def are_all_members_same(lista):


    """Selvittää onko kaikki listan alkiot yhtäsuuret"""

    if lista == []:
        return True
    elif len(lista) == 1:
        return True
    else:
        edellinen = lista[0]
        for luku in lista:
            if luku == edellinen:
                edellinen = luku
            else:
                return False

        return True


