"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
Email: lassi.cederlof@tuni.fi
"""

def read_message():

    """Lukee käyttäjän syötteen ja tallentaa viesti, listaan"""

    rivi = "s"
    viesti = []
    while rivi != "":
        rivi = input("")
        viesti.append(rivi)
    del viesti[-1]
    return viesti


def main():

    filename = input("Enter the name of the file: ")

    try:
        file = open(filename, mode="w")
    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return

    print("Enter rows of text. Quit by entering an empty row.")

    teksti = read_message()

    counter = 0
    for syöte_rivi in teksti:
        rivi = syöte_rivi.rstrip()
        counter += 1
        text_line = f"{counter} {rivi}"
        print(text_line, file=file)

    file.close()
    print(f"File {filename} has been written.")


if __name__ == "__main__":
    main()
