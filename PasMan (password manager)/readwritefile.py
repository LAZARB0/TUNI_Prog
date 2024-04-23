"""
Creator: Lassi Cederlöf
Student id number: 150351065
Email: lassi.cederlof@tuni.fi
"""

def read_file(filename):


    passwords = {}

    try:
        file = open(filename, mode="r")

        for row in file:
            row = row.split(":")
            if row[0] in passwords:
                data = passwords[row[0]]
            else:
                data = {}

            if len(row) == 3:
                data[row[1]] = row[2]
                passwords[row[0]] = data


    except IOError:
        print("Error: the file could not be read.")
        return None

    return passwords

def append_file(filename, credentials):


    passwords = {}

    try:
        file = open(filename, mode="a")
        file.write('\n')
        file.write((f"{credentials[0]}:{credentials[1]}:{credentials[2]}"))

        file.close()


    except IOError:
        print("Error: the file could not be read.")
        return None


def write_file(filename, file):

    try:
        file_new = open(filename, mode="w")

        for service in file.keys():
            for username in file[service].keys():
                user = file[service]
                password = user[username]
                credentials = [service, username, password]

                file_new.write((f"{credentials[0]}:{credentials[1]}:{credentials[2]}"))


    except IOError:
        print("Error: the file could not be read.")
        return None

def main():

    file = read_file("PASMAN/passwords.txt")

    write_file("passes.txt", file)

if __name__ == "__main__":
    main()