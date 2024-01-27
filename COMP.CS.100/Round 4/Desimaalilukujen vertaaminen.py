"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""



def compare_floats(lukuyksi, lukukaksi, virhetoleranssi):

    """Vertaa lukujen desimaaleja annetulla virhetoleranssilla epsilon"""

    EPSILON = float(virhetoleranssi)
    LUKUYKSI = float(lukuyksi)
    LUKUKAKSI = float(lukukaksi)

    return abs(LUKUYKSI - LUKUKAKSI) < EPSILON

