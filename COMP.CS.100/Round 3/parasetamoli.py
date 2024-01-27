"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""

def calculate_dose(weight, time, total_doze_24):

    """Laskee annosmäärän joka annetaan takaisin pääohjelmalle"""

    paino = int(weight)
    otettu_24 = int(total_doze_24)
    viime_annoksesta = int(time)
    yksittäinen_annos = paino * 15
    varaa = 4000 - otettu_24
    if otettu_24 >= 4000:
        annos = 0
    elif viime_annoksesta < 6:
        annos = 0
    elif yksittäinen_annos <= varaa:
        annos = yksittäinen_annos
    else:
        annos = varaa

    return annos


def main():

    weight = input("Patient's weight (kg): ")
    time = input("How much time has passed from the previous dose (full hours): ")
    total_doze_24 = input("The total dose for the last 24 hours (mg): ")

    annos = calculate_dose(weight, time, total_doze_24)

    print(f"The amount of Parasetamol to give to the patient: {annos}")


if __name__ == "__main__":
  main()
