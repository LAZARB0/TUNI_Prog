"""
COMP.CS.100 Programming 1
Code Template
"""

def read_message():

    """Lukee käyttäjän syötteen ja muuttaa sen huudetuksi"""

    rivi = "s"
    viesti = []
    while rivi != "":
        rivi = input("")
        viesti.append(rivi)
    del viesti[-1]
    return viesti

def main():

    print("Enter text rows to the message. Quit by entering an empty row.")

    msg = read_message()

    print("The same, shouting:")
    for luku in range(0, len(msg)):
        huudettuna = msg[luku].upper()
        print(huudettuna)


if __name__ == "__main__":
    main()
