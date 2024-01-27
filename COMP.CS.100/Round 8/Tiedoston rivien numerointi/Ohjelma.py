"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
Email: lassi.cederlof@tuni.fi
"""


def main():

    filename = input("Enter the name of the file: ")

    try:
        file = open(filename, mode="r")
    except OSError:
        print(f"There was an error in reading the file.")
        return

    counter = 0
    for file_rivi in file:
        rivi = file_rivi.rstrip()
        counter += 1
        print(counter,rivi)


if __name__ == "__main__":
    main()
