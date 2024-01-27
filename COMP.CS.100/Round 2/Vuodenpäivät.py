"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
"""


def main():
    kuukausi = 1
    päivä = 1
    for _ in range(1, 13):
        if kuukausi == 1 or kuukausi == 3 or kuukausi == 5 or kuukausi == 7 or kuukausi == 8 or kuukausi == 10 or kuukausi == 12:
            for päivä in range(1, 32):
                print(f"{päivä}.{kuukausi}.")
            kuukausi += 1
        elif kuukausi == 4 or kuukausi == 6 or kuukausi == 9 or kuukausi == 11:
            for päivä in range(1, 31):
                print(f"{päivä}.{kuukausi}.")
            kuukausi += 1
        elif kuukausi == 2:
            for päivä in range(1, 29):
                print(f"{päivä}.{kuukausi}.")
            kuukausi += 1
if __name__ == "__main__":
    main()
