# """
# COMP.CS.100 
# Creator: Lassi Cederlöf
# Student id number: 150351065
# """

def main():
    hinta = (int(input("Purchase price: ")))
    maksettu = (int(input("Paid amount of money: ")))
    palautus = maksettu - hinta
    kympit = palautus // 10
    vitoset = palautus % 10 // 5
    kakkoset = (palautus - kympit * 10) % 5 // 2
    ykköset = (palautus - kympit * 10 - vitoset * 5) % 2
    if palautus <= 0:
        print("No change")
    else:
        print("Offer change:")
        if kympit > 0:
            print(kympit, "ten-euro notes")
        if vitoset > 0:
            print(vitoset, "five-euro notes")
        if kakkoset > 0:
            print(kakkoset, "two-euro coins")
        if ykköset > 0:
            print(ykköset, "one-euro coins")
if __name__ == "__main__":
    main()
