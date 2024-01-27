"""
COMP.CS.100
Creator: Lassi Cederlöf
Student id number: 150351065
Email: lassi.cederlof@tuni.fi
"""

def read_file(filename):


    contacts = {}

    try:
        file = open(filename, mode="r")

        otsikkorivi = []
        for row in file:
            row = row.rstrip()
            parts = row.split(";")

            data = {}


            for ind in range(1, len(parts)):
                if contacts == {}:
                    data[parts[ind]] = parts[ind]
                    otsikkorivi.append(parts[ind])
                else:
                    if parts[ind] != "":
                        key = otsikkorivi[ind - 1]
                        data[key] = parts[ind]
            contacts[parts[0]] = data

    except IOError:
        print("Error: the file could not be read.")
        return None

    return contacts

def main():


if __name__ == "__main__":
    main()


