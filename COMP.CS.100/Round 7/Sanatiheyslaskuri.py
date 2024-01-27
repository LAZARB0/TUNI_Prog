"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def main():


    sanapankki = {}
    lause = " "
    print("Enter rows of text for word counting. Empty row to quit.")
    while lause != "":

        lause = input("")
        sanalista = lause.split(" ")
        for sana in sanalista:
            sana = sana.lower()
            if sana in sanapankki:
                luku = sanapankki[sana]
                laskuri = luku + 1
                sanapankki[sana] = laskuri
            elif sanalista[0] == "":
                pass
            else:
                sanapankki[sana] = 1

    aakkos_sanapankki = sorted(sanapankki)
    for luku in range(0, len(sanapankki)):
        sana = aakkos_sanapankki[luku]
        print(sana,":",sanapankki[sana],"times")


if __name__ == "__main__":
    main()
